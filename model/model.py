from database.dao import Dao

class Model:
    def __init__(self):
        pass

    # Funzione che è incaricata di fornire i trips (dal database).
    def get_trips(self):
        print("Getting trips...")
        dao = Dao()
        return dao.read_trips_from_db()

    def get_selected_trips(self, letter):
        print("Getting selected trips...")
        dao = Dao()
        return dao.read_selected_trips_from_db(letter)