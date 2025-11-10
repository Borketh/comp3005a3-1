from datetime import datetime

from db_obj import Students


def get_all_students():
    return [row.as_dict() for row in Students.selectBy().lazyIter()]


def add_student(first_name: str, last_name: str, email: str, enrollment_date) -> int:
    # ID should be automatically generated.
    student = Students(
        first_name=first_name,
        last_name=last_name,
        email=email,
        enrollment_date=datetime.fromisoformat(  # necessary due to nature of DateTimeCol
            enrollment_date
        ),
    )
    return (
        student.id  # we return this so we know what the ID of the new student is for later things
    )


def update_student_email(student_id: int, new_email: str):
    query = Students.selectBy(id=student_id).getOne(None)

    if query is not None:
        query.email = new_email
    else:
        print(f"Student with id {student_id} not found")


def delete_student(student_id: int):
    Students.deleteBy(id=student_id)
