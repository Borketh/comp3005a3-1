from sqlobject import SQLObject, IntCol, StringCol, DateTimeCol


class Students(SQLObject):
    class sqlmeta:
        table = "students"
        idName = "student_id"

    # student_id = IntCol()
    first_name = StringCol()
    last_name = StringCol()
    email = StringCol()
    enrollment_date = DateTimeCol()

    def as_dict(self):
        # this is purely for display
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            enrollment_date=self.enrollment_date,
        )
