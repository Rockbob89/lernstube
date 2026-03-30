# Task 6: Auth

## Objective
Secure your API with OAuth2 password flow and JWT tokens. Understand token creation, verification, and protecting endpoints with dependency-based auth.

## What to Learn
- `OAuth2PasswordBearer` — the security scheme; declares that the token comes from the `Authorization: Bearer` header
  ```python
  from fastapi.security import OAuth2PasswordBearer
  oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
  ```
- `OAuth2PasswordRequestForm` — login endpoint; parses `username` + `password` from form-encoded body
  ```python
  from fastapi.security import OAuth2PasswordRequestForm
  @app.post("/token")
  def login(form: OAuth2PasswordRequestForm = Depends()): ...
  ```
- JWT tokens — `python-jose` for creation and verification
  ```python
  from jose import jwt
  token = jwt.encode({"sub": "alice", "exp": ...}, SECRET, algorithm="HS256")
  payload = jwt.decode(token, SECRET, algorithms=["HS256"])
  ```
- `bcrypt` / `passlib` — password hashing
  ```python
  from passlib.context import CryptContext
  pwd_context = CryptContext(schemes=["bcrypt"])
  hashed = pwd_context.hash("secret")
  pwd_context.verify("secret", hashed)  # True
  ```
- Protecting endpoints — `get_current_user` dependency; injects the decoded user into any endpoint
- Scopes (optional) — role-based access control

## Exercises

### 1. Password Hashing
Create `hash_password()` and `verify_password()` functions using `passlib[bcrypt]`. Hash a password, verify it matches, verify a wrong password fails.

```python
hashed = hash_password("secret")
assert verify_password("secret", hashed) == True
assert verify_password("wrong", hashed) == False
```

### 2. JWT Token
Create `create_access_token(data: dict, expires_delta: timedelta)` that returns a JWT. Create `decode_access_token(token: str)` that returns the payload or raises.

```python
token = create_access_token({"sub": "alice"}, timedelta(minutes=30))
payload = decode_access_token(token)
# payload["sub"] == "alice"
```

### 3. Login Endpoint
Add `POST /token` that accepts `OAuth2PasswordRequestForm`, validates credentials against a fake user DB, and returns `{"access_token": "...", "token_type": "bearer"}`.

```python
# POST /token  username=alice&password=secret
# -> {"access_token": "eyJ...", "token_type": "bearer"}

# POST /token  username=alice&password=wrong
# -> 401 Unauthorized
```

### 4. Protected Endpoints
Create a `get_current_user` dependency that extracts the token, decodes it, and returns the user. Use it to protect `GET /me` and `GET /admin` (admin requires role check).

```python
# GET /me  (Authorization: Bearer <token>)
# -> {"username": "alice", "role": "admin"}

# GET /admin  (non-admin token)
# -> 403 Forbidden
```
