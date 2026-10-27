# Two-Factor Authentication

## What is two-factor authentication?

ADAM keeps private information about pupils, families and staff. We need to keep it safe.

Two-factor authentication (2FA) adds a second lock to your ADAM account. To sign in, you need two things:

1. Your password.
2. A six-digit code from an app on your phone.

If someone learns your password, they still cannot get in. They would need your phone too.

Your bank may already do something like this. When you pay, it may ask you for a one-time PIN. ADAM works in a similar way.

The code comes from an app on your phone. It is **not** sent by SMS. The app does not need airtime, data or signal to make a code.

> [!WARNING]
> From **1 January 2027**, every staff member must use two-factor authentication. You can set it up now. We suggest you do. After that date, ADAM will make you set it up the next time you sign in. You will not be able to use ADAM until you do.

If you are an ADAM administrator, you must already use two-factor authentication.

You may see a reminder box on your dashboard before then. Click on **Set up two-factor authentication** in the box to start.

## What you need

- Your phone.
- Your computer, signed in to ADAM.
- About two minutes.

## Setting up two-factor authentication

### Step 1: Get an authenticator app { #supported-authenticator-apps }

An authenticator app makes the six-digit codes. You only need one app. These are all free:

- **Google Authenticator**
- **Microsoft Authenticator**
- **Twilio Authy Authenticator** (it used to be called **Authy**)
- **1Password**

![](assets/screenshots/two-factor-authentication/two-factor-authentication-01.png)

Google Authenticator

![](assets/screenshots/two-factor-authentication/two-factor-authentication-02.png)

Microsoft Authenticator

![](assets/screenshots/two-factor-authentication/two-factor-authentication-03.png)

Twilio Authy Authenticator

![](assets/screenshots/two-factor-authentication/two-factor-authentication-16.png)

1Password

Get the app from the App Store or Google Play.

Does your school use Google? Choose **Google Authenticator**. Does your school use Microsoft? Choose **Microsoft Authenticator**.

### Step 2: Open the setup page

1. Sign in to ADAM on your computer.
2. Click on the **Staff tab**.
3. Under the **Security Administration** heading, click on **Manage your Two-Factor Authentication**.

If ADAM needs you to set up two-factor authentication, it opens this page for you when you sign in.

### Step 3: Scan the code

ADAM shows a square black-and-white code. This is called a QR code.

![](assets/screenshots/two-factor-authentication/two-factor-authentication-12.png)

> [!NOTE]
> The QR code in this picture will not scan. Scan the code you see **on your ADAM screen**. Every person gets a different code.

1. Open the authenticator app on your phone.
2. Tap the button to add an account. In Google Authenticator, this is the **+** button at the bottom right.
3. Let the app use your camera if it asks.
4. Point your phone's camera at the QR code on your computer screen.

The app now shows an entry for ADAM in its list. Under it is a six-digit number. The number changes every 30 seconds.

![](assets/screenshots/two-factor-authentication/two-factor-authentication-05.png)

*This is how three accounts look in Google Authenticator. Your app may look different.*

**Can't scan the code?** Click on **I can't scan the code** under the QR code. ADAM shows a "key" made of letters and numbers. In your app, choose to enter a setup key. Type the key in exactly as ADAM shows you.

### Step 4: Type in the six digits

1. Look at the six-digit number in your app.
2. Type it into the **Code from your app** boxes in ADAM.
3. Click on **Turn on two-factor authentication**.

![](assets/screenshots/two-factor-authentication/two-factor-authentication-13.png)

Did ADAM say the code was wrong? The number may have changed while you typed. Try again with the new number. Still not working? See [My code does not work](#my-code-does-not-work).

### Step 5: Save your recovery codes

ADAM now shows a page called **Save your recovery codes**. It lists ten codes.

![](assets/screenshots/two-factor-authentication/two-factor-authentication-14.png)

> [!WARNING]
> ADAM shows these codes **only once**. Save them before you leave this page.

1. Click on **Print these codes** or **Download these codes**.
2. Keep them somewhere safe. Keep them away from your phone. A drawer at home is good.
3. Click on **I have saved my recovery codes**.

Do not leave the codes on your desk beside your computer. Anyone with your password and those codes can get into your account.

You are done. Two-factor authentication now protects your account.

## Signing in to ADAM

1. Sign in with your username and password, as you always do.
2. ADAM asks for a **One Time PIN**. This is the six-digit code.
3. Open the authenticator app on your phone.
4. Type the six digits shown next to ADAM.
5. Click on **Authenticate**.

ADAM never sends you this code. You always get it from the app on your phone.

## Recovery codes

A recovery code is like a spare key. Use one when you cannot use your phone. Maybe your phone is lost, broken, flat, or at home.

A recovery code looks like this:

```
A3F7-K29P
```

- Each code works **once**.
- You get **ten** codes.
- Capital letters do not matter. The dash does not matter.
- There is no number 0 in a code. A round letter is always the letter **O**.

### Signing in with a recovery code

1. Sign in with your username and password.
2. When ADAM asks for your code, click on **I've lost my phone — use a recovery code**.
3. Type one of your recovery codes into the **Recovery Code** box.
4. Click on **Sign in**.

Cross that code off your list. It will not work again.

### Getting new recovery codes

Get new codes if you have used most of them. Get new codes if someone else may have seen them.

1. Click on the **Staff tab**.
2. Under the **Security Administration** heading, click on **Manage your Two-Factor Authentication**.
3. Find the **Recovery codes** box. It shows how many codes you have left.
4. Click on **Generate a new set**.
5. ADAM may ask for your password and your six-digit code. This checks that it really is you.
6. Save the new codes, just like in [Step 5](#step-5-save-your-recovery-codes).

> [!WARNING]
> When you get new codes, **all your old codes stop working**. Throw the old ones away.

## Remembered devices

Your school may let ADAM remember your computer for a while. Then ADAM does not ask for your six-digit code every time you sign in.

If your school does this, you will see a **Remembered devices** box on your two-factor authentication page. It shows how many computers ADAM remembers.

![](assets/screenshots/two-factor-authentication/two-factor-authentication-15.png)

Click on **Sign out all devices** if:

- You signed in on a computer that is not yours.
- You lost a laptop, or someone stole it.

ADAM then forgets every computer. Next time, each computer will ask for your code again. Your two-factor authentication and your recovery codes stay the same.

If the box shows **0**, ADAM is not remembering any computer. There is nothing to sign out.

If you do not see the box at all, your school asks for a code every time you sign in.

## Getting a new phone

Your new phone needs to be set up again. Do this while you still have your old phone, if you can.

1. Sign in to ADAM. Use your old phone to get a six-digit code, or [use a recovery code](#signing-in-with-a-recovery-code) if you do not have your old phone with you
2. [Remove two-factor authentication](#removing-two-factor-authentication) from your account.
3. Set it up again on your new phone. Start at [Step 1](#supported-authenticator-apps).
4. Delete the old ADAM entry from your old app. It will not work any more.

## Removing two-factor authentication

1. Click on the **Staff tab**.
2. Under the **Security Administration** heading, click on **Manage your Two-Factor Authentication**.
3. At the bottom, click on **Remove two-factor authentication**.
4. Type your ADAM password.
5. Click on **Remove two-factor authentication**.

![](assets/screenshots/two-factor-authentication/two-factor-authentication-09.png)

ADAM now shows a new QR code. This means two-factor authentication is off. Your recovery codes stop working too.

Delete the ADAM entry from your authenticator app. It will not work any more.

If your account must use two-factor authentication, ADAM will ask you to set it up again straight away.

## Frequently asked questions

### ADAM did not send me a code. How do I sign in?

ADAM does not send codes. Open the authenticator app on your phone. The code is there.

The app does not need airtime, data or signal.

### I don't have my phone with me. How do I sign in?

Use one of your [recovery codes](#signing-in-with-a-recovery-code).

No recovery codes left? Ask your ADAM administrator for help. They can remove two-factor authentication from your account. Then you can sign in with only your password. You may need to set it up again straight away, so have your phone ready.

Are you the ADAM administrator? Contact ADAM support. We will check who you are before we change anything.

### I deleted the app. Now I can't sign in.

Deleting the app does **not** turn off two-factor authentication. ADAM still asks for a code.

Use one of your [recovery codes](#signing-in-with-a-recovery-code) to sign in. No codes left? Ask your ADAM administrator for help.

> [!WARNING]
> Always remove two-factor authentication in ADAM **before** you delete the app or the ADAM entry in the app.

### My app shows two ADAM codes. Which one do I use?

You may have set up two-factor authentication more than once. Only the newest entry works.

1. Delete every ADAM entry from your app.
2. [Remove two-factor authentication](#removing-two-factor-authentication) in ADAM. Use a recovery code to sign in if you need to.
3. Set it up again from [Step 1](#supported-authenticator-apps).

### I have two ADAM accounts. Can I add both to my app?

Yes. Most apps can hold many accounts. Scan the QR code for each account.

Your app may ask if you want to replace the first one. Say no. You can rename each entry in the app so you can tell them apart and know which one to use for each account.

### My code does not work.

The code changes every 30 seconds. Type the newest number and try again.

Still not working? Your phone's clock may be wrong. The codes depend on the time. If ADAM sees this, it says: *your phone's clock is out of step with this server*.

To fix it:

1. Open your phone's **Settings**.
2. Find the date and time settings.
3. Switch on *automatic time*.
4. Try again.

Are many people at your school having this problem at once? Tell your ADAM administrator. The server's clock may be wrong. See [Allowing for clock drift](two-factor-authentication-for-administrators.md#allowing-for-clock-drift).

### I sign in with a passkey. Do I still need two-factor authentication?

Yes. A passkey is already a second lock, so ADAM does not ask for your code when you use one. But your password still works, so you still need to set up two-factor authentication. It stops anyone who learns your password. See [Passkey Authentication](passkey-authentication.md#passkey-authentication).

### I sign in with Google or Microsoft. Do I still need two-factor authentication?

Yes. Your school may let you skip the ADAM code when you sign in with Google or Microsoft. But your password still works. When you sign in with your password, ADAM asks for your code.

## For ADAM administrators

To remove two-factor authentication for another staff member, see [Two-Factor Authentication for Administrators](two-factor-authentication-for-administrators.md#removing-two-factor-for-another-staff-member). That page also explains the school's settings.
