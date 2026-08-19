from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db, Base, engine 
from models import Student
from schemas import StudentCreate, StudentOut

app = FastAPI(title="Student Management API")
Base.metadata.create_all(bind=engine) 

@app.get("/")
def home():
    return {"message": "Student API is running"}


@app.post("/students", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        age=student.age,
        city=student.city
    )

    db.add(new_student)
    db.commit() 
    db.refresh(new_student)

    return new_student


@app.get("/students", response_model=list[StudentOut])
def get_students(db: Session = Depends(get_db)):
    students= db.query(Student).all()
    return students 


@app.get("/students/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student 
@app.put("/students/{student_id}", response_model=StudentOut)
def update_student(student_id: int, student: StudentCreate, db:Session = Depends(get_db)):
    existing_student = db.query(Student).filter(Student.id == student_id).first()
    
    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    existing_student.name = student.name
    existing_student.age = student.age
    existing_student.city = student.city

    db.commit()
    db.refresh(existing_student)

    return existing_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id==student_id).first()
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student) 
    db.commit() 
    
    return {"message": "Student deleted Successully"} 