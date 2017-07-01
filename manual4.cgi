#!/usr/bin/python

import  cgi,cgitb,os,time,commands,sys
cgitb.enable()
print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
#  here  setup  choice  will store 

choice=x.getvalue('setup')

print  "<form  action='http://192.168.122.1/cgi-bin/hadoopproject/start5.cgi' method='POST'>"

print  "<input  type='radio' name='nnip' checked='checked' value="+choice+" >"+choice
print "</br>"

print "<input  type=\"text\" name=\"dirname\" placeholder=\"enter directory name here\"  >   <br/>"
print   "<input  type='submit' value='send'>"
print "</form >"

