# DataBase-Query-System
The system accept a CSV file (students.csv) as input as the initial database. After initial loading of the file, the records sorted by their index. The query will be given in SQL with a restricted command set for simplicity. The resulting data set (result of the query) stored as a JSON file.

After finishing the query, the program must wait for another query, or quits if the user enters exit.

You can assume queries as case-insensitive.

# Simplified SQL Forms

SELECT {ALL|column_name} FROM STUDENTS WHERE {column_name|=,!=,<,>,<=,>=,!<,!>,AND,OR} ORDER BY {ASC|DSC}

INSERT INTO STUDENT VALUES (val1,val2,val3,…)

DELETE FROM STUDENT WHERE {column_name|=,!=,<,>,<=,>=,!<,!>,AND,OR}

exit
