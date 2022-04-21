from config import app, mail


@app.route("/send_mail")
def index():
    #some code


if __name__ == '__main__':
    app.run(debug=True)
