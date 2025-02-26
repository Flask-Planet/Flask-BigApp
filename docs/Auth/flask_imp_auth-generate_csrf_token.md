# generate_csrf_token

```python
from flask_imp.auth import generate_csrf_token
```

```python
generate_csrf_token() -> str
```

---

Generates a SHA1 using the current date and time.

For use in Cross-Site Request Forgery.

Also used by the [flask_imp.security / csrf_protect](../Security/flask_imp_security-include_csrf.md) decorator.

*Example:*

```python
generate_csrf_token()  # >>> 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0'
```

