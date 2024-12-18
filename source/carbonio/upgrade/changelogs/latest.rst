
Release 24.12.0
=================

Release Date: December 16th, 2024

New Features List
-----------------

**CO-998: Removed assert cluster apis logic**
   The Assert Cluster API logic has been removed to prevent cluster downtime due to request timeouts when a server is down. This change allows APIs to function correctly even when a server is unavailable.


**CO-1077: Calendar Organizer Tool improvement**
   The Calendar Organizer tool now allows users to view attendees' availability during appointment creation or editing. It helps users identify conflicts and choose a time and date that suits all participants. The organizer's free/busy status is displayed, and users can toggle the visibility of the organizer tool for better usability.


**CO-1132: Enable sending S/MIME signed emails**
   Added support for sending signed emails using S/MIME, enhancing email security and authentication.


**CO-1206: Enhanced side-by-side calendar view**
   The calendar now supports a side-by-side view, allowing managers to easily view and manage multiple team members' schedules with improved visibility and readability of events for better daily planning.


**CO-1214:  Enhanced Contact List with infinite scroll**
   Implemented infinite scrolling for the address book, allowing users to load and view unlimited contacts, resolving the 500-contact limit issue.


**CO-1265: New Feature in Carbonio Webmail "Forward as Attachment" Option Added**
   Carbonio Webmail now features a "Forward as Attachment" option, enabling users to attach an email to a new message, even when visualization options are set by the sender.


**CO-1270: Improve email rendering performance for large attachments**
   The email rendering performance has been optimized for messages with large attachments or content over 1 MB, allowing emails to load faster. Users will receive a warning when an email is too large to be opened directly, with an option to load the entire email content upon request, improving the overall user experience.


**CO-1273: Users can manage personal contact groups**
   Users can now list, create, and modify contact groups from shared accounts, enabling better management of personal contact groups imported from different folders.


**CO-1288: Allow users to show or hide calendar groups**
   Users can now show or hide groups of calendars, enabling a consolidated view of resource availability. This feature allows for streamlined management of multiple calendars, making it easier to check the availability of resources at a glance and improving the overall booking process.


**CO-1295: Salesforce now records WSC-enabled accounts**
   The Salesforce system has been updated to record the number of accounts with the WSC module enabled (`carbonioFeatureChatsEnabled`). Additionally, the WSC enabled/disabled flag (`ft_wsc_basic`) is now included in the subscription details.


**CO-1341: Forward Appointments to Other Users in Carbonio**
   Users can now forward appointments to others directly from their calendar in Carbonio, making it easy to share and delegate appointments with colleagues, clients or team members.


**CO-1352: Email header notifications for user awareness**
   Users now receive visual notifications in the email body and header for external domain origins, confidentiality markers, and distribution-list origins to enhance security awareness. 


**CO-1355: Align Calendar Sender Field with MailsUI**
   The calendar sender field has been updated to align with the one in MailsUI. Users can now send appointments using any of their addresses or identities, even if no persona is set, ensuring consistency and improved usability.


**CO-1392: Compile Carbonio-Mailbox with JDK 17**
   The `carbonio-mailbox` module now supports compilation with JDK 17, ensuring compatibility with the latest Java features and improved performance.


**CO-1394: Carbonio Calendar Update with accurate Invite Details in Shared Calendars**
   Exciting update in Carbonio Calendar! Now, shared calendar invite details display correctly for participants:


**CO-1411: Support added for TIF attachments preview in Mail**
   Users can now preview TIF and TIFF attachments directly within the mail interface. This enhancement improves accessibility and user experience by enabling seamless viewing of these file formats without the need for external applications.


**CO-1422: Global Admin and Domain Admin Can Set Maximum File Upload Size at COS level**
   Global administrators and domain administrators now can configure a maximum file upload size at the COS level. This feature allows for more granular control over data management and file storage


**CO-1431: Conditional display of delete user password button**
   The "Delete User Password From Ldap" button is now conditionally displayed based on the admin's permission for the set.account.userPassword grant. If the admin lacks this permission, the button will be hidden, preventing unauthorized changes and improving security.


**CO-1460: LegalHold help button placement fix**
   The Help Button in the Legal Hold panel has been repositioned to prevent it from overlapping the navigation bar, allowing users to access navigation options while using the Help feature.


**CO-1475: New s/mime signature verification attributes  introduced**
   Carbonio has added a new attribute, carbonioSMIMESignatureVerificationEnabled, to enhance security and user control over S/MIME signatures.


**CO-1482: Refactor COS preferences for improved maintainability**
   The COS preferences section in the Carbonio Admin Console UI has been refactored to enhance code maintainability, readability, and performance. This includes component decomposition, type introduction, redundant code removal, and code reorganization for better extensibility.


**CO-1501: The advanced search enhanced for large results**
   The advanced search functionality in Carbonio has been improved to handle scenarios with over 100 results. The send_before and send_after filters now operate effectively, enabling users to refine and narrow down their search results with greater accuracy.


**CO-1509: Use Retrofit for File downloads in PowerstoreSDK**
   Carbonio PowerStore now features enhanced security with the addition of an authentication route at the proxy level. This update restricts direct access to resources, 


**CO-1513: Enable domain-specific search in SearchByFeatures API**
   Global Admins can now configure domain-specific search rules for the SearchByFeatures API. This allows users from specified domains to search accounts in related domains, improving multi-tenant management. The feature is configurable via AdminUI and CLI, and is exclusive to Carbonio Advanced.


**CO-1528: Enhanced Calendar module  with TIF image preview support**
   The Now Calendar module supports TIF image previews, providing an enhanced user experience for professionals working with high-resolution images. This upgrade allows users to view TIF images directly within the calendar.


**CO-1531: View and manage private appointment details**
   Calendar owners and authorized users can now view private appointment details directly in the calendar view while maintaining privacy. A new feature allows users to toggle the visibility of private appointment details in the calendar's day/week/monthly view, ensuring sensitive information remains hidden during activities like screen sharing.


**CO-1538: Enhanced Meeting Entry Experience for Anonymous Users**
   Anonymous users can now access the meeting entry page seamlessly without encountering the "Something went wrong" popup. The popup, previously triggered by unauthenticated module loading, has been removed. This ensures a smoother experience for users accessing public meeting links, preventing the problematic module (un-authenticate calender module) from loading


**CO-1539: Enhanced Meeting Entry Experience for Anonymous Users**
   Anonymous users can now access the meeting entry page seamlessly without encountering the "Something went wrong" popup. The popup, previously triggered by unauthenticated module loading, has been removed. This ensures a smoother experience for users accessing public meeting links, preventing the problematic module (un-authenticate contact module) from loading


**CO-1557: Enhanced library for carbonio powerstore**
   The library for Carbonio Powerstore has been upgraded to enhance security when downloading data from specific services. This ensures that data remains intact and retains its original size.


**CO-1558: Enhanced security for  bulk account creation**
   The bulk account creation process is now more secure. To eliminate potential security risks, the default password has been removed from the code.


**CO-1567: Improved tooltip name for  distribution List**
   In the latest update to Carbonio, the tooltip name for distribution lists has been simplified for clarity. Previously, it displayed as "distribution list and contact group," which could lead to confusion. Now, it simply shows as "Distribution list," providing a more straightforward and accurate label


**CO-1571: Carbonio Consul path chnaged from health/ready to health /live**
   The Carbonio Consul health check endpoint has been updated from health/ready to health/live.


**CO-1579: Hungarian language support added**
   Enhanced language support by adding Hungarian as an optional language in the UI and administration panel, increasing accessibility for Hungarian-speaking users.


**CO-1593: Enhanced appointment title visibility**
   The Webmail Calendar now features improved visibility for appointment titles within the calendar grid.


**CO-1647: Bouncycastle dependency removed**
   Removed Bouncycastle library dependency from Carbonio Advanced, ensuring improved compatibility and reduced dependencies.


**CO-1648: Improved mail module service catalog**
   Enhanced the mail module service catalog in Carbonio webmail to prevent redundant service requests. Previously, the system would initiate a new request every time the Mail module was accessed. This update optimizes the process, ensuring that once the service is called, it doesn't unnecessarily re-request resources when navigating within the Mail module.


**CO-1651: The LDAP bind password hidden on AdminUI**
   Enhanced security by hiding LDAP search bind password in AdminUI, preventing unauthorized access and exposure.


**CO-1665: Improved Free/Busy status handling for Calendar events**
   Enhancements to the calendar functionality now include a pre-check of existing appointments when adding new attendees. This improvement ensures accurate updates to the free and busy status, providing a smoother scheduling experience.


**CO-1668: Improved appointment forwarding**
   The Carbonio Calendar's appointment forwarding functionality has been improved. Forwarded appointments now trigger accurate notifications to recipients, resolving previous issues with incorrect or missing notifications.


**CO-1694: Mail module enhanced to forward mail as attachment**
   The mail module now allows forwarding emails as attachments in both conversation and message views. This update provides greater flexibility and functionality, enabling users to share emails efficiently while preserving the original context and formatting.


**CO-1709: Enhanced calendar module with "Empty Trash" function**
   The Calendar module has been upgraded with an "Empty Trash" functionality. Users can now easily remove all trashed calendar items by clicking on the trash folder and performing the "Empty Trash" action. Once completed, all listed trashed calendar items will be permanently removed and will no longer appear in the trash folder.


**CO-1732: Improved UX for uploading large attachments in mail**
   Users are now notified with a persistent banner while uploading large attachments and saving drafts. The banner informs users to stay patient as the process may take time. The percentage indicator was removed and replaced with a spinner for a cleaner UI.


**CO-1735: Dark Mode for Mail Previewer**
   Mail previewer now correctly renders in dark mode, providing an improved user experience.


**CO-1751: Enhanced Meeting Entry Experience for Anonymous Users**
   Anonymous users can now access the meeting entry page seamlessly without encountering the "Something went wrong" popup. The popup, previously triggered by unauthenticated module loading, has been removed. This ensures a smoother experience for users accessing public meeting links, preventing the problematic module (un-authenticate mail module) from loading


**DOCS-205: Improved  docs handling for heavy documents**
   Docs now efficiently manages large documents. Documents within the configured size limit will open and preview directly, while larger files will automatically download to your device, ensuring a seamless user experience and smooth performance.


**DOCS-223: Authentication Required for Document Edit/Preview**
   Accessing the edit or preview feature for a document now requires authentication. The carbonio-docs-editor URL has been replaced with a public URL generated by the carbonio-docs-connector, ensuring secure access to documents.


**FILES-75: Service to delete old versions based on configuration**
   A new service has been implemented to automatically delete old versions of files when the `maxNumberVersion` configuration is reduced or when versions exceed the configured age limit. Sysadmins can now configure and manage the maximum number of file versions and the retention period in days.


**FILES-750: Manage files for closed accounts**
   None


**FILES-837: Public link access code enhancement**
   Introduced optional access code for public links, enabling users to share folders securely while adhering to internal policies.


**FILES-839: Video file previews  available**
   The File module has been updated to support in-browser video file previews. Users can now view video content directly within the module, eliminating the need for external downloads or additional software, and enhancing overall user experience and workflow efficiency.


**IN-763: Jython Update for CVE Remediation**
   Enhanced security by updating Jython from 2.5.2 to 2.7.4, resolving CVE-2016-4000 and CVE-2013-2027 vulnerabilities.


**IN-774:   PostJournal configuration removal**
   Removed outdated PostJournal references from master.cf.in file, enhancing security and streamlining Carbonio MTA configuration.


**IN-788: Unused carbonio-perl-mozilla-ca package removed**
   The unused `carbonio-perl-mozilla-ca` package has been removed from the system to streamline dependencies and reduce redundant components, optimizing resource usage.


**IN-796: zmconfigd service fully operational**
   The zmconfigd service issues, including missing attributes, have been resolved. The service now functions as expected without errors when executing the command /opt/zextras/libexec/zmconfigd.

*****

Bugfix List
-----------

**CO-1204: Update to Crabonio CE Webmail Client Auth Module**
   The authentication module of the Crabonio CE webmail client has been updated. Support for EAS (Exchange ActiveSync), Mobile Apps, and OTP (One-Time Password) has been removed as they are no longer supported. The module now retains only the "Change Password" option for user account settings.


**CO-1362: User password button functional for domain admins**
   User management admins can now remove account passwords from LDAP using the "Delete User Password From LDAP" button in the Admin UI, enabling more effective account management without requiring intervention from global admins.


**CO-1363: Enhanced email security: restricted Send-As permissions**
   Strengthened email security by disabling the "Allow sending from any address" option, mitigating potential security risks and ensuring users can only send emails from authorized addresses.


**CO-1364: Admin configurable sender address**
   Admins can now configure the addresses from which users can send emails by setting the zimbraAllowFromAddress value. Users can select or type their desired sender address in the account settings, enhancing flexibility and usability.


**CO-1372: Enhanced Attachment Preview in Carbonio Mail**
   Carbonio Mail now offers an improved attachment preview feature. Only supported document types are displayed


**CO-1373: Mail works without carbonio-preview**
   Improved mail functionality to work seamlessly even when Carbonio-Preview is not installed or available.


**CO-1409: AdminUI authentication settings persistence**
   Enhanced AdminUI to correctly persist zimbraAuthLdapStartTlsEnabled and zimbraFeatureResetPasswordStatus settings, ensuring accurate configuration.


**CO-1416: Advanced modules postgres connection Fixed**
   Improved handling of Postgres connections for advanced modules, ensuring seamless functionality even when Postgres is temporarily unavailable.


**CO-1426: Removal of incorrect read receipt toggle in Admin Panel**
   The "Send Read Receipts" toggle in the admin console has been removed along with the associated field. This ensures that the toggle and field are no longer present since the UI does not support this preference, and the feature will no longer be managed.


**CO-1455: Calendar module enhanced with sharing features**
   The Carbonio Calendar module now allows users to share their calendars with multiple email addresses at once, ensuring all shared addresses remain intact.


**CO-1457: Calendar month view loads all information initially**
   The calendar's month view now loads all event information on first access, eliminating the need for subsequent loading. This improvement ensures a seamless and faster user experience.


**CO-1463: User account deletion successful despite s3 unreachability**
   Carbonio now ensures smooth user account deletion without any errors, even when secondary S3 volumes are not reachable


**CO-1480: Forwarded attendees remain after appointment edits**
   When the organizer edits an appointment, forwarded attendees will now remain on the attendee list, ensuring no attendees are accidentally removed during updates.


**CO-1484: Carbonio startup error resolved**
   A startup error caused by min/max version compatibility issues has been fixed. This resolves errors in the logs, ensuring smoother application startup and improved system reliability.


**CO-1491: Improved share invitation error message**
   The error message displayed when a user attempts to accept a share invitation for a folder that already exists is now more informative, indicating that a folder with the same name already exists and prompting the user to choose a different name.


**CO-1494: Correct display of non-UTF-8 characters in license details**
   he system now supports and correctly displays non-UTF-8 characters (e.g., Arabic, Hindi, Hebrew) in end-user license information after updates.  


**CO-1497: Translation for "Administrators" in Italian UI**
   The Italian Carbonio Admin Panel now correctly displays the translation for the word “Administrators.” Previously, this string was missing in Weblate, preventing translation.


**CO-1503: Modal close functionality improvement in filter**
    The "apply filter" modal now closes successfully when the close icon, cancel button, or apply button is clicked, resolving the previous issue where the modal remained open regardless of user actions.


**CO-1545: Fix incorrect mailbox quota report in Admin UI**
   Resolved the issue where the Admin UI and CSV reports displayed incorrect mailbox quota data in the DF environment. The fix ensures that both the UI and exported reports reflect accurate quota usage values.


**CO-1546: Fixed apply_hsm Error in doRestoreOnNewAccount**
   Resolved the issue where the `carbonio backup doRestoreOnNewAccount` command with `apply_hsm TRUE` fails when both secondary storage and backup are configured with S3. The fix ensures smooth restoration without triggering the `[Guice/NullInjectedIntoNonNullable]` error.


**CO-1553: Email preview auto-resize fixed**
   Fixed regression issue where email preview panel took several seconds to auto-resize, causing poor user experience.


**CO-1563: Enhanced S3 Large File Upload Support**
   Improved Powerstore functionality by updating file size handling from int to long, enabling successful uploads of large files (>300MB) to S3 buckets.


**CO-1585: Carbonio Bootstrap  enhanced for galsync creation**
   Resolved an issue where the Carbonio bootstrap process was stuck during galsync creation due to the mailbox failing to start. The update ensures that the mailbox startup no longer depends on MessageBroker or Consul being fully operational during the bootstrap phase.


**CO-1602: Message deletion behavior fixed**
   Fixed issue where deleted messages disappeared from the inbox but didn't appear in the trash until a manual reload.


**CO-1603: Mail module Update with unread mail count for self-sent message**
   The Mail module improved the mail count feature that accurately tracks unread mail count, even when users send emails to themselves.


**CO-1605: Address book creation fixed**
   Fixed issue where newly created address books didn't appear until the page was reloaded.


**CO-1616: Enhanced  Calendar attendee management**
   Calendar now allows users to seamlessly add new attendees to an existing list without removing previously added attendees. This improvement resolves a bug where adding an attendee inadvertently cleared the existing list, ensuring smooth meeting management.


**CO-1619: Improved move function in Contacts**
   The Contacts module now features an enhanced "Move" function. Users can seamlessly move contacts from one branch to another, with all associated labels displayed correctly.


**CO-1664: Mails module rendering fixed**
   Fixed issue where Mails module was not rendering properly due to incorrect usage of shell functions, ensuring emails are now displayed correctly.


**CO-1666: Large file sharing error fixed**
   Fixed issue where accessing a shared large file (2GB+) resulted in a 504 error, ensuring seamless file sharing.


**CO-1688: Breadcrumbs folder path fixed**
   Fixed issue where breadcrumbs displayed duplicate folder names, ensuring correct path display with proper colors.


**CO-1689: Enhanced email display in mail madule**
   The email rendering in Carbonio Mail has been enhanced to ensure all emails display accurately. This update resolves issues related to rendering errors or missing messages, offering users a seamless and reliable email viewing experience.


**CO-1693: Delegated account sending fixed**
   Fixed issue where delegated accounts couldn't send messages when the account and mailbox were on different application servers.


**CO-1696: Dark mode mail content fix**
   Fixed issue where email content was unreadable in dark mode due to incorrect background and text color rendering.


**CO-1699: WSC chat functions smoothly without default cos**
   The  WSC Chat now functions smoothly even when the default COS is deleted from the domain. Users can create chats and groups without issues.


**CO-1704: Email interaction block fixed**
   Fixed an issue where interacting with certain emails in shared folders would block further interaction with the Mail UI, requiring a browser refresh.


**CO-1705: Mail module enhanced with double-click email opening**
   The mail module has been enhanced to improve user experience. Double-clicking on an email now opens it in a new tab, displaying the full content instead of a blank page.


**CO-1706: Enhanced functional account email tag removal**
   Fixed an issue where removing tags from emails in function accounts didn't refresh the view, requiring a manual browser refresh.


**CO-1717: The eml attachments display enhanced**
   Fixed issue where EML attachments were not displaying correctly when opened in a new tab. The attachment now opens with the correct subject and body.


**CO-1734: Fix for creating new mail filters with redirect**
   Fixed issue where creating a new filter with 'Redirect to' and 'with tag' actions didn't work as expected, and instead updated the previous filter.


**CO-1750: Fixed anonymous access error in WSC meetings**
   Anonymous users can now seamlessly access the meeting entry page without encountering a "Something went wrong" popup. The popup has been removed, ensuring a smoother user experience for public meeting links.


**FILES-744: Drag-and-drop consistency improvement in filters**
   The drag-and-drop functionality within the Recents folder has been improved. Users will now see a gray drop zone when attempting to move a node to an unsupported folder, ensuring clear feedback and consistent behavior.


**FILES-834: Filename unchanged when drag & dropping in the same folder**
    The file name remains unchanged when dragging and dropping the file into the same directory, preventing accidental overwriting of files.


**FILES-850: File module security enhanced for public links**
   The Carbonio File module now includes an improved security feature. When a public link is revoked, it becomes immediately inaccessible, returning a 404 error. This enhancement ensures that revoked links are effectively disabled, preventing further unauthorized access.


**FILES-871: Purge All Versions file preservation**
   Enhanced file versioning to prevent accidental deletion of the current file version when purging all versions, ensuring file integrity.


**FILES-879: Fix account deletion powerstore issue**
   When an admin deletes an account, the system now correctly removes the account's data from Powerstore, preventing failed calls due to the account no longer being available.

*****

End of changelog
