# controler.py

from model import DataModel
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random


class SendBirthdayWhishesController:
    def __init__(self):
        self.model = DataModel()
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.email_address = "carlosmiguelromao@gmail.com"
        self.password = "fsem acem gxeq zxrq"

    def get_birthday_by_date(self, month, day):
        """"Retorna uma lista de nomes de pessoas que fazem aniversário em um dia e mês específicos"""
        # carrega o DataFrame
        if self.model.data is None:
            self.model.load_data()

        # filtra o DataFrame para encontrar correspondencia de mês e dia
        matches = self.model.data[(self.model.data["month"] == month) & (self.model.data["day"] == day)]

        #retorna list de nomes com correspondencias encontradas
        return list(matches[['name', 'email']].itertuples(index=False, name=None))

    def send_email(self, to_email, subject, body):
        "envia o email para o destinatario espeificado"
        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.email_address, self.password)
            server.sendmail(self.email_address, to_email, msg.as_string())
        print(f"Email enviado para {to_email}")

    def send_birthday_email(self, month, day):
        """envia email´s de aniversário com templates de rotação aleatoria"""
        names_and_emails = self.get_birthday_by_date(month, day)
        templates = self.model.load_template_paths()

        for name, email in names_and_emails:
            template_path = random.choice(templates)
            email_body = self.model.load_template_content(template_path, name)
            self.send_email(to_email=email,subject= "Feliz Aniversário!", body=email_body)







