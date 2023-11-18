from connection_db import conn

# import cv2
# from PIL import Image
# from pytesseract import pytesseract

class Vehicule:
    myresult=""
    request=""
    cursor=conn.cursor()

    def __init__(self, id, matricule,abonnement_id,user_id):
        self.id = id
        self.matricule = matricule
        self.abonnement_id = abonnement_id
        self.user_id = user_id

    def save(self):
        self.cursor.execute("INSERT INTO `vehicules` (`id`, `matricule`, `abonnement_id`,`user_id`) VALUES (NULL, %s, %s,%s);",(self.matricule,self.abonnement_id,self.user_id))
        conn.commit()
        print("Vehicule added successfully")
        return True
    
    def update(self):
        self.cursor.execute("UPDATE `vehicules` SET `matricule` = %s, `abonnement_id` = %s, `user_id` = %s WHERE `vehicules`.`id` = %s;",(self.matricule,self.abonnement_id,self.user_id,self.id))
        conn.commit()
        print("Vehicule updated successfully")
        return True
    
    def delete(self):
        self.cursor.execute("DELETE FROM `vehicules` WHERE `vehicules`.`id` = %s;",(self.id))
        conn.commit()
        print("Vehicule deleted successfully")
        return True
    
    
    @staticmethod
    def get_all():
        Vehicule.cursor.execute("SELECT * FROM vehicules")
        Vehicule.myresult = Vehicule.cursor.fetchall()
        return Vehicule.myresult
    
    def get_by_id(self):
        self.cursor.execute("SELECT * FROM vehicules WHERE id=%s",(self.id))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    
    def get_by_matricule(self):
        self.cursor.execute("SELECT * FROM vehicules WHERE matricule=%s",(self.matricule))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    def get_all_by_user(id):
        Vehicule.cursor.execute("SELECT * FROM vehicules WHERE user_id=%s",(id))
        Vehicule.myresult = Vehicule.cursor.fetchall()
        return Vehicule.myresult