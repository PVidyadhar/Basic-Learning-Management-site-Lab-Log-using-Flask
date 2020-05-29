from flask import Flask,render_template,request, send_file,redirect,session

from live_classifier1 import get_sentiment

app=Flask(__name__)

@app.route("/")

def homepage():
	return render_template('home.html')


@app.route("/res",methods=["POST"])
def result():
	text=request.form['text']
	cat,conf=get_sentiment(text)
	return render_template('ans.html',cat=cat)

#ostundi kadha ra
#web page la oka form petkoni anla nunchi text theskoni ee function ki pass chei



if __name__== '__main__':
	app.run (debug = True)
