create database lab2
    with owner postgres;
create table students(
    student_id serial primary key,
    first_name varchar(50),
    last_name varchar(50),
    date_of_birth date,
    major varchar(50),
    city varchar(50),
    gpa decimal
);

ALTER TABLE students
ALTER COLUMN student_id TYPE smallint;
ALTER TABLE students
ALTER COLUMN student_id SET NOT NULL ;
ALTER TABLE students
RENAME COLUMN date_of_birth TO birth_date;
ALTER TABLE students
ADD email varchar(50);
ALTER TABLE students
DROP COLUMN major;
INSERT INTO students(first_name, last_name, birth_date, city, gpa) VALUES ('Name1', 'Last1', '2000-01-01', 'City1', 4.0);
INSERT INTO students(first_name, last_name, birth_date, city, gpa) VALUES ('Name2', 'Last2', '2000-01-01', 'City2', 4.0);
INSERT INTO students(first_name, last_name, birth_date, city, gpa) VALUES ('Name3', 'Last3', '2000-01-01', 'City3', 4.0);

SELECT * FROM students;
SELECT * FROM students WHERE student_id=2;
DROP TABLE students;
DROP DATABASE lab2;
