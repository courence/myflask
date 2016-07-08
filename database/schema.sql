
create table IF NOT EXISTS  courence (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"date" date NOT NULL, 
"content" varchar(512) NOT NULL,
"user_id" integer NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX if not EXISTS  "courence_userId_date_createdAt_idx"
ON "courence" ("user_id" ASC,"date" ASC,"created_at" ASC);


create table IF NOT EXISTS  "user" (
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
CREATE INDEX if not EXISTS  "user_username_idx"
ON "user" ("username" ASC);


create table IF NOT EXISTS  theme (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"date" date NOT NULL, 
"type" varchar(32) NOT NULL,
"name" varchar(64) NOT NULL,
"description" varchar(512) NOT NULL,
"user_id" integer NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX if not EXISTS  "theme_type_date_idx"
ON "theme" ("type" ASC,"date" ASC);

create table IF NOT EXISTS  theme_content (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"theme_id" integer NOT NULL,
"date" date NOT NULL, 
"content" text NOT NULL,
"user_id" integer NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX if not EXISTS  "theme_content_themeId_date_idx"
ON "theme_content" ("theme_id" ASC,"date" ASC);


create table IF NOT EXISTS  task (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"type" varchar(32) NOT NULL,
"priority" varchar(32) NOT NULL,
"state" varchar(32) NOT NULL,
"begin_date" date NOT NULL, 
"end_date" date NOT NULL, 
"content" text NOT NULL,
"user_id" integer NULL,
"remark" varchar(128) NULL,
"updated_at" datetime NOT NULL,
"created_at" datetime NOT NULL
);
CREATE INDEX if not EXISTS  "task_themeId_priority_idx"
ON "task" ("user_id" ASC,"priority" ASC);