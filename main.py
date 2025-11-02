from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

from dotenv import load_dotenv
load_dotenv()

password = os.getenv("PASSWORD")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
msg = MIMEMultipart()

msg["From"] = "dmitryvah029@yandex.ru"
msg["To"] = "dmitryvah029@yandex.ru"
msg["Subject"] = "Мои занятия програмированием"
process = ['Основы Python', 'GitHub', 'API']
completed = ['Командная строка', 'Введение в Python', 'Введение в JS']

time = "3 месяца"
letter = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. "
"В процессе я выполнил модули: {completed}! Сейчас я работаю над модулями {process}. "
"Обучение мне нравится, я получил море знаний!" 
if not completed: 
    letter = f"Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. "
    "Сейчас я работаю над модулями {process}. "
    "Пока что я улучшаю свои навыки и узнаю много нового!"
    
msg.attach(MIMEText(letter, "plain"))
server.login("dmitryvah029@yandex.ru", password)
server.sendmail(msg["From"], msg["To"], msg.as_string())
server.quit()
