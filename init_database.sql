
# 1. connect mysql
mysql -u root -p

# 2. create database
create database cluster_performance;
use cluster_performance;

# 3. create table
create table info( ip varchar(20), hostname varchar(20), usercpu varchar(20), freecpu varchar(20), cputexttime varchar(20), cpubalance varchar(20), cputask varchar(20), memsize varchar(20), osremainmem varchar(20), appremainmem varchar(20), swapallsize varchar(20), swapremainsize varchar(20), queryiotime varchar(20), queryiolongth varchar(20), iotimeavg varchar(20), iocpu varchar(20));

# 4. review table struct
desc info;

