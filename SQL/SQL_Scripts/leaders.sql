DROP TABLE IF EXISTS leaders CASCADE;

CREATE TABLE leaders
(
   id           integer        NOT NULL,
   fname        varchar(255),
   lname        varchar(255),
   school       integer,
   project0_id  integer,
   project1_id  integer,
   project2_id  integer
);

ALTER TABLE public.leaders
   ADD CONSTRAINT leaders_pkey
   PRIMARY KEY (id);

COMMIT;
