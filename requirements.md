## Functional Requirements

1. sending an email
2. deleting an email
3. flagging an email as urgent
4. creating a new todo list
5. creating a new task on the todo list
6. crossing off a task on the todo list
7. sending chat messages
8. registering for the email website
9. search for an email
10. forwarding an email
11. creating an email group
12. adding attachments in an email
13. search for a chat messages in chat channel

## Non-functional Requirements

1. email website is able to work on chromium browsers and firefox
2. email website response to user input with either a success or error confirmation within 5 seconds
3. email website implements multilingual support
4. each page of the email website must load within 5 seconds

## Use Cases

1. Registering for website
- **Pre-condition:**
user has a valid email address and a password
- **Trigger:**
user selects “register” button
- **Primary Sequence:**

  1. User selects the “register” button
  2. User is prompted to a new page to enter email address and password to register
  3. User enters valid email address and valid password in their respective boxes
  4. User selects the “register” button again to validate the registration proces
  5. User is prompted to a new page, which is their email page

- **Primary Postconditions:**
User has now a registered account for email website and receives a confirmation email that they have 
successfully registered
- **Alternate Sequence:**
  1. User selects the “register” button
  2. User is prompted to a new page to enter email address and password to register
  3. User inputs a valid email address but an invalid password as it does not fit the rules of what a valid password should have
  4. User re-enters a new password that follows the rules
  5. User selects the “register” button again to validate the registration process
  6. User is prompted to a new page, which is their email page

2. Sending an email
- **Pre-condition:**
Login and recipient email address
- **Trigger:**
User pushes “compose” button
- **Primary Sequence:**
  1. User is prompted to login 
  2. User clicks compose button
  3. User enters name of draft and content of draft
  4. User enters recipient email
  5. System communicates that email is valid
  6. User presses send button
  7. System communicates that email is sent
  8. User logs out

- **Primary Postconditions:**
User gets pop up notification that the email has been sent

- **Alternate Sequence:**
  1. User is prompted to login 
  2. User clicks compose button
  3. User enters name of draft and content of draft
  4. User enters an invalid recipient email address
  5. System communicates that email is invalid
  6. User re-enters a valid recipient email address
  7. User presses send button
  8. System communicates that email is sent
  9. User logs out

3. Flagging an email as urgent
- **Pre-condition:**
User is logged in and email is selected
- **Trigger:**
User selects the “urgent” flag
- **Primary Sequence:**

  1. User is prompted to loginn
  2. User selects the email they want to flag as urgent
  3. User selects the urgent symbol to flag it as urgent
  4. User logs out

- **Primary Postconditions:**
User gets a pop up notification that the email has been marked as urgent
- **Alternate Sequence:**
  1. User is prompted to login
  2. User selects the email they want to flag as urgent
  3. User selects the urgent symbol to flag it was urgent, but the email has already been marked as urgent
  4. User gets notification that they have unflagged the email as not urgent
  5. User reflags the email as urgent by selecting the urgent symbol
  6. User logs out

4. Creating an email group
- **Pre-condition:** 
User is logged in and on the home page.
- **Trigger:** 
User clicks the "Create Email Group" button.
- **Primary Sequence:**
 
  1. User selects the "Create Email Group" button.
  2. User is served a new page to facilitates the creation of the email group.
  3. User enters a name for the email group in a textbox provided on the page.
  4. User enters up to 5 valid email addresses in textboxes provided on the page.
  5. User selects the "Create" button.
  6. User is served a new page which displays the newly created group (name & members), and a button to add more members (if applicable).

- **Primary Postconditions:** 
User has now created an email group, stored by the website in a database, which can be selected as a target for an email, delivering the email to all members in the group.

- **Alternate Sequence:** 
  1. User selects the "Create Email Group" button.
  2. User is served a new page to facilitates the creation of the email group.
  3. User enters a name for the email group in a textbox provided on the page.
  4. User enters up to 5 valid email addresses in textboxes provided on the page.
  5. User selects the "Create" button.
  6. User is served a new page which displays the newly created group (name & members), and a button to add more members (if applicable).
  7. The user entered an invalid name for the email group, or any of the email addresses 
  8. An error popup is shown detailing the specific error
  9. The user is prompted to fix their error .


5. Assigning members to an email group
- **Pre-condition:** 
User is logged in and on the page for the email group they want to assign members to.
- **Trigger:** 
User selects the "Add Member" button.
- **Primary Sequence:**
  
  1. User selects the "Add Member" button.
  2. User is served with a new page to facilitate the addition of new members, with up to 5 textboxes depending on the amount of members already in the group.
  3. User enters new email addresses in the textboxes provided on the page.
  4. User selects the "Add Member(s)" button.
  5. User is served a new page which displays the modified group (name & members), and a button to add more members (if applicable).

- **Primary Postconditions:** 
User has now modified the group to add members to their selected email group, up to a maximum of 5.
- **Alternate Sequence:** 
  
  5. If the user has entered 0 email addresses, a popup is shown saying no emails were added to the group, and the user is returned the the page for the relevant email group.
  
6. Advanced search using regex
- **Pre-condition:** 
The user is logged in and on the home page.
- **Trigger:** 
User selects the "Advanced Search" button.
- **Primary Sequence:**
  
  1. User selects the "Advanced Search" button.
  2. User is served a new page where they can enter their search terms and a "Search" button.
  3. User enters their search terms.
  4. User selects the "Search" button.
  5. User is served a list of their emails matching their search terms.

- **Primary Postconditions:** 
User is served a list of their emails matching their seach terms, and the search is saved to be accessible on a "Previous Searches" page.
- **Alternate Sequence:** 
  1. User selects the "Advanced Search" button.
  2. User is served a new page where they can enter their search terms and a "Search" button.
  3. User enters no search terms.
  4. User selects the "Search" button.
  5. User is served an empty list of emails and prompts user to enter search terms until completed.

7. Use Case Name (Should match functional requirement name)
- **Pre-condition:** 

- **Trigger:** 

- **Primary Sequence:**
  
  1. ...
  2. ...
  3. ...
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. ...

- **Primary Postconditions:** 

- **Alternate Sequence:** 
  
  1. ...
  2. ...
  3. ...

- **Alternate Sequence <optional>:** 
  
  1. ...
  2. ...
  3. ...


8. Use Case Name (Should match functional requirement name)
- **Pre-condition:** 

- **Trigger:** 

- **Primary Sequence:**
  
  1. ...
  2. ...
  3. ...
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. ...

- **Primary Postconditions:** 

- **Alternate Sequence:** 
  
  1. ...
  2. ...
  3. ...

- **Alternate Sequence <optional>:** 
  
  1. ...
  2. ...
  3. ...
