CREATE SEQUENCE IF NOT EXISTS application_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS categORy_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS course_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS course_price_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS education_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS job_title_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


 CREATE SEQUENCE IF NOT EXISTS ORganization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE IF NOT EXISTS sex_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE IF NOT EXISTS teacher_document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE IF NOT EXISTS teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE IF NOT EXISTS type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE TABLE IF NOT EXISTS ORganization
(
    id integer NOT NULL DEFAULT nextval('ORganization_id_seq'::regclass),
    code character varying(50), 
    name character varying(256), 
    phone character varying(16), 
    email character varying(256), 
	address character varying(256),  
	CONSTRAINT ORganization_pkey PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS application
(
    id integer NOT NULL DEFAULT nextval('application_id_seq'::regclass),
    name character varying(256),
    address character varying(256),
    phone character varying(50),
    email character varying(256),
    ORganization_id integer,
    employees integer,
    CONSTRAINT application_pkey PRIMARY KEY (id),
    CONSTRAINT application_ORganization_id_fkey FOREIGN KEY (ORganization_id)
        REFERENCES ORganization (id)
);

CREATE TABLE IF NOT EXISTS type
(
    id integer NOT NULL DEFAULT nextval('type_id_seq'::regclass),
    name character varying(256),
    CONSTRAINT type_pkey PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS course
(
    id integer NOT NULL DEFAULT nextval('course_id_seq'::regclass),
    code character varying(50),
    name character varying(256),
    type_id integer,
    days integer,
    students integer,
    price integer,
	price_nds integer,
	ORganization_id integer,
    CONSTRAINT course_pkey PRIMARY KEY (id),
    CONSTRAINT course_type_id_fkey FOREIGN KEY (type_id)
        REFERENCES type (id),
	CONSTRAINT ORganization_id_fkey FOREIGN KEY (ORganization_id)
        REFERENCES ORganization (id)
);


CREATE TABLE IF NOT EXISTS job_title
(
    id integer NOT NULL DEFAULT nextval('job_title_id_seq'::regclass),
    name character varying(256),
    CONSTRAINT job_title_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS employee
(
    id integer NOT NULL DEFAULT nextval('employee_id_seq'::regclass),
    first_name character varying(50),
    surname character varying(50),
    middle_name character varying,
    job_title_id integer,
    CONSTRAINT employee_pkey PRIMARY KEY (id),
    CONSTRAINT employee_job_title_id_fkey FOREIGN KEY (job_title_id)
        REFERENCES job_title (id)
);


CREATE TABLE IF NOT EXISTS application_course
(
    application_id integer NOT NULL,
    course_id integer NOT NULL,
    employee_id integer NOT NULL,
    date date,
    CONSTRAINT application_course_pkey PRIMARY KEY (application_id, course_id, employee_id),
    CONSTRAINT application_course_application_id_fkey FOREIGN KEY (application_id)
        REFERENCES application (id),
    CONSTRAINT application_course_course_id_fkey 
    FOREIGN KEY (course_id)
        REFERENCES course (id),
    CONSTRAINT application_course_employee_id_fkey 
    FOREIGN KEY (employee_id)
        REFERENCES employee (id)
);


CREATE TABLE IF NOT EXISTS categORy
(
    id integer NOT NULL DEFAULT nextval('categORy_id_seq'::regclass),
    name character varying(50),
    CONSTRAINT categORy_pkey PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS course_price
(
    id integer NOT NULL DEFAULT nextval('course_price_id_seq'::regclass),
    "number" integer,
    date date,
    price integer,
    course_id bigint not null,
    CONSTRAINT course_price_course_id_fkey FOREIGN KEY (course_id)
        REFERENCES course (id)
);


CREATE TABLE IF NOT EXISTS education
(
    id integer NOT NULL DEFAULT nextval('education_id_seq'::regclass),
    name character varying,
    CONSTRAINT education_pkey PRIMARY KEY (id)
);


CREATE TABLE IF NOT EXISTS sex
(
    id integer NOT NULL DEFAULT nextval('sex_id_seq'::regclass),
    name character varying ,
    CONSTRAINT sex_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS teacher
(
    id integer NOT NULL DEFAULT nextval('teacher_id_seq'::regclass),
    first_name character varying(50),
    surname character varying(50),
    middle_name character varying(50),
    sex_id integer,
    education_id integer,
    birthday date,
    categORy_id integer,
    CONSTRAINT teacher_pkey PRIMARY KEY (id),
    CONSTRAINT teacher_categORy_id_fkey FOREIGN KEY (categORy_id)
        REFERENCES categORy (id),
    CONSTRAINT teacher_education_id_fkey FOREIGN KEY (education_id)
        REFERENCES education (id),
    CONSTRAINT teacher_sex_id_fkey FOREIGN KEY (sex_id)
        REFERENCES sex (id)
);


CREATE TABLE IF NOT EXISTS teacher_document
(
    id integer NOT NULL DEFAULT nextval('teacher_document_id_seq'::regclass),
    teacher_id integer,
    start date,
    "end" date,
    course_id integer,
    CONSTRAINT teacher_document_pkey PRIMARY KEY (id),
    CONSTRAINT teacher_document_course_id_fkey FOREIGN KEY (course_id)
        REFERENCES course (id),
    CONSTRAINT teacher_document_teacher_id_fkey FOREIGN KEY (teacher_id)
        REFERENCES teacher (id)
);




-----TRIGGER


CREATE OR REPLACE FUNCTION price_compute() RETURNS trigger as $priceTrigger$
DECLARE
newest_date date;
   BEGIN
   SELECT max(date)
   INTO newest_date
   FROM course_price
   where course_id = NEW.course_id;
   IF newest_date is null OR newest_date < NEW.date 
   THEN
    UPDATE Course
	set price = NEW.price , price_nds = ROUND(NEW.price * 1.2);
	end IF;
	return new;
  END;
$priceTrigger$
LANGUAGE plpgsql;


 CREATE OR REPLACE TRIGGER priceTrigger 
 BEFORE INSERT OR UPDATE
 ON course_price
 FOR EACH ROW 
 EXECUTE PROCEDURE price_compute();



CREATE OR REPLACE FUNCTION teacher_document_validation() RETURNS trigger as $teacherTrigger$
DECLARE
   BEGIN
   
    IF EXISTS (
		SELECT 1 
		FROM teacher_document 
		WHERE teacher_document.course_id = NEW.course_id AND (
			teacher_document.start BETWEEN NEW.start AND NEW."end"
			   OR "end" BETWEEN NEW.start AND NEW."end"
		)
	) THEN 
    RETURN NULL;
     ELSE
    RETURN NEW;
    end IF;
  END;
$teacherTrigger$
LANGUAGE plpgsql;


 CREATE OR REPLACE TRIGGER teacherTrigger 
 BEFORE INSERT OR UPDATE
 ON teacher_document
 FOR EACH ROW 
 EXECUTE PROCEDURE teacher_document_validation();
 
CREATE OR REPLACE view course_and_current_teacher AS
SELECT id, code, name, type_id, days, students, price, price_nds, ORganization_id, (
	SELECT teacher_id 
	FROM teacher_document WHERE NOW() BETWEEN start and "end" 
	AND teacher_document.course_id = course.id
) FROM course















CREATE OR REPLACE FUNCTION price_compute() RETURNS TRIGGER AS $$
DECLARE
   newest_date DATE;
BEGIN
   SELECT MAX(date)
   INTO newest_date
   FROM course_price
   WHERE course_id = NEW.course_id;

   IF newest_date IS NULL OR newest_date < NEW.date THEN
      UPDATE course
      SET price = NEW.price, price_nds = ROUND(NEW.price * 1.2)
      WHERE course_id = NEW.course_id;
   END IF;

   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER priceTrigger 
BEFORE INSERT OR UPDATE ON course_price
FOR EACH ROW 
EXECUTE FUNCTION price_compute();


CREATE OR REPLACE FUNCTION teacher_document_validation() RETURNS TRIGGER AS $$
BEGIN
   IF EXISTS (
      SELECT 1 
      FROM teacher_document 
      WHERE course_id = NEW.course_id AND (
         start BETWEEN NEW.start AND NEW."end" OR
         "end" BETWEEN NEW.start AND NEW."end"
      )
   ) THEN 
      RETURN NULL;
   ELSE
      RETURN NEW;
   END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER teacherTrigger 
BEFORE INSERT OR UPDATE ON teacher_document
FOR EACH ROW 
EXECUTE FUNCTION teacher_document_validation();