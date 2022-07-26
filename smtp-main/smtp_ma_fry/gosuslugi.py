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
        server.login(config.server, config.password)
        sent_from = config.server
        subject = 'Приемная комиссия УрТИСИ СибГУТИ'

        email_text = """
Добрый день. Это приёмная комиссия Института связи (УрТИСИ СибГУТИ), г. Екатеринбург.

Вы подали к нам заявление на поступление через личный кабинет госуслуг и сервис приема.

Документы, которые Вы указали в заявлении, пока не подтверждаются. До тех пор пока они остаются в статусе "не подтвержден", мы не можем допустить Вас к конкурсу и зарегистрировать в нашей  электронной среде.

Для ускорения процесса подтверждения вашего заявления просим прислать скан пакета документов(паспорт с пропиской, СНИЛС, аттестат с приложением, подтверждение льгот и достижений если таковые были указаны в заявлении) на почту priem@urtisi.ru.

Обращаем ваше внимание, что СЕГОДНЯ (25 июля) ПОСЛЕДНИЙ ДЕНЬ приема заявлений для очной формы обучения, прием оригиналов и согласий на зачисление заканчивается 3 августа.
""" 

        msg = MIMEMultipart()
        msg['From'] = sent_from
        msg['To'] = to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(email_text))

        
        # with open('instruction.doc', "rb") as fil:
        #     part = MIMEApplication(
        #         fil.read(),
        #         Name='instruction.doc'
        #         )
        #         # After the file is closed
        #part['Content-Disposition'] = 'attachment; filename="%s"' % basename('instruction.doc')
        #msg.attach(part)

        server.sendmail(sent_from, to, msg.as_string())
        server.close()
        print('Письмо отправлено: ', to)
        time.sleep(1)