--ЗАДАНИЕ 1--

/* 1. Получить полную информацию обо всех преподавателях. DONE */

SELECT *
FROM PREDICTOR

/* 2. Получить полную информацию обо всех студенческих группах на специальности ЭВМ. DONE */

SELECT *
FROM STUDENT_GROUP
WHERE specialty = 'ЭВМ'

/* 3. Получить личный номер преподавателя и номера аудиторий, в которых они преподают предмет с кодовым номером 18П. DONE */

SELECT personal_number, audience_number
FROM PREDICTOR_STUDENT_GROUP
WHERE subject_number = '18П'

/* 4. Получить  номера предметов и названия предметов, которые ведет преподаватель Костин. DONE */

SELECT DISTINCT b.subject_number, b.subject_name
FROM PREDICTOR_STUDENT_GROUP AS a
INNER JOIN SUBJECT AS b ON a.subject_number = b.subject_number
INNER JOIN PREDICTOR AS c ON a.personal_number = c.personal_number
WHERE c.surname = 'Костин'

/* 5. Получить номер группы, в которой ведутся предметы преподавателем Фроловым. DONE */

SELECT group_number
FROM PREDICTOR_STUDENT_GROUP AS a
INNER JOIN PREDICTOR AS b ON a.personal_number = b.personal_number
WHERE surname = 'Фролов'


/* 6. Получить информацию о предметах, которые ведутся на специальности АСОИ. DONE */

SELECT *
FROM SUBJECT
WHERE specialty = 'АСОИ'

/* 7. Получить информацию о преподавателях, которые ведут предметы на специальности АСОИ. DONE */

SELECT *
FROM PREDICTOR
WHERE specialty LIKE '%АСОИ%'

/* 8. Получить фамилии преподавателей, которые ведут предметы в 210 аудитории. DONE */

SELECT DISTINCT b.surname 
FROM PREDICTOR_STUDENT_GROUP AS a 
INNER JOIN PREDICTOR AS b ON a.personal_number = b.personal_number
WHERE audience_number = 210

/* 9. Получить  названия  предметов  и  названия  групп,  которые  ведут  занятия  в  аудиториях  с  100  по 200. DONE */

SELECT subject_name, group_name
FROM PREDICTOR_STUDENT_GROUP AS a 
INNER JOIN SUBJECT AS b ON a.subject_number = b.subject_number
INNER JOIN STUDENT_GROUP AS c ON  a.group_number = c.group_number
WHERE audience_number BETWEEN 100 AND 200

/* 10. Получить пары номеров групп с одной специальности. DONE */

SELECT a.group_number, b.group_number
FROM STUDENT_GROUP a
INNER JOIN STUDENT_GROUP b ON a.specialty = b.specialty
WHERE a.group_number < b.group_number;
          

/* 11. Получить общее количество студентов, обучающихся на специальности ЭВМ. DONE */

SELECT SUM(number_person)
FROM STUDENT_GROUP
WHERE specialty = 'ЭВМ'

/* 12. Получить номера преподавателей, обучающих студентов по специальности ЭВМ DONE */

SELECT personal_number
FROM PREDICTOR_STUDENT_GROUP AS a
INNER JOIN STUDENT_GROUP AS b ON a.group_number = b.group_number
WHERE specialty = 'ЭВМ'

/* 13. Получить номера предметов, изучаемых всеми студенческими группами. DONE */

SELECT subject_number, COUNT(DISTINCT b.group_number)
FROM PREDICTOR_STUDENT_GROUP a
INNER JOIN STUDENT_GROUP b ON a.group_number = b.group_number
GROUP BY subject_number
HAVING COUNT(DISTINCT b.group_number) = (SELECT COUNT(group_number)
                                         FROM STUDENT_GROUP)


/* 14.  Получить  фамилии  преподавателей,  преподающих  те  же  предметы,  что  и  преподаватель преподающий предмет с номером 14П. DONE */

WITH aim_teachers AS (
    SELECT DISTINCT personal_number 
    FROM PREDICTOR_STUDENT_GROUP
    WHERE subject_number = '14П'
), 
aim_subjest AS (
    SELECT DISTINCT subject_number 
    FROM PREDICTOR_STUDENT_GROUP
    WHERE personal_number IN (SELECT * FROM aim_teachers)
), 
ans_teahers_nums AS (
    SELECT DISTINCT personal_number 
    FROM PREDICTOR_STUDENT_GROUP
    WHERE subject_number IN (SELECT * FROM aim_subjest)
)

SELECT surname 
FROM PREDICTOR
WHERE personal_number IN (SELECT * FROM ans_teahers_nums);

/* 15. Получить информацию о предметах, которые не ведет преподаватель с личным номером 221П. DONE */

SELECT *
FROM SUBJECT
WHERE subject_number NOT IN (SELECT DISTINCT subject_number
                             FROM PREDICTOR_STUDENT_GROUP
                             WHERE personal_number = '221Л')

/* 16. Получить информацию о предметах, которые не изучаются в группе М-6. DONE */

SELECT * 
FROM SUBJECT
EXCEPT
SELECT *
FROM SUBJECT 
WHERE subject_number IN (SELECT subject_number
                         FROM PREDICTOR_STUDENT_GROUP a
                         INNER JOIN STUDENT_GROUP b ON a.group_number = b.group_number
                         WHERE b.group_name = 'М-6')

/* 17. Получить информацию о доцентах, преподающих в группах 3Г и 8Г. DONE */

SELECT *
FROM PREDICTOR
WHERE personal_number IN (SELECT personal_number
                         FROM PREDICTOR_STUDENT_GROUP a
                         WHERE group_number = '3Г' OR group_number = '8Г') AND position = 'Доцент';

/* 18.  Получить  номера  предметов,  номера преподавателей,  номера  групп,  в  которых  ведут  занятия преподаватели с кафедры ЭВМ, имеющих специальность АСОИ. DONE */

SELECT a.subject_number, a.personal_number, a.group_number
FROM PREDICTOR_STUDENT_GROUP a 
INNER JOIN PREDICTOR b ON a.personal_number = b.personal_number
WHERE b.department = 'ЭВМ' AND b.specialty LIKE '%АСОИ%'

/* 19. Получить номера групп с такой же специальностью, что и специальность преподавателей. */

SELECT c.group_number
FROM PREDICTOR_STUDENT_GROUP a
JOIN PREDICTOR b ON a.personal_number = b.personal_number
JOIN STUDENT_GROUP c ON a.group_number = c.group_number
WHERE b.specialty LIKE '%' || c.specialty || '%'
GROUP BY c.group_number;



/* 20.  Получить  номера  преподавателей  с  кафедры  ЭВМ,  преподающих  предметы  по  специальности, совпадающей со специальностью студенческой группы. DONE */

SELECT DISTINCT b.personal_number
FROM PREDICTOR_STUDENT_GROUP a 
INNER JOIN PREDICTOR b ON a.personal_number = b.personal_number
INNER JOIN STUDENT_GROUP c ON a.group_number = c.group_number
INNER JOIN SUBJECT d ON a.subject_number = d.subject_number
WHERE c.specialty = d.specialty AND b.department = 'ЭВМ'

/* 21. Получить  специальности  студенческой  группы,  на  которых  работают  преподаватели  кафедры АСУ. DONE */

SELECT DISTINCT b.specialty
FROM PREDICTOR_STUDENT_GROUP a 
INNER JOIN STUDENT_GROUP b ON a.group_number = b.group_number
INNER JOIN PREDICTOR c ON a.personal_number = c.personal_number
WHERE department = 'АСУ'

/* 22. Получить номера предметов, изучаемых группой АС-8 DONE */

SELECT subject_number
FROM PREDICTOR_STUDENT_GROUP a
INNER JOIN STUDENT_GROUP b ON a.group_number = b.group_number
WHERE  b.group_name = 'АС-8'

/* 23. Получить  номера  студенческих  групп,  которые изучают  те  же  предметы,  что  и  студенческая группа АС-8. */


/* 24. Получить  номера  студенческих  групп,  которые  не  изучают  предметы,  преподаваемых  в студенческой группе АС-8.  */

SELECT sg.group_number
FROM STUDENT_GROUP sg
WHERE sg.group_number <> 'АС-8'
AND sg.group_number NOT IN (
    SELECT psg.group_number
    FROM PREDICTOR_STUDENT_GROUP psg
    WHERE psg.group_number = 'АС-8'
)
GROUP BY sg.group_number;


/* 25. Получить  номера  студенческих  групп,  которые  не  изучают  предметы,  преподаваемых преподавателем 430Л. */

SELECT group_number
FROM STUDENT_GROUP a

WHERE NOT EXISTS (
    SELECT *
    FROM PREDICTOR_STUDENT_GROUP b
    WHERE b.group_number = a.group_number
    AND b.personal_number = '430Л'
)
GROUP BY group_number;


/* 26. Получить  номера  преподавателей,  работающих  с  группой  Э-15,  но  не  преподающих  предмет 12П. DONE */

SELECT personal_number
FROM PREDICTOR_STUDENT_GROUP a 
INNER JOIN STUDENT_GROUP b ON a.group_number = b.group_number
WHERE b.group_name = 'Э-15'
EXCEPT
SELECT personal_number
FROM PREDICTOR_STUDENT_GROUP 
WHERE subject_number = '12П'



--ЗАДАНИЕ 2--

/* 24 ВАРИАНТ -> | 9 | 34 | 6 | 12 | 16 | 24 | 28 | 20 | 10 | 30 | */


/* 9. Получить номера деталей, поставляемых поставщиком в Минске. DONE */

SELECT DISTINCT d
FROM NUMBER_PARTS AS a
INNER JOIN SUPPLIERS_S AS b ON a.p = b.p 
WHERE b.city = 'Минск'

/* 34. Получить номера деталей, поставляемых либо минским поставщиком, либо для минского проекта. DONE */

SELECT DISTINCT d 
FROM NUMBER_PARTS AS a
INNER JOIN SUPPLIERS_S AS b ON a.p = b.p 
INNER JOIN PROJECTS_J AS c ON a.pr = c.pr
WHERE b.city = 'Минск' OR c.city = 'Минск' 

/* 6.  Получить все такие тройки "номера поставщиков-номера деталей-номера проектов", для которых выводимые поставщик, деталь и проект размещены в одном городе. DONE */

SELECT b.p, c.d, d.pr 
FROM NUMBER_PARTS AS a
INNER JOIN SUPPLIERS_S AS b ON a.p = b.p
INNER JOIN DETAILS_P AS c ON a.d = c.d 
INNER JOIN PROJECTS_J AS d ON a.pr = d.pr 
WHERE b.city = c.city AND b.city = d.city

/* 12. Получить  номера  деталей,  поставляемых  для  всех  проектов,  обеспечиваемых  поставщиком  из того же города, где размещен проект. DONE */

SELECT d
FROM NUMBER_PARTS AS a
INNER JOIN PROJECTS_J AS b ON a.pr = b.pr
INNER JOIN SUPPLIERS_S AS c ON a.p = c.p 
WHERE b.city = c.city

/* 16. Получить общее количество деталей Д1, поставляемых поставщиком П1. DONE */

SELECT SUM(s)
FROM NUMBER_PARTS
WHERE d = 'Д1' AND p = 'П1'

/* 24. Получить номера поставщиков со статусом, меньшим чем у поставщика П1. DONE */
SELECT p 
FROM SUPPLIERS_S
WHERE status < (SELECT status 
                FROM SUPPLIERS_S 
                WHERE p = 'П1')

/* 28. Получить  номера  проектов,  для  которых  не  поставляются  красные  детали  поставщиками  из Минска. DONE */

SELECT pr 
FROM NUMBER_PARTS
EXCEPT
SELECT pr 
FROM NUMBER_PARTS AS a
INNER JOIN SUPPLIERS_S AS b ON a.p = b.p 
INNER JOIN DETAILS_P AS c ON a.d = c.d
WHERE c.color = 'Красный' AND b.city = 'Минск'


/* 20. Получить цвета деталей, поставляемых поставщиком П1. DONE */

SELECT DISTINCT c.color 
FROM NUMBER_PARTS AS a
INNER JOIN SUPPLIERS_S AS b ON a.p = b.p 
INNER JOIN DETAILS_P AS c ON a.d = c.d
WHERE b.p = 'П1'

/* 10. Получить номера деталей, поставляемых поставщиком в Минске для проекта в Минске. DONE */

SELECT d 
FROM NUMBER_PARTS AS a 
INNER JOIN SUPPLIERS_S AS b ON a.p = b.p 
INNER JOIN PROJECTS_J AS c ON a.pr = c.pr
WHERE b.city = 'Минск' AND c.city = 'Минск'

/* 30. Получить номера деталей, поставляемых для минских проектов. DONE */

SELECT DISTINCT d 
FROM NUMBER_PARTS AS a 
INNER JOIN PROJECTS_J AS b ON a.pr = b.pr
WHERE b.city = 'Минск'