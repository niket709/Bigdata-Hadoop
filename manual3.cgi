#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
#  here  setup  choice  will store 

choice=x.getvalue('select')



ip_list=["192.168.122.107","192.168.122.9","192.168.122.160"]

ip_listing=[]

cpu_check="lscpu   |  grep -i 'CPU(s):'   |   head  -1  |  cut -d:   -f2"
mem_check="cat /proc/meminfo | grep -i MemFree:"

for i in ip_list:
	
	check=commands.getstatusoutput('ping  -c 1 '+i)
	if  check[0] ==  0  :
	
		ip_listing.append(i)


if choice == "man":

# remote login in systems and extracting information about  CPU core and FREE memory size of RAM
	for i   in  ip_listing:
		ignore_exit_value, cpu_core=commands.getstatusoutput('sudo -i sshpass -p "q" ssh -o StrictHostKeyChecking=no root@'+i+" "+cpu_check)
		cpu=cpu_core.strip()
			
		ignore1,memory_value=commands.getstatusoutput('sudo -i sshpass -p "q" ssh root@'+i+" "+mem_check)
	
		mem=memory_value.replace(" ","")
		mem_strip=mem.lstrip("MemFree:")
		mem_rstrip=mem_strip.rstrip("kB")

	

		print  "<form  action='http://192.168.122.1/cgi-bin/hadoopproject/start4.cgi' method='POST'>"

		print  "<input  type='radio' name='setup' value="+i+" >"+i +"  " +"RAM= "+mem_strip +"  " +"CPU core= "+cpu+ "<br/>"

		print   "<input  type='submit' value='send'>"
		print    "</form>"
else  :
	print   "bad  options"







