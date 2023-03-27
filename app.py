from flask import Flask, Response, url_for, redirect

app = Flask(__name__)

# basic hello all page
@app.route('/hello/<name>')
def hello(name):
    url = url_for('about_us')
    return """
    <html>
    <head>
        <title>About Us</title>
    </head>
    <body>
        <h1>Name pages</h1>
        <p>Hello {}</p>
        <a href= "{}">About Us</a>     
    </body>
    </html>
    """.format(name, url)

# basic About Us page
@app.route('/about_us')
def about_us():
    hi_image_url = url_for('static', filename='images/hi.png')
    ellen_url = url_for('about_me_ellen')
    michelle_url = url_for('about_me_michelle')
    return """
    <html>
    <head>
        <title>About Us</title>
    </head>
    <body>
        <h1>Michelle & Ellen</h1>
        <p>Noob programmers but working hard to keep up</p>
        <img src="{}" height='300' width='250' alt="hi"> 
        <br>
        
        <a href= "{}">About me - Ellen</a>     
        <br>
        <a href= "{}">About me - Michelle</a>     
               
    </body>
    </html>
    """.format(hi_image_url, ellen_url, michelle_url)

# code to return a calculation based on a given number
@app.route('/maths/<int:num>')
def maths(num):
    return f"The area of your square is {num*2:,.01f} m\u00b2"

# code to return a sentence, capitalising the given word
@app.route('/faves/<word>')
def favourites(word):
    return Response(f"Hi, Your favourite game is {word.capitalize()}, I am sure that I like that too.", mimetype='text/plain')

# Code to convert the temperature
@app.route('/weather/<int:celsius>')
def weather(celsius):
    fahrenheit = celsius*(9/5)+32
    return Response(f"The weather today is {celsius:,.01f}\u00B0C, that is {fahrenheit:,.01f}\u00B0F")

# Ellen's About Me Pages
@app.route('/about_me_ellen')
def about_me_ellen():
    stylesheet_url = url_for('static', filename='styles/styles.css')
    daughter_image_url = url_for('static', filename='images/daughter.jpg')
    son_video_url = url_for('static', filename='images/son.mp4')
    dog_url = url_for('dog')
    return """
        <html>
        <head>
            <link rel="stylesheet" href="{}">
            <title>About Me - Ellen</title>
        </head>
        <body>
            <h1>Ellen</h1>
            <p>I am a trainee programmer, working hard to achieve an opportunity with Sky.
            <br>
            I am married with 2 children and a dog.
            <br>
            <img src="{}" height='300' width='250' alt="my daughter">
            <br>
            <video width="320" height="240" controls>
                <source src="{}" type="video/mp4">
                The bearded experts; young and old.
            </video>
            <br>
            <a href="{}">See my dog</a>
            </p>
        </body>
        </html>
        """.format(stylesheet_url, daughter_image_url, son_video_url, dog_url)

@app.route('/dog')
def dog():
    style_url = url_for('static', filename='styles/styles.css')
    dog_image_url = url_for('static', filename='images/dog.jpg')
    return """
        <html>
        <head>
            <link rel="stylesheet" href="{}">
            <title>Genie</title>
        </head>
        <body>
            <h1>My dog Genie</h1>
            <p>Genie is 6 years old.
            <br>
            <img src="{}" height='300' width='350' alt="my dog">
            </p>
        </body>
        </html>
        """.format(style_url, dog_image_url)


# using redirect and url_for
@app.route('/hello_everyone/<name>')
def hello_everyone(name):
    return """
        <html>
        <head>
            <title>Hello</title>
        </head>
        <body>
            <h1>Hello {}</h1>
        </body>
        </html>
        """.format(name.capitalize())

@app.route('/victoria')
def victoria():
    thanks_url = url_for('static', filename='images/thankyou.jpg')
    return """
        <html>
        <head>
            <title>Hello Victoria</title>
        </head>
        <body>
            <h1>Hello and Thank you to Victoria</h1>
            <img src="{}", height=500, width=650>
        </body>
        </html>
        """.format(thanks_url)

@app.route('/hiya/<name>')
def hello_people(name):
   if name =='victoria':
      return redirect(url_for('victoria'))
   elif name == 'ellen':
      return redirect(url_for('about_me_ellen'))
   elif name == 'michelle':
       return redirect(url_for('about_me_michelle'))
   else:
      return redirect(url_for('hello_everyone', name = name))


# Michelle's About Me Page
@app.route('/about_me_michelle')
def about_me_michelle():
    stylesheet_url = url_for('static', filename='styles/styles2.css')
    michelle_image_url = url_for('static', filename='images/parispic-mq.jpg')
    return """
        <html>
        <head>
            <link rel="stylesheet" href="{}">
            <title>About Me - Michelle</title>
        </head>
        <body>
            <h1>Michelle</h1>
            <p>I currently work in healthcare and education, but I am also currently a trainee in the exciting world of Software Engineering (with Sky).
            <br>
            <br>
            I currently live in London, UK, where I was born and raised.
            <br>
            <br>
            <img src="{}" height='400' width='350' alt="parispic-mq.jpg">
            <br>
            Me in Paris, France.
            <br>
            <br>
            <br>
            One of my favourite songs!
            <br>
            <iframe width="420" height="345" src="https://youtube.com/embed/LQekjdbMC6U">
</iframe>
            
            </p>
        </body>
        </html>
        """.format(stylesheet_url, michelle_image_url)




if __name__=='__main__':
    app.run(debug=True)
    