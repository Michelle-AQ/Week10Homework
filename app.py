from flask import Flask, Response, request, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    url = url_for('about_us')
    return """
    <html>
    <head>
        <title>Sample - Flask routes</title>
    </head>
    <body>
        <h1>Name pages</h1>
        <p>Hello {}</p>
        <a href= "{}">About Us</a>
        <img src="./daughter.jpg">
        
    </body>
    </html>
    """.format(name, url)

    
@app.route('/about_us')
def about_us():
    daughter_image_url = url_for('static', filename='daughter.jpg')
    return """
    <html>
    <head>
        <title>About Us</title>
    </head>
    <body>
        <h1>Michelle & Ellen</h1>
        <p>add text</p>
        <img src="{}" height='300' width='250' alt="my daughter">
    </body>
    </html>
    """.format(daughter_image_url)

if __name__=='__main__':
    app.run(debug=True)