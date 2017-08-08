DROP TABLE IF EXISTS advisers CASCADE;

CREATE TABLE advisers
(
   id           integer        NOT NULL,
   fname        varchar(255),
   lname        varchar(255),
   school       varchar(255),
   project0_id  integer,
   project1_id  integer,
   project2_id  integer
);

ALTER TABLE public.advisers
   ADD CONSTRAINT advisers_pkey
   PRIMARY KEY (id);

COMMIT;
