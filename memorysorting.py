#!/usr/bin/python2

import   commands,time,ast

ip_list=["192.168.122.107","192.168.122.9","192.168.122.160"]

ip_listing=[]

for i in ip_list:
	
	check=commands.getstatusoutput('ping  -c 1 '+i)
	if  check[0] ==  0  :
	
		ip_listing.append(i)
print ip_listing		



cpu_ip={}
cpu_check="lscpu   |  grep -i 'CPU(s):'   |   head  -1  |  cut -d:   -f2"
mem_check="cat /proc/meminfo | grep -i MemFree:"

# remote login in systems and extracting information about  CPU core and size of HDD
for i   in  ip_list:
	ignore_exit_value, cpu_core=commands.getstatusoutput('sshpass -p "q" ssh -o StrictHostKeyChecking=no root@'+i+" "+cpu_check)
	cpu=cpu_core.strip()
		
	ignore1,memory_value=commands.getstatusoutput('sshpass -p "q" ssh root@'+i+" "+mem_check)
	
	mem=memory_value.replace(" ","")
	mem_strip=mem.lstrip("MemFree:")
	mem_rstrip=mem_strip.rstrip("kB")
	

	x="{"+"\'"+i+"\'"+":"+mem_rstrip+"}"
	

	y=ast.literal_eval(x)


	cpu_ip.update(y)


	sort_ip=sorted(cpu_ip,key=cpu_ip.get,reverse=True)


print cpu_ip

print sort_ip
