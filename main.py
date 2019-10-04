from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = '''
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
        <!-- create your form here -->
        <form action="" method="post">
            <label for="rot">Rotate By:</label>
            <input type="text" name="rot" value="0" >
        <textarea name="text" ></textarea>
        </body>
    </html>

'''

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    the_rotate = int(request.form['rot'])
    the_text = request.form['text']
    encrypted_text = rotate_string(the_text, the_rotate)
    return encrypted_text
        

app.run()

