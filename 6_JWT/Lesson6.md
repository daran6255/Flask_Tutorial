## JWT in Flask

### What is JWT?
JWT (JSON Web Token) is a compact, URL-safe way to securely transmit information between parties as a JSON object. It is commonly used for authentication and authorization in web apps.

- It's like a token you give to users after they log in.
- Users include this token in future requests to access protected routes.
- The server checks the token to verify the user's identity.

### How JWT Works (Simple Steps)
1. User logs in with a username/password.
2. If valid, the server sends a JWT token.
3. The client stores the token (usually in localStorage or cookies).
4. For every protected route, the token is sent in headers.
5. The server verifies the token before giving access.

### Common Use Cases
- Login & protected routes
- API security
- Single Sign-On (SSO)
- Role-based access control

### Installation
Install the JWT extension: pip install Flask-JWT-Extended
