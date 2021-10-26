import smtplib
import ssl


sender = 'script1@gmail.com'
receivers = input('enter receiver email address: ')
message = input('enter your message: ')
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, 'sender password')
        server.sendmail(sender, receivers, message)
    print('Successfully sent mail')
except smtplib.SMTPException:
    print('Error:unable to send mail')
