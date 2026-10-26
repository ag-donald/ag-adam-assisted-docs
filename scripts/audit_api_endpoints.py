#!/usr/bin/env python3
"""
Audit that every endpoint ADAM serves is documented on the right API page.

This file holds the parsers: one for the PHP source that lists the endpoints,
one for the docs/api-*.md pages.
"""
from __future__ import annotations

import re
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
