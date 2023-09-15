/*
TASK 1
*/

DROP TABLE IF EXISTS PREDICTOR_STUDENT_GROUP;
DROP TABLE IF EXISTS PREDICTOR;
DROP TABLE IF EXISTS SUBJECT;
DROP TABLE IF EXISTS STUDENT_GROUP;

CREATE TABLE PREDICTOR (
    personal_number   VARCHAR(4)    PRIMARY KEY,
		surname           VARCHAR(16)   NOT NULL,
		position          VARCHAR(16)   NOT NULL,
		department        VARCHAR(16)   NOT NULL,
		specialty         VARCHAR(32)   NOT NULL,
		phone_home        SMALLINT      NOT NULL
);

CREATE TABLE SUBJECT (
    subject_number    VARCHAR(4)    PRIMARY KEY,
		subject_name      VARCHAR(16)   NOT NULL,
		number_hours      SMALLINT      NOT NULL,
		specialty         VARCHAR(16)   NOT NULL,
		semester          SMALLINT      NOT NULL
);

CREATE TABLE STUDENT_GROUP (
    group_number      VARCHAR(4)    PRIMARY KEY,
		group_name        VARCHAR(16)   NOT NULL,
		number_person     SMALLINT      NOT NULL,
		specialty         VARCHAR(32)   NOT NULL,
		name_head         VARCHAR(16)   NOT NULL
);

CREATE TABLE PREDICTOR_STUDENT_GROUP (
    group_number      VARCHAR(4)    REFERENCES STUDENT_GROUP (group_number),
		subject_number    VARCHAR(4)    REFERENCES SUBJECT (subject_number),
		personal_number   VARCHAR(4)    REFERENCES PREDICTOR (personal_number),
		audience_number   SMALLINT      NOT NULL,

		CONSTRAINT PREDICTOR_STUDENT_GROUP_pkey PRIMARY KEY (group_number, subject_number, personal_number)
);

INSERT INTO PREDICTOR
VALUES 
        ('221Л', 'Фролов', 'Доцент', 'ЭВМ', 'АСОИ, ЭВМ', 487),
				('222Л', 'Костин', 'Доцент', 'ЭВМ', 'ЭВМ', 543),
				('225Л', 'Бойко',  'Профессор', 'АСУ', 'АСОИ, ЭВМ', 112),
				('430Л', 'Глазов', 'Ассистент', 'ТФ', 'СД', 421),
				('110Л', 'Петров', 'Ассистент', 'Экономики', 'Международная экономика', 487);

INSERT INTO SUBJECT
VALUES 
        ('12П', 'Мини ЭВМ', 36, 'ЭВМ', 1),
				('14П', 'ПЭВМ', 72, 'ЭВМ', 2),
				('17П', 'СУБД ПК', 48, 'АСОИ', 4),
				('18П', 'ВКСС', 52, 'АСОИ', 6),
				('34П', 'Физика', 30, 'СД', 6),
				('22П', 'Аудит', 24, 'Бухучета', 3);

INSERT INTO STUDENT_GROUP
VALUES 
        ('8Г', 'Э-12', 18, 'ЭВМ', 'Иванова'),
				('7Г', 'Э-15', 22, 'ЭВМ', 'Сеткин'),
				('4Г', 'АС-9', 24, 'АСОИ', 'Балабанов'),
				('3Г', 'АС-8', 20, 'АСОИ', 'Чижов'),
				('17Г', 'С-14', 29, 'СД', 'Амросов'),
				('12Г', 'М-6', 16, 'Международная экономика', 'Трубин'),
				('10Г', 'Б-4', 21, 'Бухучет', 'Зязюткин');

INSERT INTO PREDICTOR_STUDENT_GROUP
VALUES 
        ('8Г', '12П', '222Л', 112),
				('8Г', '14П', '221Л', 220),
				('8Г', '17П', '222Л', 112),
				('7Г', '14П', '221Л', 220),
				('7Г', '17П', '222Л', 241),
				('7Г', '18П', '225Л', 210),
				('4Г', '12П', '222Л', 112),
				('4Г', '18П', '225Л', 210),
				('3Г', '12П', '222Л', 112),
				('3Г', '17П', '221Л', 241),
				('3Г', '18П', '225Л', 210),
				('17Г', '12П', '222Л', 112),
				('17Г', '22П', '110Л', 220),
				('17Г', '34П', '430Л', 118),
				('12Г', '12П', '222Л', 112),
				('12Г', '22П', '110Л', 210),
				('10Г', '12П', '222Л', 210),
				('10Г', '22П', '110Л', 210);

/*
TASK 2
*/

DROP TABLE IF EXISTS NUMBER_PARTS;
DROP TABLE IF EXISTS SUPPLIERS_S;
DROP TABLE IF EXISTS DETAILS_P;
DROP TABLE IF EXISTS PROJECTS_J;

CREATE TABLE SUPPLIERS_S (
    p                 VARCHAR(2)    PRIMARY KEY,
		name_p            VARCHAR(8)    NOT NULL,
	  status            SMALLINT      NOT NULL,
		city              VARCHAR(8)    NOT NULL
);

CREATE TABLE DETAILS_P (
    d                 VARCHAR(2)    PRIMARY KEY,
		name_d            VARCHAR(8)    NOT NULL,
		color             VARCHAR(8)    NOT NULL,
		size              SMALLINT      NOT NULL,
		city              VARCHAR(8)    NOT NULL
);

CREATE TABLE PROJECTS_J (
    pr                VARCHAR(4)    PRIMARY KEY,
		name_pr           VARCHAR(4)    NOT NULL,
		city              VARCHAR(8)    NOT NULL
);

CREATE TABLE NUMBER_PARTS (
    p                 VARCHAR(2)    REFERENCES SUPPLIERS_S (p),
		d                 VARCHAR(2)    REFERENCES DETAILS_P (d),
		pr                VARCHAR(4)    REFERENCES PROJECTS_J (pr),
		s                 SMALLINT      NOT NULL,

		CONSTRAINT NUMBER_PARTS_pkey PRIMARY KEY (p, d, pr)
);

INSERT INTO SUPPLIERS_S
VALUES 
        ('П1', 'Петров', 20, 'Москва'),
				('П2', 'Синицин', 10, 'Таллинн'),
				('П3', 'Федоров', 30, 'Таллинн'),
				('П4', 'Чаянов', 20, 'Минск'),
				('П5', 'Крюков', 30, 'Киев');

INSERT INTO DETAILS_P
VALUES 
        ('Д1', 'Болт', 'Красный', 12, 'Москва'),
				('Д2', 'Гайка', 'Зеленая', 17, 'Минск'),
				('Д3', 'Диск', 'Черный', 17, 'Вильнюс'),
				('Д4', 'Диск', 'Черный', 14, 'Москва'),
				('Д5', 'Корпус', 'Красный', 12, 'Минск'),
				('Д6', 'Крышки', 'Красный', 19, 'Москва');

INSERT INTO PROJECTS_J
VALUES 
        ('ПР1', 'ИПР1', 'Минск'),
				('ПР2', 'ИПР2', 'Таллинн'),
				('ПР3', 'ИПР3', 'Псков'),
				('ПР4', 'ИПР4', 'Псков'),
				('ПР5', 'ИПР5', 'Москва'),
				('ПР6', 'ИПР6', 'Саратов'),
				('ПР7', 'ИПР7', 'Москва');

INSERT INTO NUMBER_PARTS
VALUES 
        ('П1', 'Д1', 'ПР1', 200),
				('П1', 'Д1', 'ПР2', 700),
				('П2', 'Д3', 'ПР1', 400),
				('П2', 'Д2', 'ПР2', 200),
				('П2', 'Д3', 'ПР3', 200),
				('П2', 'Д3', 'ПР4', 500),
				('П2', 'Д3', 'ПР5', 600),
				('П2', 'Д3', 'ПР6', 400),
				('П2', 'Д3', 'ПР7', 800),
				('П2', 'Д5', 'ПР2', 100),
				('П3', 'Д3', 'ПР1', 200),
				('П3', 'Д4', 'ПР2', 500),
				('П4', 'Д6', 'ПР3', 300),
				('П4', 'Д6', 'ПР7', 300),
				('П5', 'Д2', 'ПР2', 200),
				('П5', 'Д2', 'ПР4', 100),
				('П5', 'Д5', 'ПР5', 500),
				('П5', 'Д5', 'ПР7', 100),
				('П5', 'Д6', 'ПР2', 200),
				('П5', 'Д1', 'ПР2', 100),
				('П5', 'Д3', 'ПР4', 200),
				('П5', 'Д4', 'ПР4', 800),
				('П5', 'Д5', 'ПР4', 400),
				('П5', 'Д6', 'ПР4', 500);