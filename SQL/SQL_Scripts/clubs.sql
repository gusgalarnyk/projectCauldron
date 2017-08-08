DROP TABLE IF EXISTS clubs CASCADE;

CREATE TABLE clubs
(
   id      integer        NOT NULL,
   name    varchar(255),
   school  integer
);

ALTER TABLE public.clubs
   ADD CONSTRAINT clubs_pkey
   PRIMARY KEY (id);

COMMIT;