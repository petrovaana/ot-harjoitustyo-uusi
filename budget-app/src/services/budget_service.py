#Tää on se mis tapahtuu kai yleinen luokkien laskenta ja sen muut
#Esim mun sovellukses tulee näkyy yhteismäärä menoista
from repositories.spendings_repository import SpendingsRepository


class SpendingsService:
    def __init__(self, repo: SpendingsRepository):
        self.repo = repo
    
#Mikä tulee tekee sen laskun mis näkyy kaikki yhteensä laskettu
    def sum_numbers(self):
        s = self.repo.get_all()
        return sum(x.amount for x in s)
