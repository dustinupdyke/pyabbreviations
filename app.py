import unirest

from flask import Flask
app = Flask(__name__)

app.debug = True

@app.route('/')
def hello_world():
	response = unirest.get("https://daxeel-abbreviations-v1.p.mashape.com/all/CS",
	  headers={
	    "X-Mashape-Key": "<key>"
	  }
	)    
	return response.raw_body

if __name__ == '__main__':
    app.run()