import random
import time
import datetime
import sys
import json
import os
import uuid


def gen_log():
    w1 = '''TIMESTAMP LEVEL [http-nio-8080-exec-8] classOne: Index out of range
java.lang.StringIndexOutOfBoundsException: String index out of range: 18
	at java.lang.String.charAt(String.java:658)
	at com.example.app.loggingApp.classOne.getResult(classOne.java:15)
	at com.example.app.loggingApp.AppController.tester(AppController.java:27)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:190)
	at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:138)'''

    levelList = [
       'ERROR',
       'WARN',
       'INFO',
       'INFO',
       'INFO'
    ]
    
    timeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")
    randomLevel = str(random.choice(levelList))
   
    n_w1 = w1

    if "LEVEL" in w1:
        n_w1 = n_w1.replace("LEVEL", randomLevel)
    if "TIMESTAMP" in w1:
        n_w1 = n_w1.replace("TIMESTAMP", timeStamp)
    

    return n_w1 #+ '\n'

def write_file(fo,mm):
  with open(fo, 'a') as f:
    f.write(mm)
    f.write('\n')

def main():
    file = "/log/test/" + str(uuid.uuid4())+ ".log"
    try:
       os.mkdirs("/log/test")
    except FileExistsError:
      pass
    while True:
        msg = gen_log()
        write_file(file,msg)
        time.sleep(random.randint(1,10)/100)

main()
