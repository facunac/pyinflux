#!/usr/bin/env python
import sys
import getopt
from influxdb import client as influxdb

ihost='54.207.3.29'
iport=8086
iusername='clima'
ipassword='pangirosa'
idatabase='weather'
ipres=-100
itemp=-100

argv = sys.argv[1:]
try:
  opts,args = getopt.getopt(argv,'h:k:s:d:u:p:t:a:',['help', 'port=','host=','database=','user=','password=','temp=','presion='])
except getopt.GetoptError as err:
  sys.exit(2)
for opt, arg in opts:
  if (opt in ('-h','--help')):
    print 'Usage :  -h --help esta ayuda'
    print '         -k --port= puerto]'
    print '         -s --host= base de datos'
    print '         -d --database= base de datos'
    print '         -u --user= base de datos'
    print '         -p --password= base de datos'
    print '         -t --temp temperatura'
    print '         -a --presion presion'

  if (opt in ('-s','--host')):
    ihost=arg
  if (opt in ('-d','--database')):
    idatabase=arg
  if (opt in ('-u','--user')):
    iusername=arg
  if (opt in ('-p','--password')):
    ipassword=arg
  if (opt in ('-k','--port')):
    iport=arg
  if (opt in ('-t','--temp')):
    itemp=arg
  if (opt in ('-a','--presion')):
    ipres=arg

if ((ipres == -100) and (itemp == -100)):
  print "Sin datos.."
  sys.exit(-1)

db = influxdb.InfluxDBClient(ihost, iport, iusername, ipassword, idatabase)

data = [{
   "name":"clima01",
   "columns":["presion", "temperatura"],
   "points":[
      [ipres,itemp]
   ]
}]
print data
db.write_points(data)

