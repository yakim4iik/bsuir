INSERT INTO organization(name, code, phone, email, address)  
values 
        ('epam', '1', '+375292063019', 'epam@mail.com','minsk'),
        ('coursePy', '2', '+375293217852', 'pycourse@gmail.com','grodno');

INSERT INTO application(name, address, phone, email, ORganization_id, employees)  
values 
        ('itschool', 'minsk', '+375291122312', 'itschool@mail.com', 1, 5),
        ('softlearn', 'grodno', '+375332415841', 'softlearn@gmail.com', 2, 4);

INSERT INTO type(name)  
values 
        ('programming'),
        ('management'),
        ('foreign language');

INSERT INTO course(code, name, type_id, days, students, ORganization_id)  
values 
        ('01423', 'pythonLearn', 1, 30, 30, 2),
        ('e23r2', 'English', 3, 30, 10, 1),
        ('2314f', 'JavaScript', 1, 30, 15, 1),
        ('24213', 'C++', 1, 30, 10, 2);

INSERT INTO job_title(name)  
values 
        ('engineer'),
        ('programmer'),
        ('teacher'),
        ('accountant');

INSERT INTO employee(first_name, surname, middle_name, job_title_id)  
values 
        ('ivan', 'ivanov', 'ivanovich', 1),
        ('andrey', 'andreev', 'andreevich', 3),
        ('ilya', 'ilyanov', 'ilyich', 2),
        ('sergey', 'sergeev', 'sergeevich', 4);

INSERT INTO application_course(course_id, employee_id, date)  
values 
        (3, 2, '2023-11-18'),
        (2, 1, '2024-01-01');

INSERT INTO category(name)  
values 
        ('first'),
        ('second'),
        ('highest');

INSERT INTO course_price("number", date, price, course_id)  
values 
        (123, '2023-11-10', 100, 1),
        (2414, '2023-11-12', 200, 2),
        (213, '2023-11-13', 300, 3);

INSERT INTO education(name)  
values 
        ('primary'),
        ('secondary'),
        ('higher');


INSERT INTO sex(name)  
values 
        ('man'),
        ('woman');

INSERT INTO teacher(first_name, surname, middle_name, sex_id, education_id, birthday, categORy_id)  
values 
        ('Igor', 'Petrosyan', 'Sergeevich', 1, 3, '1978-12-22', 3),
        ('Dima', 'Verenich', 'Igorevich', 1, 2, '1991-09-01', 2),
        ('Elena', 'Pochinchik', 'Andreevna', 2, 2, '1999-04-04', 1);



INSERT INTO teacher_document(teacher_id, start, "end", course_id)  
values 
        (1, '2023-11-15', '2023-12-01', 1),
        (2, '2023-11-01', '2023-12-01', 2);
