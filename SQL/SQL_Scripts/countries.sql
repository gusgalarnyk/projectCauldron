DROP TABLE IF EXISTS countries CASCADE;

CREATE TABLE countries
(
   id    integer        NOT NULL,
   name  varchar(255)
);

ALTER TABLE public.countries
   ADD CONSTRAINT countries_pkey
   PRIMARY KEY (id);

COMMIT;