from flask import Flask
from flask import jsonify
from flask import request
import const 
import requests

app = Flask(__name__)
print("Chat Server is ready...")
count = 0 #global score

@app.route('/get',methods=['POST'])
def showScore():
    print("[" + request.json['name'] +  "] HAS READ THE SCORE")
    return {'count':count}

@app.route('/add',methods=['POST'])
def addScore():
    global count
    oldScore = count
    count += int(request.json['number'])  

    print("[" + request.json['name'] + "] ADDED " + str(request.json['number']) + " TO SCORE (to " + str(count) + " from " + str(oldScore) + ")\n")

    return {'count':count}

if __name__ == '__main__':
    url = const.CHAT_SERVER_HOST
    host_ip = url.split('http://',1)[1]
    app.run(host=host_ip,port=const.CHAT_SERVER_PORT)