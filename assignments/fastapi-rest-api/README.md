# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

In this assignment, you will build a simple REST API using FastAPI. You will learn how to create endpoints, validate request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Build the main API routes for managing a small collection of books. Your API should support creating, reading, updating, and deleting books.

#### Requirements
Completed program should:

- Define a FastAPI app in `starter-code.py`
- Create the following endpoints: `GET /books`, `GET /books/{book_id}`, `POST /books`, `PUT /books/{book_id}`, and `DELETE /books/{book_id}`
- Return JSON responses with clear success or error messages


### 🛠️	Add Data Validation and Error Handling

#### Description
Use Pydantic models to validate incoming data and improve reliability of your API. Add proper error handling when a requested book does not exist.

#### Requirements
Completed program should:

- Create a Pydantic model with fields for `title`, `author`, and `year`
- Reject invalid requests automatically through FastAPI validation
- Return HTTP 404 errors when a book is not found
