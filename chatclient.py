
from flask import Flask
from flask import jsonify
from flask import request
import sys
import const 
import requests
import threading
import socket

me = str(sys.argv[1]) # User's name (as registered in the registry. E.g., user1, user2, ...)

def showScore():
    data = {
        'name':me,
    }
    res = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/get', json = data)
    print("THE CURRENT SCORE IS " + str(res.json()['count'])+"\n")

def addScore():
    showScore()
    number = input("ENTER A POSITIVE NUMBER:\n")
    if(int(number)<0):
        print("ERROR: NEGATIVE NUMBER")
    else:
        data = {
            'name':me,
            'number':number,
        }
        res = requests.post(const.CHAT_SERVER_HOST+":"+str(const.CHAT_SERVER_PORT)+'/add', json = data)
        print("YOU ADDED " + str(number) + " TO THE SCORE ("+ str(res.json()['count'])+")\n")


if __name__ == '__main__':
    while True:
        reply = input("Enter (s) to SEE or (a) to ADD to the current score: \n")
        if (reply == 'a'):
            addScore()
        elif(reply == 's'):
            showScore()
