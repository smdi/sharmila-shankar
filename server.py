from flask import Flask , render_template , redirect ,  url_for , flash , session


app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def intro() :
    return render_template('base.html')    


if __name__ == '__main__':
    from os import environ
    app.run(port=environ.get("PORT", 5000), debug = True)
