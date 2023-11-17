#include <stdio.h>
#include <string.h> 
 struct Date {
    int Jour ; 
    int Mois ;
    int Année ;
 };
 struct Etudiant {
    char Nom [20];
    char Prénom [20]; 
    struct Date date_naissance ; 
    int CNE ; 
    float Notes_S3 [6] ;
 };
int main () {
    struct Etudiant E1 ;
    strcpy(E1.Nom,"WAFAE") ;
    strcpy(E1.Prénom,"WAAZIZ ") ;
    E1.date_naissance.Jour = 21 ; 
    E1.date_naissance.Mois = 3 ;
    E1.date_naissance.Année = 2004 ;
    E1.CNE = 4335454 ;
    E1.Notes_S3[0] = 14 ;
    E1.Notes_S3[1] = 14 ;
    E1.Notes_S3[2] = 15;
    E1.Notes_S3[3] = 19;
     E1.Notes_S3[4] = 12;
    E1.Notes_S3[5] = 17 ;
    // Affichage des  informations 
    printf("Nom  : ⁒s \n",E1.Nom ) ;
    printf("Prénom : ⁒s \n",E1.Prénom ) ;
    printf("CNE : ⁒d \n" , E1.CNE) ; 
return 0  ; 
}