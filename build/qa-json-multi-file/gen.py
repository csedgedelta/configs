import random
import time
import datetime
import sys
import json
import os
import uuid


def gen_log():
    w1 = '''{
  "ip_address": "REMOTEIP",
  "user_agent": "AGENT",
  "level": "LEVEL",
  "timestamp": "TIMESTAMP",
  "request_method": "METHOD",
  "request_url": "REQUEST",
  "protocol": "HTTP/1.1",
  "status_code": "STATUS",
  "message": "DB connection successful",
  "response_size_bytes": BYTES
}'''
    methodList = [
       'GET',
       'GET',
       'GET',
       'POST',
       'POST',
       'UPDATE',
       'DELETE'
    ]
    requestList = [
       '/account',
       '/home',
       '/docs',
       '/account',
       '/order',
       '/'
    ]
    levelList = [
       'ERROR',
       'WARN',
       'INFO',
       'INFO',
       'INFO'
    ]
    statusCode = [
      '200',
      '301',
      '403',
      '404',
      '500'
    ]

    userAgent = [
       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
       'Mozilla/5.0 (Windows NT 7.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
       'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201'
    ]

    ipOctet1 = random.randint(1,255)
    ipOctet2 = random.randint(1,255)
    ipOctet3 = random.randint(1,255)
    ipOctet4 = random.randint(1,255)

    randomIP = "%s.%s.%s.%s" % (ipOctet1, ipOctet2, ipOctet3, ipOctet4)
    timeStamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    randomMethod = str(random.choice(methodList))
    randomStatus = str(random.choice(statusCode))
    randomBytes = str(random.randrange(300, 2000, 1))
    randomRequest = "http://site.com"+str(random.choice(requestList))
    randomLevel = str(random.choice(levelList))
    randomUserAgent = str(random.choice(userAgent))

    randomRequestLength = str(random.randrange(100, 4000, 1))
    randomRequestTime = str(round(random.uniform(20.000, 0.001), 3))
    randomConnectTime = str(random.randrange(100, 4000, 1))
    randomHeaderTime = str(random.randrange(100, 4000, 1))
    randomResponseTime = str(random.randrange(100, 4000, 1))
    n_w1 = w1

    if "REMOTEIP" in w1:
        n_w1 = n_w1.replace("REMOTEIP", randomIP)
    if "TIMESTAMP" in w1:
        n_w1 = n_w1.replace("TIMESTAMP", timeStamp)
    if "METHOD" in w1:
        n_w1 = n_w1.replace("METHOD", randomMethod)
    if "STATUS" in w1:
        n_w1 = n_w1.replace("STATUS", randomStatus)
    if "BYTES" in w1:
        n_w1 = n_w1.replace("BYTES", randomBytes)
    if "REQUEST" in w1:
        n_w1 = n_w1.replace("REQUEST", randomRequest)
    if "AGENT" in w1:
        n_w1 = n_w1.replace("AGENT", randomUserAgent)
    if "REQUESTLENGTH" in w1:
        n_w1 = n_w1.replace("REQUESTLENGTH", randomRequestLength)
    if "REQUESTTIME" in w1:
        n_w1 = n_w1.replace("REQUESTTIME", randomRequestTime)
    if "CONNECTTIME" in w1:
        n_w1 = n_w1.replace("CONNECTTIME", randomConnectTime)
    if "HEADERTIME" in w1:
        n_w1 = n_w1.replace("HEADERTIME", randomHeaderTime)
    if "RESPONSETIME" in w1:
        n_w1 = n_w1.replace("RESPONSETIME", randomResponseTime)
    if "LEVEL" in w1:
        n_w1 = n_w1.replace("LEVEL", randomLevel)

    return n_w1 #+ '\n'

def write_file(fo,mm):
  with open(fo, 'a') as f:
    f.write(mm)
    f.write('\n')

def main():
    file = "/log/" + str(uuid.uuid4())+ ".log"
    try:
      os.mkdir("/log")
    except FileExistsError:
      pass
    while True:
        msg = gen_log()
        write_file(file,msg)
        time.sleep(random.randint(1,10)/100)

main()
