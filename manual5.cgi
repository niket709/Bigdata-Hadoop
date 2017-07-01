#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""
x=cgi.FieldStorage()
nn_ip=x.getvalue("nnip")
directory=x.getvalue("dirname")

commands.getoutput("sudo -i touch /var/www/cgi-bin/hdfs_conf_file")
commands.getoutput("sudo -i chmod 777 /var/www/cgi-bin/hdfs_conf_file")

file1=open("/var/www/cgi-bin/hdfs_conf_file","w")
s="<property>\n<name>dfs.name.dir</name>\n<value>"+"/"+directory+"</value>\n</property>"
file1.write(s)
file1.close()

commands.getoutput("sudo -i touch /var/www/cgi-bin/core_conf_file")
commands.getoutput("sudo -i chmod 777 /var/www/cgi-bin/core_conf_file")


file2=open("/var/www/cgi-bin/core_conf_file","w")
s="<property>\n<name>fs.default.name</name>\n<value>hdfs://ipaddr:10001</value>\n</property>"
file2.write(s)
file2.close()

namenode=nn_ip


commands.getoutput("sudo -i sshpass -p 'q' scp /var/www/cgi-bin/hdfs_conf_file root@"+namenode+":/etc/hadoop/")

commands.getoutput("sudo -i sshpass -p 'q' scp /var/www/cgi-bin/core_conf_file root@"+namenode+":/etc/hadoop/")

		

h1="sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i "/<configuration>/r /etc/hadoop/hdfs_conf_file" /etc/hadoop/hdfs-site.xml\''

h2="sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i "/<configuration>/r /etc/hadoop/core_conf_file" /etc/hadoop/core-site.xml\''

	
		
commands.getoutput(h1)

commands.getoutput(h2)
	
commands.getoutput("sudo -i sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@"+namenode+" "+'\'sed -i \"s/ipaddr/'+namenode+"/"+"\" /etc/hadoop/core-site.xml\'")

time.sleep(2)

print "done"


