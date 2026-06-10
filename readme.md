# Student Management API

A simple REST API built with FastAPI for managing student records.

## Features

- Create new student records
- Retrieve all students
- Retrieve specific student by ID
- Update student information
- Delete student records
- Input validation
- Error handling for not found and duplicate entries
- Auto-generated student IDs

## Setup Instructions

pip install fastapi

pip install uvicorn

python -m uvicorn main:app --reload

Swagger:

http://127.0.0.1:8000/docs