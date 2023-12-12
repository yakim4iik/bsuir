CREATE SEQUENCE IF NOT EXISTS application_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE IF NOT EXISTS category_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE course_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE course_price_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE education_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE SEQUENCE job_title_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


 CREATE SEQUENCE organization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE sex_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE teacher_document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE teacher_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

 CREATE SEQUENCE type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE TABLE IF NOT EXISTS organization
(
    id integer NOT NULL DEFAULT nextval('organization_id_seq'::regclass),
    code character varying(50), 
    name character varying(256), 
    phone character varying(10), 
    email character varying(256), 
    CONSTRAINT organization_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS application
(
    id integer NOT NULL DEFAULT nextval('application_id_seq'::regclass),
    name character varying(256),
    address character varying(256),
    phone character varying(50),
    email character varying(256),
    organization_id integer,
    empoyees integer,
    CONSTRAINT application_pkey PRIMARY KEY (id),
    CONSTRAINT application_organization_id_fkey FOREIGN KEY (organization_id)
        REFERENCES organization (id)
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
    CONSTRAINT course_pkey PRIMARY KEY (id),
    CONSTRAINT course_type_id_fkey FOREIGN KEY (type_id)
        REFERENCES type (id)
);

CREATE TABLE IF NOT EXISTS application_course
(
    aplication_id integer NOT NULL,
    course_id integer NOT NULL,
    employee_id integer NOT NULL,
    date date,
    CONSTRAINT application_course_pkey PRIMARY KEY (aplication_id, course_id, employee_id),
    CONSTRAINT application_course_aplication_id_fkey FOREIGN KEY (aplication_id)
        REFERENCES application (id),
    CONSTRAINT application_course_course_id_fkey 
    FOREIGN KEY (course_id)
        REFERENCES course (id),
    CONSTRAINT application_course_employee_id_fkey 
    FOREIGN KEY (employee_id)
        REFERENCES employee (id)
);

CREATE TABLE IF NOT EXISTS category
(
    id integer NOT NULL DEFAULT nextval('category_id_seq'::regclass),
    name character varying(50),
    CONSTRAINT category_pkey PRIMARY KEY (id)
);



CREATE TABLE IF NOT EXISTS course_price
(
    id integer NOT NULL DEFAULT nextval('course_price_id_seq'::regclass),
    "number" integer,
    date date,
    price integer,
    course_id bigint,
    CONSTRAINT course_price_course_id_fkey FOREIGN KEY (course_id)
        REFERENCES course (id)
);

CREATE TABLE IF NOT EXISTS education
(
    id integer NOT NULL DEFAULT nextval('education_id_seq'::regclass),
    name character varying,
    CONSTRAINT education_pkey PRIMARY KEY (id)
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
    category_id integer,
    CONSTRAINT teacher_pkey PRIMARY KEY (id),
    CONSTRAINT teacher_category_id_fkey FOREIGN KEY (category_id)
        REFERENCES category (id),
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
    corse_id integer,
    CONSTRAINT teacher_document_pkey PRIMARY KEY (id),
    CONSTRAINT teacher_document_corse_id_fkey FOREIGN KEY (corse_id)
        REFERENCES course (id),
    CONSTRAINT teacher_document_teacher_id_fkey FOREIGN KEY (teacher_id)
        REFERENCES teacher (id)
);
