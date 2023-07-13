from flask import Flask,render_template, request
from model2 import judge_text
from model3 import judge_percent


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



# @app.route("/judg",methods=['GET','POST'])
# def result():
#     if request.method == "GET":
#         return render_template('input.html')
#     elif request.method == "POST":
#         input_text = request.form['input_text']
#         # 文章診断
#         answer = judge_text(input_text)

#         return render_template('result2.html', result=answer)
@app.route("/judg",methods=['GET','POST'])
# %表示する方
def result():
    if request.method == "GET":
        return render_template('input.html')
    elif request.method == "POST":
        input_text = request.form['input_text']
        # 文章診断
        percent = judge_percent(input_text)
        if  percent[0][0]>0.5:
            answer="文系"
            percent=percent[0][0]*100
        elif percent[0][0]==0.5:
            answer="キメラ"
            percent="50"
        else :
            answer="理系"
            percent=percent[0][1]*100


        return render_template('result2.html', result=answer, per=percent)


if __name__ == "__main__":
    app.run()