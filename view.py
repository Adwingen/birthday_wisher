# view.py

from controller import SendBirthdayWhishesController

class BirthdayView:
    def __init__(self):
        self.controller = SendBirthdayWhishesController()

    def display_birthday(self, month, day):
        names = self.controller.get_birthday_by_date(month, day)

        if names:
            print(f"Pessoas que fazem aniversario em {day}/{month}")
            for name in names:
                print(f"- {name}")
            else:
                print(f"Nenhuma pessoa faz aniversario em {day}/{month}.")

    def send_birthday_emails(self, month, day):
        "dispara o envio dos emails e exibe o status"
        print(f"Enviar email para os aniversariantes em {day}/{month}")
        self.controller.send_birthday_email(month, day)
        print(f"Envio de email de aniversario concluidos")

