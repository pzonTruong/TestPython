CREATE TABLE students(
    student_id NUMERIC,
    name VARCHAR(255),
    age NUMERIC,
    email VARCHAR(255),
    average_score NUMERIC
)

INSERT INTO students VALUES (1,"John Doe",20,"john.doe@example.com",8.5);
INSERT INTO students VALUES (2,"Jane Smith",22,"jane.smith@example.com",7.8);
INSERT INTO students VALUES (3,"Emily Johnson",19,"emily.johnson@example.com",9.1);
INSERT INTO students VALUES (4,"Micheal Brown",21,"michael.brown@example.com",8.2);
INSERT INTO students VALUES (5,"Jessica Davis",23,"jessica.davis@example.com",6.9);
INSERT INTO students VALUES (6,"David Wilson",20,"david.wilson@example.com",7.3);
INSERT INTO students VALUES (7,"Sarah Lee",22,"sarah.lee@example.com",8.8);
INSERT INTO students VALUES (8,"Chris Kim",19,"chris.kim@example.com",9);
INSERT INTO students VALUES (9,"Anna Clark",21,"anna.clark@example.com",7.5);
INSERT INTO students VALUES (10,"Daniel Martinez",23,"daniel.martinez@example.com",6.5);
INSERT INTO students VALUES (11,"Sophia Lopez",20,"sophia.lopez@example.com",8.1);
INSERT INTO students VALUES (12,"James White",22,"james.white@example.com",7.9);
INSERT INTO students VALUES (13,"Olivia Harris",19,"olivia.harris@example.com",9.3);


SELECT * FROM students WHERE students.age > 18;
SELECT * FROM students WHERE students.name LIKE "%Smith%" AND students.average_score > 7;
SELECT COUNT(*) FROM students WHERE students.average_score > 8;