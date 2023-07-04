import os
import pathlib
import smtplib
from string import Template
from dotenv import load_dotenv   # type : ignore
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'template.html'

# Ddos do remetente e destinatario
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Config server SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('SENHA_EMAIL', '')

# Mensgem de texto
with open(CAMINHO_HTML, 'r',encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='Lucas')

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso')
