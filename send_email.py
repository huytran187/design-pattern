import smtplib
from email.mime.text import MIMEText


def send_email(sender, recipients, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(recipients)

    mail_sender = smtplib.SMTP('localhost')
    mail_sender.send_message(msg)
    mail_sender.quit()


if __name__ == "__main__":
    send_email(
        sender="me@example.com",
        recipients=["peter@example.com", "paul@example.com", "john@example.com"],
        subject="message",
        message="allo"
    )

