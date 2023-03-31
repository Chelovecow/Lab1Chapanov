from flask import Flask, request, render_template

app = Flask(__name__)





@app.route('/')
def hell():
       user_data = {
       "family" : "Нагиев",
       "name" : "Дмитрий",
       "fname" : "Владимирович",
       "infa" : "Дед по отцу — Николай (Гулам) Нагиев, после Первой мировой войны со своими родителями — иранскими азербайджанцами бежал из Ирана в Ашхабад[1]. По дороге родители умерли от голода, и мальчик попал в туркменский детский дом, где ему дали фамилию Нагиев в честь людей,которые его туда привели, а также новое имя — Николай[2][3].",
       "inst" : "https://www.instagram.com/nagiev.universal/",
       "photo" : "https://s8.stc.all.kpcdn.net/putevoditel/serialy/wp-content/uploads/2019/07/20131130_gaf_rk39_008-467x697.jpg"
       }

       return render_template('hello.html', user=user_data)

app.run(debug=True)
