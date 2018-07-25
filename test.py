import os
from flask import Flask, request, jsonify
#from test import microdust_1


app = Flask(__name__)



@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons":["대화하기","도움말"]
    }
    return jsonify(dataSend)

@app.route('/message',methods = ['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"따라하기":
        dataSend = {
            "message":{
                "text" : "점머먹 명령어 목록 \n1. 도움말\n2. 안녕\n3.저기"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message" : {
                "text" : "곧 점머먹 개장합니다."
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message" : {
                "text": "안녕하십니까"
            }
        }
    elif u"저기" in content:
        dataSend = {
            "message" : {
                "text" : "꺼져 병신아"
            }
        }
    else:
        dataSend = {
            "message" : {
                "text" : content
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run()
