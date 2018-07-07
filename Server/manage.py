from flask import Flask
app = Flask(__name__)

@app.route('/')
def retravel_url():
    return 'https://res.cloudinary.com/hwhaxlz5c/image/upload/v1530998382/staticmap.png'

if __name__ == '__main__':
    app.run()