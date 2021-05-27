# cluster_info_collect
集群信息收集
getCpuMessage.sh 这个脚本文件用来获取机器运行性能信息，写到控制台、
2、重定向到a文件，
3、通过txt_to_json.py文件把.txt格式的a文件转成json文件：test01.json
4、通过write.py文件把json格式的信息写入数据库中，数据库是cluster_performance，数据库中的表是info,

0、创建数据库，数据库的表，字段相关的代码：

