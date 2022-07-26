server = "priem@urtisi.ru"
password = "uQ7AHaHF"
with open("to.txt", "r") as file:
    to = file.read().splitlines()
"""

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.ehlo()
#server.starttls()
server.login('priem@urtisi.ru', 'uQ7AHaHF')

server = "neltsker@gmail.com"
password = "bejcgcpuyejhxxeb"


subject = open("subject.txt", "r", encoding='utf-8').read()
text = open("text.txt", "r").read()
print(subject)
print(to)
print(text)
"""