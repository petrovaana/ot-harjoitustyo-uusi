#Luokka kuvaa yksittäistä kirjausta. Esim et paljonko rahaa menee vuokraan
#Tai sit paljonko saa palkasta
#user_id = et sama käyttäjä kysees?
#amount = paljonko voi olla negatiivinenki
#content = mihin menee / mistä just saa

class Budget:
    def __init__(self, user_id, amount:int, content:str):
        self.user_id = user_id
        self.amount = amount
        self.content = content