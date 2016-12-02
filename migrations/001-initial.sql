-- CREATE TABLE "public"."users" (
--     "id" serial,
--     "name" varchar(255),
--     "email" varchar(255),
--     "solved_challenges" jsonb DEFAULT '[]'::jsonb,
--     PRIMARY KEY ("id"),
--     UNIQUE ("email")
-- );
--
-- CREATE TABLE "public"."submissions" (
--     "id" serial,
--     "user_id" integer,
--     "created" timestamp without time zone NOT NULL DEFAULT current_timestamp,
--     "code" text NOT NULL,
--     PRIMARY KEY ("id"),
--     FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE SET NULL
-- );

CREATE TABLE submissions (
    id serial,
    name varchar(255),
    challenge_num integer,
    created timestamp without time zone NOT NULL DEFAULT current_timestamp,
    code text NOT NULL,
    PRIMARY KEY (id)
);
