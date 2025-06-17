#  Superheroes Flask API

A RESTful API built with Flask that manages **heroes**, their **powers**, and the **strengths** of those powers. It's a comic-book database in the making — complete with validations, relationships, and proper error handling.

---

##  Features

- Create and manage superheroes and their powers
- Assign powers to heroes with different strength levels
- Update power descriptions
- Handles validations and errors like a boss
- Uses Flask, SQLAlchemy, and Marshmallow

---

##  Setup Instructions

### 1. Clone the repo
```bash
git clone <your-repo-url>
cd <repo-folder>
````

### 2. Install dependencies

```bash
pipenv install
pipenv shell
```

### 3. Run the migrations

```bash
flask db init
flask db migrate -m "Initial tables"
flask db upgrade
```

### 4. Seed the database

```bash
python seed.py
```

### 5. Start the server

```bash
flask run
```

Server will run on:
**`http://localhost:5555`**

---

##  API Endpoints

###  `/heroes` (GET)

Returns a list of all heroes.

###  `/heroes/<id>` (GET)

Returns a single hero and their powers.
If the hero is not found:

```json
{ "error": "Hero not found" }
```

---

###  `/powers` (GET)

Returns a list of all powers.

###  `/powers/<id>` (GET)

Returns a single power.
If not found:

```json
{ "error": "Power not found" }
```

### ✍️ `/powers/<id>` (PATCH)

Update a power's description.

Request body:

```json
{ "description": "Your new valid description here" }
```

Validation error:

```json
{ "errors": ["validation errors"] }
```

---

###  `/hero_powers` (POST)

Create a new HeroPower.

Request body:

```json
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 2
}
```

Validation error:

```json
{ "errors": ["validation errors"] }
```

---

##  Models

### `Hero`

* `id`: Integer
* `name`: String
* `super_name`: String

### `Power`

* `id`: Integer
* `name`: String
* `description`: String (minimum 20 characters)

### `HeroPower`

* `id`: Integer
* `strength`: String — must be "Strong", "Average", or "Weak"
* `hero_id`: Foreign Key
* `power_id`: Foreign Key

---

## ✅ Validations

| Model     | Field       | Validation Rule                             |
| --------- | ----------- | ------------------------------------------- |
| Power     | description | Must be present and ≥ 20 characters         |
| HeroPower | strength    | Must be one of: "Strong", "Average", "Weak" |

---

## 👤 Author

Built  by **Brian Munene Mwirigi** 
A young dev
---
## 📝 License

This project is open for learning, testing, and leveling up.
No strict license — just don’t be evil
---
##  Notes

* Make sure your Postman collection matches the endpoints.
* Your `.flaskenv` should have:

```
FLASK_APP=app.py
FLASK_ENV=development
```
* Use `flask run` instead of `python app.py` if you're using `.flaskenv`.
---

```
---