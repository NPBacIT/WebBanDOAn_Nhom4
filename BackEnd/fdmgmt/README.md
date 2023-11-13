# Simple backend for food managament website

## Installation
1. Create database and insert data
```
docker-compose up -d
```
- NOTE: You can use microsoft azure data studio to execute .sql or simply using Windows and DBMS

2. Connect to DB and use sqlcmd to query
```
root@ops-huynda-nodedb:~# docker ps
CONTAINER ID   IMAGE                                        COMMAND                  CREATED       STATUS       PORTS                                           	NAMES
aad14346999e   api                                          "gunicorn api:app --…"   6 hours ago   Up 6 hours   0.0.0.0:<port>-><port>/tcp, :::<port>-><port>/tcp   	relaxed_bohr
459430cb716a   mcr.microsoft.com/mssql/server:2019-latest   "/opt/mssql/bin/perm…"   10 days ago   Up 10 days   0.0.0.0:<port>-><port>/tcp, :::<port>-><port>/tcp       sqlserver
root@ops-huynda-nodedb:~# docker exec -it 459430cb716a bash

NOTE: Read docker-compose for user and password
mssql@459430cb716a:/$ /opt/mssql-tools/bin/sqlcmd -U <username> -P <password> -d <database>

# basic query
1> SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='MonAn';
2> go
COLUMN_NAME                                                                                                                     
--------------------------------------------------------------------------------------------------------------------------------
MaMA                                                                                                                            
TenMA                                                                                                                           
ChiTietMA                                                                                                                       
Gia                                                                                                                             
AnhMA                                                                                                                           
SoLuongMA                                                                                                                       
Active                                                                                                                          
isDeleted                                                                                                                       
MaLoaiMA                                       

1> SELECT MaMA,TenMA,Gia FROM MonAn;
2> go
MaMA        TenMA                                                                                                Gia        
----------- ---------------------------------------------------------------------------------------------------- -----------
          1 Delicious Pizza                                                                                               18
          2 Delicious Burger                                                                                              15
          3 Delicious Pizza                                                                                               17
          4 Delicious Pasta                                                                                               10
          5 French Fries                                                                                                  15
          6 Delicious Pizza                                                                                               12
          7 Tasty Burger                                                                                                  14
          8 Tasty Burger                                                                                                  10
          9 French Fries                                                                                                  15
```

3. Run dockerfile
```
docker build -f Dockerfile -t api <dockerfile_path>
docker run -p <port>:<port> -d api
```
