
DROP TABLE if exists courence;
CREATE TABLE "courence" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"date" date NOT NULL, 
"content" varchar(512) NOT NULL,
"user_id" integer NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX "courence_userId_date_createdAt_idx"
ON "courence" ("user_id" ASC,"date" ASC,"created_at" ASC);


DROP TABLE if exists "user";
CREATE TABLE "user" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"username" varchar(64) NOT NULL, 
"name" varchar(128) NOT NULL,
"password" varchar(64) NOT NULL,
"phone" varchar(32) NOT NULL,
"email" varchar(128) NULL,
"is_active" INTEGER NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX "user_username_idx"
ON "user" ("username" ASC);


DROP TABLE if exists theme;
CREATE TABLE "theme" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"date" date NOT NULL, 
"type" varchar(32) NOT NULL,
"name" varchar(64) NOT NULL,
"description" varchar(512) NOT NULL,
"user_id" integer NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX "theme_type_date_idx"
ON "theme" ("type" ASC,"date" ASC);

DROP TABLE if exists theme_content;
CREATE TABLE "theme_content" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"theme_id" integer NOT NULL,
"date" date NOT NULL, 
"content" text NOT NULL,
"user_id" integer NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX "theme_content_themeId_date_idx"
ON "theme_content" ("theme_id" ASC,"date" ASC);