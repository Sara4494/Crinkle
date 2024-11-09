# API Documentation

## 1. **Registration (Register)**

- **Endpoint**: `http://127.0.0.1:8000/users/register/`
- **Method**: `POST`
- **Content**:
  - **Required Fields**:
    - `first_name`: First Name (String, Required)
    - `email`: Email (String, Required)
    - `phone_number`: Phone Number (String, Required)
    - `password`: Password (String, Required)
- **Expected Response**:
  - **On Success**:
    - **Status**: `200 Created`
    - **Content**:
      ```json
      {
          "message": "User created successfully!",
          "user": {
              "first_name": "User Name",
              "email": "user@example.com",
              "phone_number": "0123456789"
          }
      }
      ```
  - **On Error**:
    - **Status**: `400 Bad Request`
    - **Content**:
      ```json
      {
          "error_messages": {
              "email": ["A user with this email already exists."],
              "phone_number": ["A user with this phone number already exists"] ,
              "password": ["Password must be at least 8 characters long."]
          }
      }
      ```

  - **Possible Errors**:
    - `email`: 
      - **Message**: `"A user with this email already exists."`
      - **Scenario**: When a user tries to register with an already existing email.
    - `phone_number`:
      - **Message**: `"A user with this phone number already exists."`
      - **Scenario**: When a user tries to register with an already existing phone number.
    - `password`:
      - **Message**: `"Password must be at least 8 characters long."`
      - **Scenario**: When the password provided is less than 8 characters.

---

## 2. **Login (Login)**

- **Endpoint**: `http://127.0.0.1:8000/users/login/`
- **Method**: `POST`
- **Content**:
  - **Required Fields**:
    - `email`: Email (String, Optional)
    - `phone_number`: Phone Number (String, Optional)
    - `password`: Password (String, Required)
- **Expected Response**:
  - **On Success**:
    - **Status**: `200 OK`
    - **Content**:
      ```json
      {
          "message": "Login successful.",
          "token": "your_token_here"
      }
      ```
  - **On Error**:
    - **Status**: `400 Bad Request`
    - **Content**:
      ```json
      {
          "errors": {
              "non_field_errors": ["Invalid login credentials."]
          }
      }
      ```

  - **Possible Errors**:
    - `non_field_errors`:
      - **Message**: `"Invalid login credentials."`
      - **Scenario**: When either the email/phone number or the password is incorrect.
    - `email` or `phone_number`:
      - **Message**: `"Either email or phone number is required."`
      - **Scenario**: When neither email nor phone number is provided during login.
    - `password`:
      - **Message**: `"Password is required."`
      - **Scenario**: When password is not provided.

---

## 3. **Messages in the Model**

### 3.1 **CustomUser Model**
- **Messages**:
  - **Email**: 
    - `"Email is required."` 
    - **Scenario**: If email is not provided during registration.
  - **Phone Number**: 
    - `"Phone number is required."`
    - **Scenario**: If phone number is not provided during registration.
  - **Password**: 
    - `"Password must be at least 8 characters long."`
    - **Scenario**: If password is shorter than 8 characters during registration.

---

## 4. **Common Errors**

- **Scenario**: Missing or incorrect field inputs
  - **Message**: `"Field X is required."`
  - **Scenario**: When any required field like email, phone number, or password is missing.
- **Scenario**: Invalid email or phone number format
  - **Message**: `"Invalid email format."` or `"Invalid phone number format."`
  - **Scenario**: When an invalid email or phone number is provided.
  
---
