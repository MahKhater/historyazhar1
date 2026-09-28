from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "منصة سر التفوق تعمل بنجاح!"

if __name__ == '__main__':
    app.run()
