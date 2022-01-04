 use DRDB;
 
 create table stock(
    -> id int AUTO_INCREMENT PRIMARY KEY,
    -> name varchar(250),
    -> price float,
    -> quantity int);