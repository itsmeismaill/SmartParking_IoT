from connection_db import conn
class Abonnement:
    myresult=""
    request=""
    cursor=conn.cursor()

    def __init__(self, id, duree,montant):
        self.id = id
        self.duree = duree
        self.montant = montant
    
    def save(self):
        self.cursor.execute("INSERT INTO `abonnements` (`id`, `duree`, `montant`) VALUES (NULL, %s, %s);",(self.duree,self.montant))
        conn.commit()
        print("Abonnement added successfully")
        return True
    
    def update(self):
        self.cursor.execute("UPDATE `abonnements` SET `duree` = %s, `montant` = %s WHERE `abonnements`.`id` = %s;",(self.duree,self.montant,self.id))
        conn.commit()
        print("Abonnement updated successfully")
        return True
    
    def delete(self):
        self.cursor.execute("DELETE FROM `abonnements` WHERE `abonnements`.`id` = %s;",(self.id))
        conn.commit()
        print("Abonnement deleted successfully")
        return True
    @staticmethod
    def get_all():
        Abonnement.cursor.execute("SELECT * FROM abonnements")
        Abonnement.myresult = Abonnement.cursor.fetchall()
        return Abonnement.myresult
    
    def get_by_id(self):
        self.cursor.execute("SELECT * FROM abonnements WHERE id=%s",(self.id))
        self.myresult = self.cursor.fetchone()
        return self.myresult
    

