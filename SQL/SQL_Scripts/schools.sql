DROP TABLE IF EXISTS schools CASCADE;

CREATE TABLE schools
(
   id       integer        NOT NULL,
   name     varchar(255),
   city     varchar(255),
   state    varchar(255),
   zipcode  integer,
   country  integer
);

ALTER TABLE public.schools
   ADD CONSTRAINT schools_pkey
   PRIMARY KEY (id);

COMMIT;