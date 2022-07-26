import smtplib

from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.ehlo()
#server.starttls()
server.login('priem@urtisi.ru', 'uQ7AHaHF')
# bejcgcpuyejhxxeb
#sent_from = config.server
#to = config.to
#subject = open("subject.txt", "r", encoding='utf-8').read()
#print(subject)
#text = open("text.txt", "r", encoding='utf-8').read()
#print(text)
sent_from = 'priem@urtisi.ru'
#to = config.to
#subject = open("subject.txt", "r", encoding='utf-8').read()
#print(subject)
#text = open("text.txt", "r", encoding='utf-8').read()
#print(text)
to = 'laa@urtisi.ru'
subject = 'test'
text = 'test from urtisi with mime'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, text)

msg = MIMEMultipart()
msg['From'] = sent_from
msg['To'] = to
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject

msg.attach(MIMEText(text))

with open('instruction.doc', "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name='instruction.doc'
        )
        # After the file is closed
part['Content-Disposition'] = 'attachment; filename="%s"' % basename('instruction.doc')
msg.attach(part)


server.sendmail(sent_from, to, msg.as_string())
server.close()



'''
        email_text = """\
        From: %s
        To: %s
        Subject: %s



        Добрый день %s, 15.06 у Вас пройдёт экзамен по мемоведению!
        Будьте добры, явитесь вовремя!
        Время экзамена: %s
        Логин для входа в систему: %s
        Пароль: %s
        Ссылка для подключения: %s
        """ % (sent_from, to, subject, FIO, time, login, password, link)
'''