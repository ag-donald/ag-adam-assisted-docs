#!/usr/bin/env python3
"""
Audit that every endpoint ADAM serves is documented on the right API page.

This file holds the parsers: one for the PHP source that lists the endpoints,
one for the docs/api-*.md pages. It then compares the two and reports the gaps.

Exit codes: 0 when the docs match the source, 1 when there are findings,
2 when the audit cannot run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import NamedTuple

import yaml


class Endpoint(NamedTuple):
    path: str
    method: str

    @property
    def prefix(self) -> str:
        return self.path.split("/", 1)[0]

    def __str__(self) -> str:
        return f"{self.path}:{self.method}"


@dataclass
class Page:
    name: str
    prefixes: list[str]
    headings: list[Endpoint]


_BLOCK_SPLIT = re.compile(r"__set_state\(array\(")
_METHOD = re.compile(r"'method'\s*=>\s*'([^']*)'")
_ENDPOINT = re.compile(r"'endpoint'\s*=>\s*'([^']*)'")
_HEADING = re.compile(
    r"^### ([A-Za-z][A-Za-z0-9_]*(?:/[A-Za-z0-9_-]+)+):([a-z]+)(?:\s+\{#[^}]*\})?\s*$"
)


def parse_source(php_text: str) -> set[Endpoint]:
    """Read (endpoint, method) pairs from the PHP text without running it."""
    found: set[Endpoint] = set()
    for block in _BLOCK_SPLIT.split(php_text)[1:]:
        method = _METHOD.search(block)
        if not method:
            continue
        endpoint = _ENDPOINT.search(block, method.end())
        if endpoint:
            found.add(Endpoint(endpoint.group(1).lower(), method.group(1).lower()))
    return found


def _read_prefixes(name: str, text: str) -> list[str]:
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError(f"{name}: front matter is not closed")
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as err:
        raise ValueError(f"{name}: front matter is not valid YAML: {err}") from err
    if data is None:
        return []
    if not isinstance(data, dict):
        raise ValueError(f"{name}: front matter is not a mapping")
    prefixes = data.get("api_prefixes", [])
    if not isinstance(prefixes, list) or not all(isinstance(p, str) for p in prefixes):
        raise ValueError(f"{name}: api_prefixes must be a list of strings")
    return prefixes


def parse_page(name: str, text: str) -> Page:
    prefixes = _read_prefixes(name, text)
    headings: list[Endpoint] = []
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = _HEADING.match(line)
        if match:
            headings.append(Endpoint(match.group(1).lower(), match.group(2)))
    return Page(name, prefixes, headings)


def load_pages(docs_dir: Path) -> list[Page]:
    return [
        parse_page(path.name, path.read_text(encoding="utf-8"))
        for path in sorted(docs_dir.glob("api-*.md"))
    ]


CHECKS: tuple[str, ...] = (
    "undocumented", "not_in_source", "duplicated", "wrong_page",
    "unassigned_prefix", "prefix_declared_twice", "stale_prefix",
)

_TITLES = {
    "undocumented": "Undocumented",
    "not_in_source": "Not in source",
    "duplicated": "Duplicated",
    "wrong_page": "Wrong page",
    "unassigned_prefix": "Unassigned prefix",
    "prefix_declared_twice": "Prefix declared twice",
    "stale_prefix": "Stale prefix",
}


def audit(source: set[Endpoint], pages: list[Page]) -> dict[str, list[str]]:
    documented = {h for page in pages for h in page.headings}

    pages_by_heading: dict[Endpoint, list[str]] = {}
    for page in pages:
        for heading in page.headings:
            pages_by_heading.setdefault(heading, []).append(page.name)

    declared: dict[str, list[str]] = {}
    for page in pages:
        for prefix in dict.fromkeys(page.prefixes):
            declared.setdefault(prefix, []).append(page.name)

    source_prefixes = {e.prefix for e in source}

    wrong_page = {
        f"{heading} ({page.name})"
        for page in pages
        for heading in page.headings
        if heading in source and heading.prefix not in page.prefixes
    }

    findings = {
        "undocumented": [str(e) for e in source - documented],
        "not_in_source": [str(e) for e in documented - source],
        "duplicated": [
            f"{e} ({', '.join(names)})"
            for e, names in pages_by_heading.items() if len(names) > 1
        ],
        "wrong_page": list(wrong_page),
        "unassigned_prefix": [p for p in source_prefixes if p not in declared],
        "prefix_declared_twice": [
            f"{p} ({', '.join(sorted(names))})"
            for p, names in declared.items() if len(names) > 1
        ],
        "stale_prefix": [
            f"{p} ({name})"
            for p, names in declared.items() if p not in source_prefixes
            for name in names
        ],
    }
    return {check: sorted(findings[check]) for check in CHECKS}


def _fail(message: str) -> int:
    print(f"audit_api_endpoints: {message}", file=sys.stderr)
    return 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--adam", default="~/dev/adam", help="path to the ADAM checkout")
    parser.add_argument("--docs", default=str(Path(__file__).resolve().parent.parent / "docs"),
                        help="path to the docs directory")
    parser.add_argument("--json", action="store_true", help="print the findings as JSON")
    args = parser.parse_args(argv)

    php_file = Path(args.adam).expanduser() / "includes" / "methods_apiresource.php"
    docs_dir = Path(args.docs).expanduser()
    if not php_file.is_file():
        return _fail(f"cannot find {php_file}")
    if not docs_dir.is_dir():
        return _fail(f"cannot find the docs directory {docs_dir}")

    source = parse_source(php_file.read_text(encoding="utf-8"))
    if not source:
        return _fail(f"no endpoints found in {php_file}")
    try:
        pages = load_pages(docs_dir)
    except ValueError as err:
        return _fail(str(err).replace("\n", " "))

    findings = audit(source, pages)
    if args.json:
        print(json.dumps(findings, indent=2))
    elif not any(findings.values()):
        print(f"All {len(source)} endpoints are documented on the correct pages.")
    else:
        for check in CHECKS:
            if findings[check]:
                print(f"{_TITLES[check]} ({len(findings[check])}):")
                for item in findings[check]:
                    print(f"  - {item}")
    return 1 if any(findings.values()) else 0


if __name__ == "__main__":
    sys.exit(main())
