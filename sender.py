import smtplib
from os.path import basename
from email.message import EmailMessage

#info
sender_mail = "YOUR EMAIL ADRESS HERE"
sender_psw = "YOUR EMAIL APP PASSWORD HERE"
reciever = "TARGET EMAIL HERE"

def send(filenames):
    #from whom to whom
    msg = EmailMessage()
    msg['From'] = sender_mail
    msg['To'] = reciever
    msg['Subject'] = "Today's Weather Around the World"
    msg.set_content("You can find todays weather attached.")

    #add each pdf
    for file_path in filenames:
        with open(file_path, 'rb') as file:
            file_data = file.read()

        #add pdf to email
        msg.add_attachment(
            file_data,
            maintype='application',
            subtype='pdf',
            filename=basename(file_path)
        )

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_mail, sender_psw)
        server.send_message(msg)
