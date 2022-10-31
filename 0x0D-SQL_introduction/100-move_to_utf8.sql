-- convert database, table nad column character encoding
ALTER DATABASE hbtn_0c_0  CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_table  CONVERT TO CHARACTER SET utf8 COLLATE utf8_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8 COLLATE utf8mb4_unicode_ci;
