###Intergrate HTML with Flask
### HTTP verb GET and POST 
from flask import Flask,redirect,url_for,render_template,request
### WSGI application
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/pas/<int:score>")
def pas(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template("result.html",result=res)

@app.route("/fail/<int:score>")
def fail(score):
    return "the person is failed with the score : " +str(score)

@app.route("/result/<int:marks>")
def results(marks):
    result=""
    if marks<50:
        result="fail"
    else:
        result="pas"
    return redirect(url_for(result,score=marks))

###Result checker HTML page 
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        maths=float(request.form["maths"])
        c=float(request.form["c"])
        data_science=float(request.form["datascience"])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for("pas",score=total_score))

if __name__=="__main__":
    app.run(debug=True)

