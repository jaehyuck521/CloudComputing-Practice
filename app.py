from flask import Flask
app=Flask(__name__)
@app.route("/ping")
def test():
    return 'This is Cloud computing Practice'

if __name__ == '__main__':
    app.run()

