from flask import Flask

app = Flask(__name__)

@app.route('/')
def homething():
    return 'This server is currently being used as a YACLT repo. You can find the project <a href="https://github.com/Pixeleer/yaclt">here</a>'

if __name__ == "__main__":
    app.run(
        port=80
    )