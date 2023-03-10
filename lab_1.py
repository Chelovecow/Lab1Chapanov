from flask import Flask


app = Flask(__name__)



@app.route("/silka/") 
def page_silka(): 
    return "<a href='www.google.com'>Ссыка</a>"


@app.route('/haha//<int:chislo>')
def haha(chislo):
    print(chislo)
    print(type(chislo))
    return f'<h1>Вы написали число {chislo} в URL строке</hl>'







app.run(host='127.0.0.21', port=5000)
