import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments, improve):##
    port = 2525 # mailtrap 
    smtp_server = 'smtp.mailtrap.io'
    login = 'e618dcc1411141'
    password = 'beb4495beac8a4'
    message = f"<h3> New Feedback Submission </h3> <ul> <li> Customer: {customer} </li> <li> Dealer: {dealer} </li> <li> Rating: {rating} </li> <li> Comments: {comments} </li> <li> Improve: {improve} </li> </ul> "

    sender_email = '217patrick.ck@gmail.com'
    receiver_email = 'ladislav.hric@yahoo.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Vertu Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())