import unirest
from flask import Flask
from flask import request
app = Flask(__name__)

app.debug = True

@app.route('/')
def hello_world():
	response = unirest.get("https://daxeel-abbreviations-v1.p.mashape.com/all/" + request.args.get('a'),
	  headers={
	    "X-Mashape-Key": "key"
	  }
	)    
	return response.raw_body

if __name__ == '__main__':
    app.run()