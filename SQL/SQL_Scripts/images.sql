DROP TABLE IF EXISTS images CASCADE;

CREATE TABLE images
(
   id                integer       NOT NULL,
   name              varchar(36),
   imagedata         bytea         NOT NULL,
   student_owner_id  integer,
   project_owner_id  integer
);

ALTER TABLE public.images
   ADD CONSTRAINT images_pkey
   PRIMARY KEY (id);

COMMIT;