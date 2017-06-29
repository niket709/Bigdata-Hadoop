#!/usr/bin/python2

import   commands,time,ast

ip_list=["192.168.122.107","192.168.122.9","192.168.122.160"]

ip_listing=[]

for i in ip_list:
	
	check=commands.getstatusoutput('ping  -c 1 '+i)
	if  check[0] ==  0  :
	
		ip_listing.append(i)
print ip_listing		


cpu_core_ip={}
hdd_ip={}
cpu_check="lscpu   |  grep -i 'CPU(s):'   |   head  -1  |  cut -d:   -f2"
mem_check="cat /proc/meminfo | grep -i MemFree:"

# remote login in systems and extracting information about  CPU core and FREE memory size of HDD
for i   in  ip_list:
	ignore_exit_value, cpu_core=commands.getstatusoutput('sshpass -p "q" ssh -o StrictHostKeyChecking=no root@'+i+" "+cpu_check)
	cpu=cpu_core.strip()
		
	ignore1,memory_value=commands.getstatusoutput('sshpass -p "q" ssh root@'+i+" "+mem_check)
	
	mem=memory_value.replace(" ","")
	mem_strip=mem.lstrip("MemFree:")
	mem_rstrip=mem_strip.rstrip("kB")
	

	x1="{"+"\'"+i+"\'"+":"+mem_rstrip+"}"
	

	y1=ast.literal_eval(x1)


	hdd_ip.update(y1)


	sort_hdd_ip=sorted(hdd_ip,key=hdd_ip.get,reverse=True)

############################################################### NAMENODE ############################################################################

namenode=sort_hdd_ip[0]

if namenode in sort_hdd_ip:
	commands.getoutput("sshpass -p 'q' scp /root/Desktop/hdfs_conf_file root@"+namenode+":/etc/hadoop/")

	commands.getoutput("sshpass -p 'q' scp /root/Desktop/core_conf_file root@"+namenode+":/etc/hadoop/")

		

	h1="sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i "/<configuration>/r /etc/hadoop/hdfs_conf_file" /etc/hadoop/hdfs-site.xml\''

	h2="sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i "/<configuration>/r /etc/hadoop/core_conf_file" /etc/hadoop/core-site.xml\''

	
		
	commands.getoutput(h1)

	commands.getoutput(h2)
	
	commands.getoutput("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i \"s/ipaddr/'+namenode+"/"+"\" /etc/hadoop/core-site.xml\'")
	 



############################################################### X X X X X X##########################################################################



