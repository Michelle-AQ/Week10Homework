from Flask import Flask, Response, request

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return """
    <html>
    <head>
        <title>Sample - Flask routes</title>
    </head>
    <body>
        <h1>Name pages</h1>
        <p>Hello {}</p>
        
        <img src="daughter.jpg">
        
    </body>
    </html>
    """.format(name)

if __name__=='__main__':
    app.run(debug=True)