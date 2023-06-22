# DataBase-Query-System
The system accept a CSV file (students.csv) as input as the initial database. After initial loading of the file, the records sorted by their index. The query will be given in SQL with a restricted command set for simplicity. The resulting data set (result of the query) stored as a JSON file.

SELECT {ALL|column_name} FROM STUDENTS WHERE {column_name|=,!=,<,>,<=,>=,!<,!>,AND,OR} ORDER BY{ASC|DSC}
