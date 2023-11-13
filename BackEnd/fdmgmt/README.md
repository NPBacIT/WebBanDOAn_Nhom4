# Simple backend for food managament website

##i Installation
1. Docker installation
- Using docker desktop for windows with hyper-V or wsl(recommended), docker engine for Linux user
	+ [docker desktop](https://docs.docker.com/desktop/install/windows-install/)
	+ [docker engine](https://docs.docker.com/engine/install)

- Install docker-compose
```
root@ops-huynda-nodedb:~# apt-get update
root@ops-huynda-nodedb:~# apt-get install docker-compose
```

2. Create database and insert data
```
docker-compose up -d
```

- install microsoft azure data studio
[microsoft azure data studio](https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio?view=sql-server-ver16&tabs=win-install%2Cwin-user-install%2Credhat-install%2Cwindows-uninstall%2Credhat-uninstall)
- NOTE: You can use microsoft azure data studio to execute .sql or simply using Windows and DBMS. Read the docs for installation

3. Connect to DB and use sqlcmd to query
```
root@ops-huynda-nodedb:~# docker ps
CONTAINER ID   IMAGE                                        COMMAND                  CREATED       STATUS       PORTS                                           	NAMES
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

4. Run dockerfile
```
docker build -f Dockerfile -t api <dockerfile_path>
docker run -p <port>:<port> --name <app_name> -d api
```

5. Test using postman
- NOTE: Read the docs for installation or simply use Postman on the web
- [postman](https://www.postman.com/downloads/)
