import csv
import smtplib
from email.mime.text import MIMEText


class Mailer(object):
    """Handle the details of sending a message to users"""
    @staticmethod
    def send(sender, recipients, subject, message):

        # implementation of data fetching
        # get user detail
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = [recipients]

        # send email
        s = smtplib.SMTP('localhost')
        s.send_message(recipients)
        s.quit()


if __name__ == "__main__":
    with open("user.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        users = [row for row in reader]

    mailer = Mailer()
    mailer.send(
        sender="me@example.com",
        recipients=[x["email"] for x in users],
        subject="message", message="allo"
    )


