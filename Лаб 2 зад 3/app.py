import json
from flask import Flask, request, render_template

app = Flask(__name__)

def json_read():
       with open('capitals.json' , encoding='UTF=8') as my_file:
              user= json.load(my_file)
       return user




@app.route('/')
def hell():
       duser=json_read()
       return render_template('hello.html', user=duser)

app.run(debug=True)
