#!usr/bin/python

import cgi
form = cgi.FieldStorage()
with open ('fileToWrite.txt','w') as fileOutput:
    fileOutput.write(form.getValue('firstname'))
    fileOutput.write(form.getValue('lastname'))
