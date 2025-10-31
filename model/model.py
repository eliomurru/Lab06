from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        query = "SELECT * FROM automobile"
        self.cursor.execute(query)
        risultati = self.cursor.fetchall()

        if not risultati:
            return None

        automobili = [Automobile(*r) for r in risultati]
        return automobili

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        query = "SELECT * FROM automobile WHERE LOWER(modello) = LOWER(%s)"
        self.cursor.execute(query, (modello,))

        risultati = self.cursor.fetchall()

        if not risultati:
            return None

        automobili = [Automobile(*r) for r in risultati]
        return automobili
