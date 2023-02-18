-- full description of table
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_DEFAULT, COLUMN_KEY
FROM information_schema.COLUMNS
WHERE TABLE_NAME = 'first_table'
AND TABLE_SCHEMA = 'hbtn_0c_0';
