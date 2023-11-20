from connection_db import conn

class TimeParking:
    myresult=""
    request=""
    cursor=conn.cursor()

    def __init__(self, id, vehicule_id, date_entree, date_sortie):
        self.id = id
        self.vehicule_id = vehicule_id
        self.date_entree = date_entree
        self.date_sortie = date_sortie


    def save(self):
        self.cursor.execute("INSERT INTO `time_parking` (`id`, `vehicule_id`, `date_entree`, `date_sortie`) VALUES (NULL, %s, %s, %s);",(self.vehicule_id,self.date_entree,self.date_sortie))
        conn.commit()
        print("TimeParking added successfully")
        return True
    
    def update(self):
        self.cursor.execute("UPDATE `time_parking` SET `vehicule_id` = %s, `date_entree` = %s, `date_sortie` = %s WHERE `time_parking`.`id` = %s;",(self.vehicule_id,self.date_entree,self.date_sortie,self.id))
        conn.commit()
        print("TimeParking updated successfully")
        return True
    

    def delete(self):
        self.cursor.execute("DELETE FROM `time_parking` WHERE `time_parking`.`id` = %s;",(self.id))
        conn.commit()
        print("TimeParking deleted successfully")
        return True
    
    @staticmethod
    def get_all():
        TimeParking.cursor.execute("SELECT * FROM time_parking")
        TimeParking.myresult = TimeParking.cursor.fetchall()
        return TimeParking.myresult
    
    def get_by_id(self):
        self.cursor.execute("SELECT * FROM time_parking WHERE id=%s",(self.id))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    
    def get_by_vehicule_id(self):
        self.cursor.execute("SELECT * FROM time_parking WHERE vehicule_id=%s",(self.vehicule_id))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    
    def get_last_by_date_entrer(self, num_records=1):
        query = "SELECT * FROM time_parking WHERE vehicule_id=%s ORDER BY date_entree DESC LIMIT %s"
        self.cursor.execute(query, (self.vehicule_id, num_records))
        self.myresult = self.cursor.fetchall()
        return self.myresult

    

