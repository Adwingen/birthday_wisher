# model.py

import pandas as pd


class DataModel:
    def __init__(self):
        self.data_file_birthdays = "birthdays.csv"
        self.data = None
        self.templates = ["letter_templates/letter_1.txt",
                          "letter_templates/letter_2.txt",
                          "letter_templates/letter_3.txt"]


    def load_data(self):
        """carrega o DataFrame diretamente a partir do CSV."""
        try:
            self.data = pd.read_csv(self.data_file_birthdays).dropna()
        except FileNotFoundError:
            print(f"Arquivo {self.data_file_birthdays} não encontrado!")
        except pd.errors.EmptyDataError:
            print(f"Arquivo {self.data_file_birthdays} está vazio!")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar o ficheiro {e}")

    def load_template_paths(self):
        """Retorna uma lista com os caminhos dos templates disponíveis."""
        return self.templates


    def load_template_content(self, template_path, name):
        """Carrega o conteúdo de um template e substitui o [NAME] pelo nome do aniversariante."""
        try:
            with open(template_path, "r") as file:
                template = file.read()
            return template.replace("[NAME]", name)
        except FileNotFoundError:
            print(f"Template {template_path} não encontrado.")
            return ""





