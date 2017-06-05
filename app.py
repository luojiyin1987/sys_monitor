# coding=utf-8
import time
import MySQLdb as mysql

db = mysql.connect(user='web', passwd='web', db='r', host='localhost')
db.autocommit(True)
cur =db.cursor()

def getMem():
    with open('/proc/meminfo') as f :
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
        mem_use = total  - free - buffers - cache
        t =int(time.time())
        print mem_use/1024
        sql = 'insert into memory (memory, time) value (%s, %s)' %(mem_use/1024, t)
        cur.execute(sql)
while True:
    time.sleep(1)
    getMem()
