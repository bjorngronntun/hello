from flask import Flask
# Testing
app = Flask(__name__)

@app.route("/")
def index():
	return "Hello world"
	
if __name__ == '__main__':
	app.run(port = 5000, debug = True)
