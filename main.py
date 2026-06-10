from fastapi import FastAPI, HTTPException
from schemas import Student

app = FastAPI(
    title="Student Management API",
    version="1.0"
)

# Student Records (List Storage)
students = [
    {
        "id": 1,
        "name": "Suresh",
        "age": 25,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Ramesh",
        "age": 22,
        "course": "Testing"
    },
    {
        "id": 3,
        "name": "Ravi",
        "age": 26,
        "course": "Dev"
    }
]

# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}

# Add Student API
@app.post("/students")
def add_student(student: Student):

    for s in students:
        if s["id"] == student.id:
            raise HTTPException(
                status_code=400,
                detail="Duplicate student ID"
            )

    students.append(student.dict())

    return {
        "message": "Student added successfully",
        "student": student
    }

# Get All Students API
@app.get("/students")
def get_all_students():
    return students

# Get Student By ID API
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# Update Student API
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student["id"] == student_id:
            students[index] = updated_student.dict()

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# Delete Student API
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )