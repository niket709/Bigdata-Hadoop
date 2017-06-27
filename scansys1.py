#!/usr/bin/python2

import   commands,time,ast

ip_list=["192.168.10.113"]
'''
# set your ipaddr according to your networkid
ipaddr="192.168.122."
# set range according to the ip range
for  i  in   range(108)[-1:]  :
	check=commands.getstatusoutput('ping  -c 1 192.168.122.'+str(i))
	if  check[0] ==  0  :
		ip_list.append(ipaddr+str(i))
	else  :
		print    "IP  Address  "+str(i) + " unreachable "


print   "scanned  IP    "
time.sleep(2)
print   ip_list
#  checking  cpu  cores '''
cpu_ip={}
mem_ip={}
cpu_check="lscpu   |  grep -i 'CPU(s):'   |   head  -1  |  cut -d:   -f2"
mem_check="cat /proc/meminfo | grep -i MemFree:"

# remote login in systems and extracting information about  CPU core and size of HDD
for i   in  ip_list:

		

################################################### M E M O R Y ##########################################################################
	ignore1,memory_value=commands.getstatusoutput('sshpass -p "redhat" ssh root@'+i+" "+mem_check)


	
	mem=memory_value.replace(" ","")
	mem_strip=mem.lstrip("MemFree:")
	mem_rstrip=mem_strip.rstrip("kB")
	

	x2="{"+"\'"+i+"\'"+":"+mem_rstrip+"}"
	print x2
	print type(x2)

	y2=ast.literal_eval(x2)
	print y2
	print type(y2)


	mem_ip.update(y2)
	print mem_ip

# sorting of memory

	sort_ip_mem=sorted(mem_ip,key=mem_ip.get,reverse=True)
	print sort_ip_mem
	
	name_node=sort_ip_mem[0]
	print name_node

	if name_node in sort_ip_mem:
		commands.getoutput("sshpass -p 'redhat' scp hdfs_conf_file root@"+name_node+":/etc/hadoop/")

		commands.getoutput("sshpass -p 'redhat' scp core_conf_file root@"+name_node+":/etc/hadoop/")

		

		h1="sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+name_node+" "+'\'sed -i "/<configuration>/r /etc/hadoop/hdfs_conf_file" /etc/hadoop/hdfs-site.xml\''

		h2="sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+name_node+" "+'\'sed -i "/<configuration>/r /etc/hadoop/core_conf_file" /etc/hadoop/core-site.xml\''

	
		
		commands.getoutput(h1)

		commands.getoutput(h2)
		commands.getoutput("sshpass -p 'redhat' ssh -o StrictHostKeyChecking=no root@"+name_node+" "+'\'sed -i \"s/ipaddr/'+name_node+"/"+"\" /etc/hadoop/core-site.xml\'")
	 




################################################## C P U ###############################################################################

	ignore_exit_value, cpu_core=commands.getstatusoutput('sshpass -p "q" ssh -o StrictHostKeyChecking=no root@'+i+" "+cpu_check)
	cpu=cpu_core.strip()
	
	x1="{"+"\'"+i+"\'"+":"+cpu+"}"
	print x1
	print type(x1)

	y1=ast.literal_eval(x1)
	print y1
	print type(y1)


	cpu_ip.update(y1)
	print cpu_ip
#sorting of cpu 
	sort_ip_cpu=sorted(cpu_ip,key=cpu_ip.get,reverse=True)
	print sort_ip_cpu

	job_tracker=sort_ip_cpu[0]

	if job_tracker in sort_ip_cpu:



