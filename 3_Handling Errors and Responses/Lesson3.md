
## What are HTTP Status Codes?

HTTP status codes are issued by a server in response to a client’s request. They are grouped into different categories:

---

### 1xx - Informational
- Rarely used in APIs
- Example: `100 Continue`

---

### 2xx - Success

| Code | Meaning               | Explanation                            |
|------|------------------------|----------------------------------------|
| 200  | OK                     | The request was successful             |
| 201  | Created                | Resource successfully created          |
| 204  | No Content             | Success, but no content to return      |

---

### 3xx - Redirection

| Code | Meaning               | Explanation                            |
|------|------------------------|----------------------------------------|
| 301  | Moved Permanently      | Resource moved to a new URL            |
| 302  | Found                  | Temporary redirect                     |
| 304  | Not Modified           | Cached version can be used             |

---

### 4xx - Client Errors

| Code | Meaning               | Explanation                            |
|------|------------------------|----------------------------------------|
| 400  | Bad Request            | Server cannot process the request      |
| 401  | Unauthorized           | Authentication required                |
| 403  | Forbidden              | No permission to access resource       |
| 404  | Not Found              | Resource not found                     |
| 405  | Method Not Allowed     | HTTP method not allowed                |

---

### 5xx - Server Errors

| Code | Meaning               | Explanation                            |
|------|------------------------|----------------------------------------|
| 500  | Internal Server Error  | Generic server error                   |
| 502  | Bad Gateway            | Invalid response from another server   |
| 503  | Service Unavailable    | Server temporarily unable to handle    |

---
## Error Handling and Try-Except in Flask
Error handling is used to manage unexpected situations in your code—like dividing by zero or missing data—without crashing the application.

### Why Use Error Handling?
1. To prevent your app from crashing on invalid input.
2. To give meaningful messages back to the user.
3. To handle known issues (like missing data, invalid types, etc.) gracefully.
---
## Using try-except Blocks
The try-except block allows you to “try” something that might cause an error and “catch” the error if it happens.
**Syntax**
try:
    # risky code here
except SomeError:
    # handle the error
