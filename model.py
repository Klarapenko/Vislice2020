import random

STEVIL_DODOVOLJENIH_NAPAK = 10

#Konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA ='o'
NAPACNA_CRKA = '-'

#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open("vislice/Vislice2020/besede.txt") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [c for c in self.crke if c  not in self.geslo]
    
    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        #return all(c in self.crke for c in self.geslo) #torej za vsako crko naridmo ce je true in ce kerakol crke ni v self.crke bo vrnl false, če so vse ok pa vrne true.
        for c in self.geslo:
            if c not in self.crke: #vsako crko ki smo ugibal gremo skos, če je smo jo ugibal, če je nismo ugibal vrne False
                return False
    
        return True

    def nepravilni_ugibi(self):
        return ".join(self.napacne_crke())"

    def pravilni_del_gesla(self):
        trenutno = "" #prazen niz, tega bomo sestavlal in vračal nakonc
        for crka in self.geslo:
            if crka in self.crke: #če sem črko kdajkoli uganil naredim trenutno += crka
                trenutno += crka
            else:
                trenutno += "_"

        return trenutno

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower() #to kar je nekdo ugibal, najprej crko spremenimo v mejhno, ker v programu delamo z malimi črkami (smo gor nastavl)

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA 
       
     #NA NASLEDNJEM KORAKU NA BO ELIF KER SMO TUKI STRAN VRGL KAR NE RABMO IN Z NASLEDNIM IF DELAMO NA TISTIH CKRAH K SO OK

        self.crke.append(ugibana_crka) #dodamo crko v seznam ugibanih črk,brez da vemo a je prou uganu al ne

        if ugibana_crka in self.geslo:#takrat je zihr prou uganu, torej mormo sam prevert če je že zmagu
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


def nova_igra():
    nakljucna_beseda = random.choice(bazen_besed) #izbere nakljucno besedo
    return Igra(nakljucna_beseda) #naredi nov onjekt igra ki imato nakljucno besedo za geslo
 
  




    pass





