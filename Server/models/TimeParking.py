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
        self.cursor.execute("INSERT INTO `timeparkings` (`id`, `vehicule_id`, `date_entree`, `date_sortie`) VALUES (NULL, %s, %s, %s);",(self.vehicule_id,self.date_entree,self.date_sortie))
        conn.commit()
        print("TimeParking added successfully")
        return True
    
    def update(self):
        self.cursor.execute("UPDATE `timeparkings` SET `vehicule_id` = %s, `date_entree` = %s, `date_sortie` = %s WHERE `timeparkings`.`id` = %s;",(self.vehicule_id,self.date_entree,self.date_sortie,self.id))
        conn.commit()
        print("TimeParking updated successfully")
        return True
    

    def delete(self):
        self.cursor.execute("DELETE FROM `timeparkings` WHERE `timeparkings`.`id` = %s;",(self.id))
        conn.commit()
        print("TimeParking deleted successfully")
        return True
    
    @staticmethod
    def get_all():
        TimeParking.cursor.execute("SELECT * FROM timeparkings")
        TimeParking.myresult = TimeParking.cursor.fetchall()
        return TimeParking.myresult
    
    def get_by_id(self):
        self.cursor.execute("SELECT * FROM timeparkings WHERE id=%s",(self.id))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    
    def get_by_vehicule_id(self):
        self.cursor.execute("SELECT * FROM timeparkings WHERE vehicule_id=%s",(self.vehicule_id))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    

