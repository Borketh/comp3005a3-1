CREATE TABLE students (
    student_id serial primary key not null,
    first_name text not null,
    last_name text not null,
    email text not null unique,
    enrollment_date Date
);

ALTER TABLE students OWNER TO normaluser;

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');