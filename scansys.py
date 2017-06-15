#!/usr/bin/python2

import   commands,time

ip_list=[]
# set your ipaddr according to your networkid
ipaddr="192.168.10."
# set range according to the ip range
for  i  in   range(121)[-1:]  :
	check=commands.getstatusoutput('ping  -c 1 192.168.10.'+str(i))
	if  check[0] ==  0  :
		ip_list.append(ipaddr+str(i))
	else  :
		print    "IP  Address  "+str(i) + " unreachable "


print   "scanned  IP    "
time.sleep(2)
print   ip_list
#  checking  cpu  cores 
cpu_ip=[]
cpu_check="lscpu   |  grep -i 'CPU(s):'   |   head  -1  |  cut -d:   -f2"
mem_check="cat /proc/meminfo | grep -i MemTotal:"

# remote login in systems and extracting information about  CPU core and size of HDD
for i   in  ip_list:
	ignore_exit_value, cpu_core=commands.getstatusoutput('sshpass -p "redhat" ssh root@'+i+" "+cpu_check)
	cpu=cpu_core.strip()
	
	ignore1,memory_value=commands.getstatusoutput('sshpass -p "redhat" ssh root@'+i+" "+mem_check)
	
	mem=memory_value.replace(" ","")
	cpu_ip.append("["+"IP="+i+" ,  "+"CPU="+cpu+" , "+"Memory="+mem+"]")

info_of_system=cpu_ip[:]
for info in info_of_system:
	print info	

	
	
