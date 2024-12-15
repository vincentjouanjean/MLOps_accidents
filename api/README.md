# Prediction API application

The Prediction API application allows to predict severity of accident by user input.

A history is store in dedicated mongo database and the consult is allowed only for admin.

![img.png](api_c4_lvl3.png)

# Build application

```bash
  docker compose build
```

# Run application in local

```bash
  docker compose up
```

# Create Admin user

```curl
curl -X POST --location "http://127.0.0.1:8000/admins" \
    -H "Content-Type: application/json"
```

# Tests

Run `creation_request.http` to test connexion, creation and token validation.
