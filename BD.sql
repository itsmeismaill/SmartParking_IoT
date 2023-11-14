-- Table vehicule
CREATE TABLE vehicule (
    id INT AUTO_INCREMENT PRIMARY KEY,
    matricule VARCHAR(20) NOT NULL
);

-- Table user
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL, -- Assurez-vous de choisir une méthode de hachage appropriée pour stocker les mots de passe
    cin VARCHAR(15) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL,
    role ENUM('client', 'admin') NOT NULL
);

-- Table abonnement
CREATE TABLE abonnement (
    id INT AUTO_INCREMENT PRIMARY KEY,
    duree INT NOT NULL,
    montant DECIMAL(10, 2) NOT NULL
);

-- Table time_parking
CREATE TABLE time_parking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_entree DATETIME NOT NULL,
    date_sortie DATETIME NOT NULL
);

-- Liaison One-to-Many entre user et vehicule
ALTER TABLE vehicule
ADD COLUMN user_id INT,
ADD CONSTRAINT fk_user_vehicule FOREIGN KEY (user_id) REFERENCES user(id);

-- Liaison One-to-One entre vehicule et abonnement
ALTER TABLE vehicule
ADD COLUMN abonnement_id INT,
ADD CONSTRAINT fk_abonnement_vehicule FOREIGN KEY (abonnement_id) REFERENCES abonnement(id);

-- Liaison One-to-Many entre vehicule et time_parking
ALTER TABLE time_parking
ADD COLUMN vehicule_id INT,
ADD CONSTRAINT fk_vehicule_time_parking FOREIGN KEY (vehicule_id) REFERENCES vehicule(id);
