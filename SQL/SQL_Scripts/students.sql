DROP TABLE IF EXISTS students CASCADE;

CREATE TABLE students
(
   id              integer        NOT NULL,
   fname           varchar(255),
   lname           varchar(255),
   school          integer,
   project0_id     integer,
   project1_id     integer,
   project2_id     integer,
   project3_id     integer,
   project4_id     integer,
   school_email    varchar(255)   NOT NULL,
   personal_email  varchar(255),
   short_summary   varchar(100),
   full_summary    varchar(255),
   degree_program  varchar(255),
   minor           varchar(255),
   birthdate       date,
   ra              boolean,
   honors          boolean,
   full_time       boolean,
   club0_id        integer,
   club1_id        integer,
   club3_id        integer,
   club4_id        integer,
   password        varchar(255)   NOT NULL
);

ALTER TABLE public.students
   ADD CONSTRAINT students_pkey
   PRIMARY KEY (id);

COMMENT ON COLUMN students.project4_id IS 'as a student you can be a member of up to 5 projects total';

COMMIT;