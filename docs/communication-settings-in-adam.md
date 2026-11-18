# Communication Settings in ADAM

## Introduction

In order to send emails from ADAM’s [Messaging Centre](messaging-centre.md#messaging-centre), and to receive automated notifications from ADAM, it will be necessary to link ADAM up to an SMTP service provider through which it can send emails.

Navigate to **Administration → Site Administration → Edit site settings**. On the **Communications** tab, scroll down to the **Email Settings** section.

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-01.png)

The **Email Return Name** and **Email “From” Address** fields are used only when ADAM sends an automated notification email - in other words, an email that wasn’t sent by a person.

> [!NOTE]
> Where a user sends a message from the Messaging Centre, ADAM will use their name as the “Return Name” and their email address and the “From Address”. This ensures that any replies to that person’s email are directed to them and not to another person who may not understand the reason for the reply.

The **SMTP Server for Outgoing Mail** and the **SMTP Server Port for Outgoing Mail** need to be specified and your network support personnel are best positioned to tell you what details go here. This includes whether the connection is **SSL** protected, and the **SMTP Username**  and **SMTP Password**.

The **SMTP Session Limit** tells ADAM how many emails its allowed to send once it has logged on to the server. Some servers have low limits, and others have higher limits. Again, your network support personnel are the best people to ask. If in doubt, leave this at **50**. It can always be changed later.

The **Sending Mode** is important. The ideal scenario is to **Deliver from “sending user”**. However, this requires that the **SMTP Username** is permitted to send email on behalf of other users. This isn’t always allowed by email service providers.

A good option as a second choice, but one which is not permitted by many email servers is option 2: deliver from “sending user” with the return path as the “from” address.

Depending on how your email server is configured, if it doesn’t allow the SMTP Username to deliver on behalf of other users, you may have to rely on a “reply-to” address for the sending user. The safest option is likely “5”, but this looks least professional on the receiving end.

If you’re in doubt, experiment with these in order from 1 to 5 to see which works for your network.

## Testing Mail Sending

To test these sending settings, you can navigate to **Administration → Messaging Administration → Send test emails**.

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-02.png)

Enter your own email address in the **Deliver To** field and click on the **Send** button. Note that changing the “From” option allows you to test the difference between an automated email (from ADAM) vs a message sent by a person from the Messaging Centre (“from You”).

When you click on the Send button, ADAM will immediately send you an email. Check your email inbox.

If you get an error message reported, you may need to check the error logs to see what problem ADAM encountered.

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-03.png)

### Checking the Error Logs

Navigate to **Administration → Debugging and Error Logging → View error log**.

In the log, within the first few rows, you may see one or more “Warnings” that are associated with the page “classes/ADAM/EmailMessage”:

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-04.png)

On the right-hand side (you may need to scroll across, horizontally to see it), you should see an error message (in the diagram below, we’ve covered up some confidential information!):

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-05.png)

Be sure to pass this error message on to your network support personnel for them to assist in resolving the issue.

### Understanding What Else Could Go Wrong

If you sent the message and received a success notification, it means that ADAM successfully handed the email over to the SMTP server. In this instance, you won’t see any error messages in the error log. However, lots can still go wrong. The problem is that none of this is in ADAM’s hands any more. Like a letter in the mail, we can ensure the address is correct and that we have the correct stamps in place, but from the moment you put it in a postbox, you no longer have any control over its delivery.

If you don’t receive the email from ADAM, you can check your junk mail or spam folder to see if it’s there. If not, you’ll have to get further help from your network support personnel who can investigate further.

Have a look at the section below on [improving email deliverability](#improving-email-deliverability).

## Improving Email Deliverability

When computers see multiple copies of the same email emanating from a single IP address, they generally treat that email more suspiciously than they would any other email destined to only one or two recipients.

End users may find that mail sent via ADAM lands up in their spam or junk mail folders, or may not be delivered at all.

To combat this, it is important that you take precautions to ensure that your mail is properly configured. There are a number of techniques that can help with this.

We recommend using [MXToolbox’s Email Health service](https://mxtoolbox.com/emailhealth) for more information regarding your email domain’s deliverability.

### Sender Framework Policy (SPF) Configuration

One of the simplest techniques to combat spam is to create or update your domain’s SPF record. This record, stored in your domain’s “zone file.” Your ISP may be required to make these changes for you.

The SPF record works by listing the IP addresses of all the servers that are permitted to send email addressed from your email domain. This reduces the chances of recipient email servers from treating your email as spam.

**Setting up an SPF record is strongly recommended.**

For schools that make use of our managed hosting service, we recommend adding our ADAM SPF configuration to your SPF record. Schools that send email via Google’s “Google Workspace for Education” would likely have an SPF record such as:

v=spf1 include:\_spf.google.com ~all

### Domain Keys Identified Mail (DKIM) Signing

DKIM is a robust method which signs individual emails with a cryptographic signature that can be verified online by a receiving email server. Because they are essentially impossible to fake, mail that has a valid DKIM signature is almost certainly not spam mail.

Setting up DKIM signing is different for each service provider. Google’s “Google Workspace for Education” makes this a simple 1-click operation to turn on, but does require further setup in your domain’s “zone file”. Your ISP may be required to make these changes for you.

If DKIM signing is enabled for your domain, it is recommended that email sent via ADAM is relayed to your DKIM-signing SMTP server so that it too can be sent with the benefit of DKIM signatures.

### DMARC Records

Although servers can voluntarily check and decide how to deal with mail based on the results of SPF and DKIM signing, DMARC records provide explicit instructions on how email servers should treat mail that emanates either from untrusted origins or from unsigned sources.

Once again, this does require configuration and setup in your domain’s “zone file”. Your ISP may be required to make these changes for you.

## Sending email from ADAM if you use Google Workspace

If you are a “Google School” that makes use of Google’s email offering, then the preferred method of mail delivery, to reduce the possibility that emails sent from your ADAM server will be interpreted by the recipients as spam mail.

### Configure Google Workspace

Follow [the official instructions](https://support.google.com/a/answer/2956491?hl=en) to configure the SMTP relay service in Google Workspace’s Admin Console.

However, please take note of the following points:

-   Allow **Only addresses in my domains**. This means that any of your users who can send mail in ADAM will have their mail processed through Google.

### Configure ADAM

Instructions are provided here to configure popular mail servers to communicate through Google’s SMTP relay services, but configuring ADAM is reasonably straightforward.

Navigate to the ADAM Site Settings: **Administrator → Site Administration → Edit site settings**.

On the **Communications** tab, scroll down to **Email Settings**. Update the following settings as indicated:

-   **SMTP Server for Outgoing Mail:** smtp-relay.gmail.com
-   **SMTP Server Port for Outgoing Mail:** 587
-   **SMTP Server Requires SSL:** Yes
-   **SMTP Username:** The email address of the user account you wish to authenticate with, if you chose to authenticate with a user when setting up the relay. *If you are using IP address authentication, you can ignore this. Note that while it is possible to use IP authentication when you host on our cloud service, the IP address may change without notice.*
-   **SMTP Password:** The password as set for that user. *Leave blank if using IP authentication.*
-   **SMTP Session Limit:** 50

> [!NOTE]
> If you see that any of these settings are “Set in the configuration file” and your ADAM server is hosted on our cloud platform, please contact [ADAM Support](mailto:help@adam.co.za) so that we can assist you in changing these settings! If you host your own ADAM server, please see elsewhere in this documentation for assistance [editing the configuration file](server-setup-and-configuration.md#editing-the-configuration-file).

Once finished, save the settings. Navigate to **Administration → Messaging Administration → Send test emails**. From here, send yourself an email and check that:

1.  ADAM reports a success; and
2.  the email arrives in your inbox.

If you can tick off both of those, then your mail is set up correctly.

## Sending email from ADAM if you use Microsoft’s O365

> [!WARNING]
> Firstly, a disclaimer: we have noticed that mail delivery via O365 is not perfect and Microsoft itself can block your server from delivering messages to it if it considers those messages to be spam-like. ADAM has no control over the email that you send (i.e. its content, frequency and user-friendliness) and has no control over how Microsoft chooses to interpret that email. Your experience may vary!

### Configuring O365

Follow the [instructions on Office 365’s official help site](https://learn.microsoft.com/en-us/Exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365#smtp-relay-configure-a-connector-to-relay-email-from-your-device-or-application-through-microsoft-365-or-office-365) for details on how to “Configure a connector to relay SMTP email”.

You will need to know the IP address of your ADAM server. If you make use of a hosted ADAM server, please inform us so that we can give you the IP address of the server.

### Configuring ADAM

Navigate to the ADAM Site Settings: **Administrator → Site Administration → Edit site settings**.

On the **Communications** tab, scroll down to **Email Settings**. Update the following settings as indicated:

-   **SMTP Server for Outgoing Mail:** The “POINTS TO” address
-   **SMTP Server Port for Outgoing Mail:** 25
-   **SMTP Server Requires SSL:** Yes
-   **SMTP Username:** leave blank
-   **SMTP Password:** leave blank
-   **SMTP Session Limit:** 50

## Alternative Configuration for Microsoft’s O365

> [!WARNING]
> Kindly note that these are theoretical settings that have not been tested. They may be more reliable than the method discussed above, but have much more stringent controls with regards to the volume of messages that can be sent. **Try this at your own risk and make sure to [monitor the messaging centre batches](#troubleshooting-email-delivery-issues-in-adam) for failure notifications.**

This method makes use of a single address to send email from ADAM. We recommend creating a single user in your O365 control panel for this purpose. The user should be sufficiently generic (e.g. “Example School’s ADAM”. The user should have a strong password associated with it.

### Configuring Office 365 - Alternative Method

Follow the [instructions on Office 365’s official help site](https://docs.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-office-3) for **Option 1**.

### Configuring ADAM - O365 Alternative Method

Navigate to the ADAM Site Settings: **Administrator → Site Administration → Edit site settings**.

On the **Communications** tab, scroll down to **Email Settings**. Update the following settings as indicated:

-   **Email From Name:** give the name of the user chosen above. A good example of this would be “*Example School’s* ADAM”
-   **Email From Address:** give the address of the user chosen above.
-   **SMTP Server for Outgoing Mail:** smtp.office365.com
-   **SMTP Server Port for Outgoing Mail:** 587
-   **SMTP Server Requires SSL:** Yes
-   **SMTP Username:** give the address of the user chosen above.
-   **SMTP Password:** give the password of the user chosen above.
-   **SMTP Session Limit:** 50
-   **Sending Mode:** 5. Deliver from ‘SMTP username’ with ‘reply-to’ as sending user.

## Troubleshooting Email Delivery Issues in ADAM

Have a look at the section above on [improving email deliverability](#improving-email-deliverability).

ADAM does not deliver mail directly to the recipients. It requires an intermediate server to take over the delivery of the mail. This is done for a number of reasons:

1.  ADAM delivers emails one at a time, in the order that the emails were loaded.
2.  ADAM is designed to “fail easily” when sending messages.
3.  There are many complexities with sending email that are better left to specialist software.

ADAM processes email in a queue, and sends messages one at a time. This means that delivery is slow. By using an intermediate server, the messages can be handed off to that server quickly since it has only one computer to talk to (which is normally on the same LAN or even same computer as ADAM). This software can then deliver email more efficiently to recipients by delivering mail in parallel and retrying the delivery of messages that couldn’t be sent on their first attempt.

### Step 1: Did ADAM send the message?

The first thing for a site administrator to do is to check the messaging batch records. These can be found **Administration → Messaging Administration → View Messaging Centre Batches**.

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-06.png)

Click on the **view** link to view the details of a batch.

Here, ADAM records whether an email was sent and, depending on the email program that the recipient is using, when the message was opened.

ADAM will list the time that the email message was processed if it was successful, or list the fact that there was an error at that time. If ADAM shows an Error, then the message was not sent.

![](assets/screenshots/communication-settings-in-adam/communication-settings-in-adam-07.png)

If ADAM did not send the messages (there is an “Error” listed under “Processed”), then you will need to investigate:

1.  Which server is ADAM talking to (set in the **Site Settings** under the **Communications** tab, look for **SMTP Server**)?
2.  Is ADAM using the right authentication credentials to talk to the SMTP server?
3.  Is the SMTP server on and configured to listen to ADAM?

Advanced network administrators will want to check the logs of their SMTP server to see if there are clues there are to why the emails from ADAM are not being accepted for delivery.

Further information as to *why* ADAM didn’t succeed in delivery are shown in the ADAM Error Logs.

### Step 2: Check your mail server for issues

From this point on, you will want to engage the services of an email server expert to determine why your email isn’t being delivered. Unfortunately, after the email is passed to the upstream SMTP server, the delivery of those emails are out of our control. To use an apt analogy: once you drop the letter into a postbox for delivery by the post office, you no longer have control over its delivery.

### Step 3: One mail or an entire batch?

If you receive a bounce notification for a single email - or perhaps each time a batch is sent, a familiar set of bounce notifications return, then you will need to check that those email addresses are captured correctly. It may be that an email address no longer exists, that the mailbox is full or a host of other reasons. These are all out of our (and your!) control.

Very often, a telephone call to the recipient is best to determine whether there is an alternative email address that you can use instead.
