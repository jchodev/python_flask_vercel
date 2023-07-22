from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def home():
	return "HELLO from vercel use flask"

@app.route("/page2")
def page2():
	return "依個係第二頁作測試, this is page2 for testing"

@app.route('/example', methods=['POST'])
def example():
    if request.method == 'POST':
        data = request.form['data']
        print(data)
        return f"The data you sent is: {data}"

@app.route("/about")
def about():
	return "HELLO about"