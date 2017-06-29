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


	
	x2="{"+"\'"+i+"\'"+":"+cpu+"}"
	

	y2=ast.literal_eval(x2)


	cpu_core_ip.update(y2)

	sort_cpu_core_ip=sorted(cpu_core_ip,key=cpu_core_ip.get,reverse=True)


print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
print "	CPU CORE ALONG WITH IP:-"
print  cpu_core_ip
print "________________________________________________________"

print "________________________________________________________"

print "SORTED CPU CORE IP"
print sort_cpu_core_ip

print "- - - - - - - - - - - - - - - - - - - - - - - - -  - - - "
print ""
print "FREE MEMORY ALONG WITH IP:-"
print hdd_ip

print "__________________________________________________________"

print "__________________________________________________________ "

print "SORTED MEMORY IP"
print sort_hdd_ip


