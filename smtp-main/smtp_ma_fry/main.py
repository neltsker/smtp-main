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
        subject = 'УрТИСИ СибГУТИ. Экзамен. Направление 09.04.01 «Информатика и вычислительная техника»'

        email_text = """
Добрый день!
26.07.2022г. в 9:00, состоится междисциплинарный экзамен для поступления в магистратуру на направление 09.04.01 «Информатика и вычислительная техника».
Последовательность действий для участия в экзамене:
1) Подключиться в ZOOM для подтверждения личности и проверки рабочего места. 
Ссылка для входа: https://us05web.zoom.us/j/7155286980?pwd=dDBidWFUV0NVSlRhbkNnR3hKc0RvZz09 
Идентификатор конференции: 715 528 6980
Код доступа: zv4bbJ
Просьба быть готовым продемонстрировать сотруднику приемной комиссии в камеру удостоверение личности и подготовить рабочее место в соответствии с инструкцией. Ссылка для подключения будет доступна с 8.30.
Просьба перед подключением убедиться, что ваш аккаунт в zoom назван в соответствии с фамилией и именем в паспорте, например Иванов Иван. Допуск на консультацию будет осуществляться по экзаменационным спискам.

2) Подключиться к экзамену в ZOOM. 
Ссылка для входа на экзамен: https://us06web.zoom.us/j/89269198031?pwd=aE9RU3FTU1l0NVQ1cjdsQzN5V1hNUT09 
Идентификатор: 892 6919 8031
Код доступа: 505476

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