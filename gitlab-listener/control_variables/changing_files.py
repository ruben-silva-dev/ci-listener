class ChangingFiles:
    def __init__(self, gitlab):
        self.gitlab = gitlab

    def compute(self, project, start_date, end_date):
        print("Mudanças em Arquivos")