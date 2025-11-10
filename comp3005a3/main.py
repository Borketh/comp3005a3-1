import time

import sqlobject as sql
from functions import *

if __name__ == "__main__":
    user = "normaluser"
    password = "dbrowstastelikecoffeecrisp"
    host = "localhost"
    port = "5432"
    dbname = "normaluser"
    uri = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    attempt = 1
    while attempt < 6:
        try:
            connection = sql.connectionForURI(uri)
            sql.sqlhub.processConnection = connection
            break
        except sql.dberrors.OperationalError:
            print(f"Could not connect to the DB on attempt {attempt}")
            attempt += 1
            time.sleep(5)
    else:  # this happens if the loop is not broken by a successful connection
        raise ConnectionError("Could not connect to the DB")

    input("Demonstration of getAllStudents")
    print(
        *get_all_students(), sep="\n"
    )  # we print it weird this way to print each list item as a new line

    input("Demonstration of addStudent")
    jane_id = add_student("Jane", "Doe", "janedoe@example.com", "2025-11-09")
    print(*get_all_students(), sep="\n")

    input("Demonstration of updateStudentEmail")
    update_student_email(jane_id, "jane.doe@example.com")
    print(*get_all_students(), sep="\n")

    input("Demonstration of deleteStudent")
    delete_student(jane_id)
    print(*get_all_students(), sep="\n")

    input("End of demonstration")
