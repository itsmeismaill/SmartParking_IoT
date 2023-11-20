import bcrypt
from connection_db import conn 
import bcrypt

class User:
    myresult=""
    request=""
    cursor=conn.cursor()

    def __init__(self, id, username,cin,telephone, password, email, role):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.telephone = telephone
        self.cin = cin
        self.role = role


    def save(self):
        # hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        self.cursor.execute("INSERT INTO `users` (`id`, `username`, `password`,`cin`,`telephone`,`email`,`role`) VALUES (NULL, %s, %s,%s,%s,%s,%s);",(self.username,self.password,self.cin,self.telephone,self.email,self.role))
        conn.commit()
        print("User added successfully")
        return True
    
    def update(self):
        self.cursor.execute("UPDATE `users` SET `username` = %s, `password` = %s, `cin` = %s, `telephone` = %s, `email` = %s, `role` = %s WHERE `users`.`id` = %s;",(self.username,self.password,self.cin,self.telephone,self.email,self.role,self.id))
        conn.commit()
        print("User updated successfully")
        return True
    
    def delete(self):
        self.cursor.execute("DELETE FROM `users` WHERE `users`.`id` = %s;",(self.id))
        conn.commit()
        print("User deleted successfully")
        return True
    
    @staticmethod
    def get_all():
        User.cursor.execute("SELECT * FROM users")
        User.myresult = User.cursor.fetchall()
        return User.myresult
    
    @staticmethod
    def get_by_id(self):
        self.cursor.execute("SELECT * FROM users WHERE id=%s",(self.id))
        self.myresult = self.cursor.fetchone()
        return self.myresult

    
    @staticmethod
    def get_by_username(username):
        User.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = User.cursor.fetchone()
        
        if user_data:
            return User(**user_data)
        else:
            return None

    @staticmethod
    def check_password(username, password):
        User.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = User.cursor.fetchone()

        if user_data:
            stored_password = user_data[2] 
            return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

        return False
    
    @staticmethod
    def check_password(username, password):
        User.cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user_data = User.cursor.fetchone()

        if user_data:
            stored_password = user_data["password"] 
            return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

        return False
    
    

    
    

    