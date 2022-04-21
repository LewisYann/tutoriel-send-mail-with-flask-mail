from mailbox import Message

from config import app, mail


@app.route("/send_mail")
def index():
    mail_message = Message(
        "Hi ! Don't forget to follow me for more article!",
        sender='your_mail@gmail.com',
        recipients=['to@gmail.com'])
    mail_message.body = "This is a test"
    mail.send(mail_message)


if __name__ == '__main__':
    app.run(debug=True)
