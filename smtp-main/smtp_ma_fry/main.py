import smtplib
import config


from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


import time

class rass():
    def sendMail(self, to):
        server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
        server.ehlo()
        #server.starttls()
        server.login(config.server, config.password)
        #server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.ehlo()
        #server.starttls()
        #server.login(config.server, config.password)
        # bejcgcpuyejhxxeb

        sent_from = config.server
        #to = config.to
        #subject = open("subject.txt", "r", encoding='utf-8').read()
        #print(subject)
        #text = open("text.txt", "r", encoding='utf-8').read()
        #print(text)
        subject = 'УрТИСИ СибГУТИ. Консультация Математика и ЭВМ'

        email_text = """
Добрый день!
1.08.2022г. в 15:00 состоится онлайн консультация по подготовке к сдаче вступительных испытаний «Математика» и «Элементы высшей математики»
Ссылка для входа на консультацию: https://us06web.zoom.us/j/83968785158?pwd=VUpxd3QvUzdsdDJ1VHhJWncrL3A3Zz09 
Идентификатор: 839 6878 5158
Код доступа: 954214

Примерный вариант экзаменационного билета «Математика» размещен на сайте https://uisi.ru/uisi/abiturient/2022/bak_mag/Mat_primer_2022.pdf
Примерный вариант экзаменационного билета «Элементы высшей математики» размещен на сайте 
https://uisi.ru/uisi/abiturient/2022/bak_mag/obrazec_ekz_evm.pdf 
Просьба перед подключением убедиться, что ваш аккаунт в zoom назван в соответствии с фамилией и именем в паспорте, например Иванов Иван. Допуск на консультацию будет осуществляться по экзаменационным спискам.

Экзамен по Математике состоится 2.08.2022 г. В 9.00.
Экзамен по Элементам высшей математике состоится 2.08.2022 г. В 14.00.

Просьба подтвердить получение письма.
""" 

        msg = MIMEMultipart()
        msg['From'] = sent_from
        msg['To'] = to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(email_text))

        
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
        print('Письмо отправлено: ', to)
        time.sleep(1)