## Functional Requirements

- [x] ~~Milestone 2: (1) sending an email @n-k-leung~~
- [x] ~~Milestone 2: (2) deleting an email @n-k-leung~~
- [ ] Milestone 3: (3) flagging an email as urgent @rudysuarez1
- [x] ~~Milestone 2: (4) clear all tasks from the todo list @ky135b~~
- [x] ~~Milestone 2: (5) creating a new task on the todo list @ky135b~~
- [ ] Milestone 3: (6) crossing off a task on the todo list @rudysuarez1
- [ ] Milestone 3: (7) sending chat messages @rudysuarez1
- [x] ~~Milestone 2: (8) registering for the email website @n-k-leung~~
- [ ] Milestone 3: (9) advanced search using regex @ky135b
- [x] ~~Milestone 2: (10) delete email account from email website @ky135b~~
- [ ] Milestone 3: (11) creating an email group @ky135b
- [ ] Milestone 3: (12) adding attachments in an email @n-k-leung
- [x] ~~Milestone 2: (13) login @n-k-leung~~
- [x] ~~Milestone 2: (14) logout @ky135b~~

## Non-functional Requirements

1. email website is able to work on chromium browsers and firefox browsers
2. email website has multilingual support (e.g. English, Spanish)

## Use Cases

### 1. Registering for the email website
- **Author: @n-k-leung**
- **Pre-condition:**
User has a valid email address and password
- **Trigger:**
User selects the “register” button
- **Primary Sequence:**

  1. User is prompted to a new page to enter their desired email address and password to register
  2. User enters valid email address and valid password in their respective boxes and selects the “register” button again to validate the registration process
  3. User is prompted to a new page, which is their email page

- **Primary Postconditions:**
User has now a registered account for email website and receives a confirmation email sent by system that they have 
successfully registered.
- **Alternate Sequence:**
  1. User is prompted to a new page to enter their desired email address and password to register
  2. User inputs a valid email address but an invalid password as it does not fit the rules of what a valid password should have
  3. User re-enters a new password that follows the rules
  4. User selects the “register” button again to validate the registration process
  5. User is prompted to a new page, which is their email page

### 2. Sending an email
- **Author: @n-k-leung**
- **Pre-condition:**
User is logged in and has valid recipient email address
- **Trigger:**
User pushes “compose” button
- **Primary Sequence:**
  1. User enters the name and content of their email draft
  2. User enters recipient's email address
  3. System communicates that their email draft is valid
  4. User presses send button
  5. System communicates that email is sent
  6. User logs out

- **Primary Postconditions:**
User gets pop up notification that the email has been sent. User sees that email is marked as sent by the system on the email home page.

- **Alternate Sequence:**
  1. User enters the name and content of their email draft
  2. User enters an invalid recipient email address
  3. System communicates that email is invalid
  4. User re-enters a valid recipient email address
  5. User presses send button
  6. System communicates that email is sent
  7. User logs out

### 3. Flagging an email as urgent
- **Author: @n-k-leung**
- **Pre-condition:**
User is logged in
- **Trigger:**
User selects the "Mark Emails as Urgent" button
- **Primary Sequence:**

  1. User selects the email they want to flag as urgent
  2. User selects the urgent symbol to flag it as urgent
  3. User logs out

- **Primary Postconditions:**
User gets a pop up notification that the email has been marked as urgent. Email is marked urgent by system by coloring the urgent symbol next to the email for visual confirmation.
- **Alternate Sequence:**
  1. User selects the email they want to flag as urgent
  2. User selects the urgent symbol to flag it was urgent, but the email has already been marked as urgent
  3. User gets notification that they have unflagged the email as not urgent
  4. User reflags the email as urgent by selecting the urgent symbol
  5. User logs out

### 4. Creating an email group
- **Author: @ky135b**
- **Pre-condition:** 
User is logged in and on the home page.
- **Trigger:** 
User clicks the "Create Email Group" button.
- **Primary Sequence:**

  1. User is served a new page to facilitate the creation of the email group.
  2. User enters a name for the email group in a textbox provided on the page.
  3. User enters up to 5 valid email addresses in textboxes provided on the page.
  4. User selects the "Create" button.
  5. User is served a new page which displays the newly created group (name & members), and a button to add more members (if applicable).

- **Primary Postconditions:** 
User has now created an email group, stored by the website in a database, which can be selected as a target for an email, delivering the email to all members in the group.

- **Alternate Sequence:** 
  1. User is served a new page to facilitate the creation of the email group.
  2. User enters a name for the email group in a textbox provided on the page.
  3. User enters up to 5 valid email addresses in textboxes provided on the page.
  4. User selects the "Create" button.
  5. The user entered an invalid name for the email group, or one or multiple invalid email addresses, and an error popup is shown detailing this error.
  6. The user is prompted to fix their error.

### 5. Adding attachments in an email
- **Author: @ky135b**
- **Pre-condition:** 
User is logged in and composing an email.
- **Trigger:** 
User selects the attachment button.
- **Primary Sequence:**

  1. User is prompted to attach a file through a popup.
  2. User selects the file to attach.
  3. The popup goes away, leaving the user to continue composing their email.
  4. User logs out.
  
- **Primary Postconditions:** 
User has now added an attachment to their email, which will be sent with it to their recipient (and stored on the server). The user will also see an X next to their attachment, allowing them to delete the attachment.
- **Alternate Sequence:** 
  
  1. User is prompted to attach a file through a popup.
  2. User decides not to attach a file and cancels the popup.
  3. The popup goes away, leaving the user to continue composing their email.
  4. User may select the attachment button again if they decide to attach a file, starting back at step 1. in the sequence.
  
### 6. Advanced search using regex
- **Author: @ky135b**
- **Pre-condition:** 
The user is logged in and on the home page.
- **Trigger:** 
User selects the "Advanced Search" button.
- **Primary Sequence:**

  1. User is served a new page where they can enter their search terms and a "Search" button.
  2. User enters their search terms.
  3. User selects the "Search" button.
  4. User is served a list of their emails matching their search terms.
  5. User logs out.
  
- **Primary Postconditions:** 
User is served a list of their emails matching their seach terms, and the search is saved to be accessible on a "Previous Searches" page.
- **Alternate Sequence:** 

  1. User is served a new page where they can enter their search terms and a "Search" button.
  2. User enters no search terms.
  3. User selects the "Search" button.
  4. User is served an empty list of emails and page prompts user to enter search terms until.
  5. User logs out.

### 7. Deleting an email
- **Author: @rudysuarez1**
- **Pre-condition:** 
User is logged in and an email is selected
- **Trigger:** 
User presses the delete button
- **Primary Sequence:**
  
  1. User is prompted to confirm the delete action
  2. User confirms deletion through pressing a confirmation button and the server deletes the email 
  3. User gets a pop up notification confirming that the email was deleted
  4. User is brought back to the home page
  5. User logs out
  

- **Primary Postconditions:** 
User sees that the email has been deleted, gets pop up notification confirming that email is deleted, and is brought back to email list home page.
- **Alternate Sequence:** 
  
  1. User is prompted to confirm delete action
  2. User does not confirm deletion by not selecting confirmation button and clicks out of the confirmation screen
  3. User gets pop up notification that email is not deleted because it was not a confirmed action
  4. User is clicks the delete button again and selects the confirmation button 
  5. User gets pop up notification that email is deleted
  6. User is brought back to email list home page
  7. User logs out


### 8. Clear all tasks from the todo list
- **Author: @ky135b**
- **Pre-condition:** 
User is logged into email and on the todo list page
- **Trigger:** 
User presses the "Clear" button on the todo list page
- **Primary Sequence:**
  
  1. User is prompted to confirm they want to clear all tasks from the todo page
  2. User selects "Yes"
  3. The todo page is cleared of all tasks
  4. User logs out

- **Primary Postconditions:** 
User gets pop up notification that the todo list was successfully cleared
- **Alternate Sequence:** 
  1. User is prompted to confirm they want to clear all tasks from the todo page
  2. User selects "No"
  3. User is returned to unchanged todo list page
  4. User is able to trigger this use case again if they want to clear their todo list in the future
