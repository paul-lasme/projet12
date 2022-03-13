from flask import Flask,jsonify
from datetime import datetime
import os
my_port = int(os.environ.get("PORT", 8030))
app = Flask(__name__)
visit_cnt=0
@app.route('/')
def hello_world():
    global visit_cnt
    visit_cnt+=1
    return jsonify(message='Congrats! you have deployed your first web service',time=datetime.now(),totoal_visit_count=visit_cnt)
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=my_port)