from connection_db import conn


class Abonnement:
    myresult=""
    request=""
    cursor=conn.cursor()

    def __init__(self, id, duree,montant):
        self.id = id
        self.duree = duree
        self.montant = montant
    

    def to_dict(self):
        return {
            'id': self.id,
            'duree': self.duree,
            'montant': self.montant
        }
        
    def save(self):
        try:
            # Explicitly convert duree to an integer
            duree_int = int(self.duree)

            # Use parameters in the execute method to avoid SQL injection
            self.cursor.execute(
                "INSERT INTO `abonnements` (`id`, `duree`, `montant`, `initial_duree`) VALUES (NULL, %s, %s, %s);",
                (duree_int, self.montant, duree_int)
            )
            conn.commit()
            print("Abonnement added successfully")

            # Use LAST_INSERT_ID() to get the last inserted ID
            self.cursor.execute("SELECT * FROM `abonnements` WHERE `id` = LAST_INSERT_ID();")
            saved_data = self.cursor.fetchone()

            self.id = saved_data['id']
            self.duree = saved_data['duree']
            self.montant = saved_data['montant']

            return self
        except Exception as e:
            # Handle any exceptions, print the error, and return None
            print(f"Error adding abonnement: {e}")
            return None
    
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
    
    def get_by_id(id):
        Abonnement.cursor.execute("SELECT * FROM abonnements WHERE id=%s",str(id))
        Abonnement.myresult = Abonnement.cursor.fetchone()
        return Abonnement.myresult
    

    

