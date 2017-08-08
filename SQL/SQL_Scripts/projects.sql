DROP TABLE IF EXISTS projects CASCADE;

CREATE TABLE projects
(
   project_id         integer        NOT NULL,
   project_name       varchar(255)   NOT NULL,
   short_summary      varchar(100),
   full_summary       varchar(255),
   affiliated_club    varchar(255)   NOT NULL,
   begin_date         date,
   expected_end_date  date,
   students_involved  varchar(255)   NOT NULL,
   associated_school  integer        NOT NULL
);

ALTER TABLE public.projects
   ADD CONSTRAINT project_pkey
   PRIMARY KEY (project_id);

COMMIT;
