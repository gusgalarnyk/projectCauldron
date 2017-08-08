DROP TABLE IF EXISTS prereqs CASCADE;

CREATE TABLE prereqs
(
   id      integer        NOT NULL,
   name    varchar(255)   NOT NULL,
   school  integer
);

ALTER TABLE public.prereqs
   ADD CONSTRAINT prereqs_pkey
   PRIMARY KEY (id);

COMMIT;