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
12. assigning members to an email group
13. add functionality for email & chat attachments
14. advanced search using regex
15. cc/bcc function for emails

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
login and recipient email address
- **Trigger:**
user pushes “compose” button
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

3. Flagging an email as urgente
- **Pre-condition:**
user is logged in and email is selectedd
- **Trigger:**
user selects the “urgent” flag
- **Primary Sequence:**

  1. User is prompted to loginn
  2. User selects the email they want to flag as urgent
  3. User selects the urgent symbol to flag it as urgent
  4. User logs out

- **Primary Postconditions:**
User gets a pop up notification that the email has been marked as urgentd
- **Alternate Sequence:**
  1. User is prompted to login
  2. User selects the email they want to flag as urgent
  3. User selects the urgent symbol to flag it was urgent, but the email has already been marked as urgent
  4. User gets notification that they have unflagged the email as not urgent
  5. User reflags the email as urgent by selecting the urgent symbol
  6. User logs out

1. Use Case Name (Should match functional requirement name)
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

2. Use Case Name (Should match functional requirement name)
   ...

3. Use Case Name (Should match functional requirement name)
   ...

4. Use Case Name (Should match functional requirement name)
   ...

5. Use Case Name (Should match functional requirement name)
   ...

6. Use Case Name (Should match functional requirement name)
   ...

7. Use Case Name (Should match functional requirement name)
   ...

8. Use Case Name (Should match functional requirement name)
   ...
