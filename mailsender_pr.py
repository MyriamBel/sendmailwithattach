# -*- coding: utf-8 -*-

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

HOST = "SMTP.yandex.ru"
SUBJECT = "Test email"
TO = ["xxx", ]
FROM = "xxx"
text = "Python 3.4 rules them all!"
password = "xxx"

def send_email_with_attach(host, FROM, SUBJECT, send_to, path_to_file, password):

    header = 'Content-Disposition', 'attachment; filename="%s"' % path_to_file

    msg = MIMEMultipart()
    msg["From"] = FROM
    msg["Subject"] = SUBJECT
    msg["Date"] = formatdate(localtime=True)
    msg["To"] = send_to
    msg.attach(MIMEText("This e-mail contains an attach"))

    attachment = MIMEBase('application', "octet-stream")
    try:
        with open(path_to_file, "rb") as fa:
            data = fa.read()

        attachment = MIMEBase('data', "octet-stream")
        attachment.set_payload(data)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename=path_to_file)
        msg.attach(attachment)
    except IOError:
        msg = "Error opening attachment file %s" % path_to_file
        print(msg)
        sys.exit(1)

    server = smtplib.SMTP_SSL(host)
    server.login(user=FROM, password=password)
    server.sendmail(FROM, send_to, msg.as_string())
    server.quit()

i = TO.__len__() - 1
while i >= 0:
    print(TO[i])
    path_to_file = "РЕКВИЗИТЫ.docx"
    send_email_with_attach(host=HOST, FROM=FROM, SUBJECT=SUBJECT, send_to=TO[i], path_to_file=path_to_file,
                           password=password)
    i -= 1