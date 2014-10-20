# -*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
import MySQLdb
from vigen import Vigenere
from settings import DB_HOST, DB_USER, DB_PASSWD, PORT

# 访问数据库获取新的编号值
def getNum():
    conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, 
        db="honeycomb", charset="utf8")    
    cursor = conn.cursor()
    # 关闭自动提交
    sql = 'set autocommit=0;'
    cursor.execute(sql)  
    
    # 使用行锁
    sql = 'select * from number where id = 1 for update'
    cursor.execute(sql)  
    record = cursor.fetchone()
    #print record
    new_number = int(record[1]) + 1
    
    sql = "update number set serial_number=%s"     
    param = [new_number]      
    cursor.execute(sql,param) 
    
    #提交      
    conn.commit()  
    #关闭
    cursor.close()       
    conn.close()   
    return new_number

# 访问数据库获取监控agent的最新版本号
def get_latest_version():
    conn = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, 
        db="honeycomb", charset="utf8")    
    cursor = conn.cursor()
    sql = 'select * from version'
    cursor.execute(sql)  
    record = cursor.fetchone()
    
    #提交      
    conn.commit()  
    #关闭      
    conn.close()   
    return record[0]
    


# 对编号用Vigenere算法加密,并加上标示,使其更美观
def decorate(num, limit):
    num = str(num)
    cleartext = num
    for i in range(limit - len(num)):
        cleartext = '0' + cleartext
    v = Vigenere(table='0152893647', key='Studyhardandmakeprogresseveryday')
    return 'GD' + v.encrypt(cleartext)
    
# 主机编号
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        num = getNum()
        sn = decorate(num, 10)
        self.write(sn)
        
# 返回当前最新的版本
class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(get_latest_version())
        
application = tornado.web.Application([
    (r"/number", MainHandler),
    (r"/version", VersionHandler),
])

if __name__ == "__main__":
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
    print 'honeycomb server is start.'	



