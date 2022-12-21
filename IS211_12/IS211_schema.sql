DROP TABLE IF EXISTS students;
CREATE TABLE students(student_id INTEGER PRIMARY KEY, student_firstname TEXT, student_lastname TEXT);
INSERT INTO students(student_id, student_firstname, student_lastname)
VALUES (1, "John", "Smith");


DROP TABLE IF EXISTS quizzes;
CREATE TABLE quizzes(quiz_id INTEGER PRIMARY KEY, subject TEXT, num_questions INTEGER, quiz_date TEXT);
INSERT INTO quizzes(quiz_id, subject, num_questions, quiz_date)
VALUES (1, "Python Basics", 5, "February, 5th, 2015");

DROP TABLE IF EXISTS studentsresults;
CREATE TABLE studentsresults(result_id INTEGER, score INTEGER, FOREIGN KEY student_id REFERENCES students(student_id), FOREIGN KEY quiz_id REFERENCES quizzes(quiz_id));
INSERT INTO studentsresults(result_id, score, student_id, quiz_id)
VALUES (1, 85, 1, 1,);

