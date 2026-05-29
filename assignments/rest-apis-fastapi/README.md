# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple RESTful API using the FastAPI framework. You'll practice defining routes, request/response models with Pydantic, handling HTTP methods, and running a development server.

## 📝 Tasks

### 🛠️ Project Setup

#### Description
Create a new Python project folder for the assignment, install dependencies, and prepare a minimal FastAPI app skeleton.

#### Requirements
Completed project should:

- Include a `starter-code.py` file with a runnable FastAPI app.
- Specify required packages in the instructions (`fastapi`, `uvicorn`).
- Provide clear run instructions.

### 🛠️ Endpoints and Models

#### Description
Design and implement API endpoints to manage a simple resource (e.g., `items`). Use Pydantic models for request validation and response schemas.

#### Requirements
Completed API should:

- Provide at least the following endpoints:
  - `GET /items` — list all items
  - `GET /items/{item_id}` — retrieve a single item
  - `POST /items` — create a new item
  - `PUT /items/{item_id}` — update an existing item
  - `DELETE /items/{item_id}` — remove an item
- Use Pydantic models for request bodies and responses.
- Return appropriate HTTP status codes for success and error cases.

### 🛠️ Validation and Error Handling

#### Description
Add input validation and sensible error responses when requests are invalid or resources are not found.

#### Requirements
Completed program should:

- Validate required fields and types using Pydantic.
- Return `404 Not Found` when an `item_id` does not exist.
- Return `400 Bad Request` for invalid input where appropriate.

### 🛠️ Documentation and Run Instructions

#### Description
Provide instructions so a student can run the API locally and inspect the interactive OpenAPI docs.

#### Requirements
README should include:

- Commands to install dependencies:

  ```bash
  python3 -m pip install --upgrade pip
  python3 -m pip install fastapi uvicorn
  ```

- Command to run the development server:

  ```bash
  uvicorn starter-code:app --reload
  ```

- Note: Open the interactive docs at `http://127.0.0.1:8000/docs` after running the server.

## ✅ Deliverables

- [ ] `starter-code.py` with a functioning FastAPI app
- [ ] Brief README (this file) with run instructions and API overview

## 💡 Extensions (Optional)

- Add simple in-memory persistence that survives multiple requests during runtime.
- Add query parameters to filter or paginate results.
- Add simple authentication (API key or OAuth) for protected endpoints.

---

**Starter guidance:** Put `starter-code.py` in the same folder and run `uvicorn starter-code:app --reload` to test the API and view docs at `/docs`.