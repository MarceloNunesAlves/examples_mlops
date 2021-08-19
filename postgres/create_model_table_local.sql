create schema modelstore;

DROP TABLE IF EXISTS modelstore.futurex_model_catalog;
CREATE TABLE modelstore.futurex_model_catalog
(
    model_id integer NOT NULL,
    model_name character varying COLLATE pg_catalog."default" NOT NULL,
    model_file bytea NOT NULL
);