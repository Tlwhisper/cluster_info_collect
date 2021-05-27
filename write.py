#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import os
import json 

class MysqlServer(object):
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = password
        self.conn = self.__create_connection()

    def __create_connection(self):
        #和远端mysql建立连接
        conn = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, charset='utf8')
        #选取数据库
        conn.select_db("cluster_performance")
        return conn

    def close(self):
        #关闭连接
        self.conn.close()

    def execute(self, sql):
        #执行sql语句
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()


#def get_comment_data_info(file_path):
    #获取文件内容
    #with open(file_path, 'r') as file:
    #    comment_data_info = file.read()
    #return comment_data_info


def get_comment_data_info(file_path):
    #获取文件内容
    with open(file_path,'r') as jsonfile:
        json_string = json.load(jsonfile)
    return json_string

def write_data_to_db(data):
    #判断文件是否存在
    if not os.path.exists(data['data_info']['file_path']):
        return "file: %s not exist" % data['data_info']['file_path']
    json_string = get_comment_data_info(data['data_info']['file_path'])

    #生成sql语句
    #sql = "INSERT INTO user_info(username, course_id, score, comment) VALUES " "('%s', '%s', '%d', '%s')" % \
            #     (data['data_info']['username'], data['data_info']['course_id'], data['data_info']['score'], comment_data_info)
    print(type(json_string))
    #json_string = json.loads(json_string)
    sql = "INSERT INTO info(ip, hostname, usercpu, freecpu, cputexttime, cpubalance, cputask, memsize, osremainmem, appremainmem, swapallsize, swapremainsize, queryiotime, queryiolongth, iotimeavg, iocpu) VALUES ('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(json_string['IP'], json_string['hostname'], json_string['usercpu'], json_string['freecpu'], json_string['cputexttime'], json_string['cpubalance'], json_string['cputask'], json_string['memsize'], json_string['osremainmem'], json_string['appremainmem'], json_string['swapallsize'], json_string['swapremainsize'], json_string['queryiotime'], json_string['queryiolongth'], json_string['iotimeavg'], json_string['iocpu'])

#    try:
    mysql_server = MysqlServer(data['db_info']['host'], data['db_info']['port'], data['db_info']['user'],data['db_info']['passwd'])
    mysql_server.execute(sql)
#    except Exception as e:
#       print("error show!!!")
#        return str(e)
    return "insert success"

def  main():
    data = {
            #remote database info;
            "db_info": {"host": "192.168.130.129",
                "port": 3306,
                "user": "root",
                "passwd": "hahaha369",},
            # file route
            "data_info": {
                "file_path":"./test01.json"}
            }
    status = write_data_to_db(data)
    print(status)
if __name__ == "__main__":
    main()
