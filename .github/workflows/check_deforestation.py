import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_alert(to_email, alert_message):
    from_email = 'your_gmail@gmail.com'
    password = 'your_gmail_password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Deforestation Alert'

    msg.attach(MIMEText(alert_message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Example usage
send_email_alert('recipient_email@example.com', 'Deforestation detected in the specified area.')
