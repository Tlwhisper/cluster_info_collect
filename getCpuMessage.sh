#!/bin/bash

# 1 获取要监控的本地服务器IP地址
IP=`ifconfig | grep inet | grep -vE 'inet6|127.0.0.1' | awk '{print $2}'`
echo "IP="$IP
# 2 hostname
HOSTNAME=`hostname`
echo "hostname="$HOSTNAME

# 3 获取用户空间占用CPU百分比
cpu_user=`top -b -n 1 | grep Cpu | awk '{print $2}' | cut -f 1 -d "%"`
echo "usercpu="$cpu_user

# 4 获取空闲CPU百分比
cpu_idle=`top -b -n 1 | grep Cpu | awk '{print $5}' | cut -f 1 -d "%"`
echo "freecpu="$cpu_idle 

# 5 获取CPU上下文切换次数
cpu_context_switch=`vmstat -n 1 1 | sed -n 3p | awk '{print $12}'`
echo "cputexttime="$cpu_context_switch 

# 6 获取CPU5分钟前到现在的负载平均值
cpu_load_5min=`uptime | awk '{print $10}' | cut -f 1 -d ','`
echo "cpubalance="$cpu_load_5min
 
# 7 获取任务队列(就绪状态等待的进程数)
cpu_task_length=`vmstat -n 1 1 | sed -n 3p | awk '{print $1}'`
echo "cputask="$cpu_task_length

# 8 获取物理内存总量
mem_total=`free | grep Mem | awk '{print $2}'`
echo "memsize="$mem_total

# 9 获取操作系统未使用内存总量
mem_sys_free=`free | grep Mem | awk '{print $4}'`
echo "osremainmem="$mem_sys_free

# 10 获取应用程序未使用内存总量
mem_user_free=`free | sed -n 3p | awk '{print $4}'`
echo "appremainmem="$mem_user_free

# 11 获取交换分区总大小
mem_swap_total=`free | grep Swap | awk '{print $2}'`
echo "swapallsize="$mem_swap_total

# 12 获取剩余交换分区大小
mem_swap_free=`free | grep Swap | awk '{print $4}'`
echo "swapremainsize="$mem_swap_free

# 13 每秒向设备发起的写请求次数
disk_sda_ws=`iostat -kx | grep sda| awk '{print $5}'`
echo "queryiotime="$disk_sda_ws 

# 14 向设备发起的I/O请求队列长度平均值
disk_sda_avgqu_sz=`iostat -kx | grep sda| awk '{print $9}'`
echo "queryiolongth="$disk_sda_avgqu_sz

# 15 每次向设备发起的I/O请求平均时间
disk_sda_await=`iostat -kx | grep sda| awk '{print $10}'`
echo "iotimeavg="$disk_sda_await

# 16 向设备发起I/O请求的CPU时间百分占比
disk_sda_util=`iostat -kx | grep sda| awk '{print $12}'`
echo "iocpu="$disk_sda_util


