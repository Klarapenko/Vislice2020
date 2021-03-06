
import random
import json
STEVILO_DOVOLJENIH_NAPAK = 10

ZACETEK = 'Z'

#konstante za rezultate ugibanj 
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'



#konstante za zmago in poraz
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open("besede.txt", encoding="UTF-8") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())
        
class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = crke.lower() #sprehodt se morm s for zanko

    def pravilne_crke(self):
        return [c for c in self.crke if c in self.geslo]

    def napacne_crke(self):
        return [c for c in self.crke if c not in self.geslo]
    
    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke: 
                return False
        return True 

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
    
    def pravilni_del_gesla(self):
        trenutno = ""
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else: 
                trenutno += "_"

        return trenutno
    
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
    
    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(ugibana_crka)
        
        if ugibana_crka in self.geslo: #vedmo da je pravilno uganil
            #uganil je
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
        nakljucna_beseda = random.choice(bazen_besed)
        return Igra(nakljucna_beseda)


class Vislice: #namen tega je da bo zaobsegal več iger(kontejner teh iger) v sebi bo imel slovar iger
    """
    Skrbi za trenutno stanje več iger(imel bo več objektov tipov Igra)
    """
    def __init__(self):

        #Slovar, ki ID-ju priredi objekt njegove igre
        self.igre = {}
        #self.igre[20] #če to naredimo dobimo ven napako

        
    def prosti_id_igre(self):
        """vrne nek id, ki ga ne uporabla nobena igra"""

        if len(self.igre) == 0:
            return 0
        #mam neke igre notr, pa pogledam kok je mela igra največji ID pa dam +1, ta nov ID se ziher ne bo z nobenim prej ponovil
        #kdaj lahko vzamemo max + 1? česa ne smemo delat? problem je če brišemo, sam zenkrat ne bom brisal
        
        else: 
            return max(self.igre.keys()) + 1
            #druga možnost: return len(self.igre.keys())

    #zdaj naredimo metodo nova igra, da k prde igralec pa hoče igrad da dobi ID pa mu zgenerira novo igro
    def nova_igra(self):
        self.preberi_iz_datoteke()
        

        #dobimo svež id
        
        nov_id = self.prosti_id_igre()
        
        #naredimo novo igro
        
        sveza_igra = nova_igra()
        
        #vse to shranimo v self.igre

        self.igre[nov_id] = (sveza_igra, ZACETEK) #zacetek je konstanta
       
        #če začnemo igro je dobr da dobimo odgovor od fukcije: torej da vrne id, ker z id lahko vedno pridemo do cele igre
        
        return nov_id
        
    def ugibaj(self, id_igre, crka):
        #dobimo staro igro ven
        self.preberi_iz_datoteke()
        trenutna_igra_ = self.igre[id_igre]

         #ugibamo crko, dobimo novo stanje
        novo_stanje = trenutna_igra.ugibaj(crka)

        #Zapišemo posodobljeno stanje in igro nazaj v "bazo"
        self.igre[id_igre] = (trenutna_igra, novo_stanje)

        self.shrani_v_datoteko

    def shrani_v_datoteko(self):
        {id_igre : ((geslo, ugibane_crke), stanje_igre )
        
        }

        igre = {}
        for id_igre, (igra, stanje) in self.igre.items(): #id_igre, (Igra, stanje)
            igre[id_igre] = ((igra.greslo, igra.crke), stanje )

        with open("stanje_iger.json", "w") as out_file:
            json.dump(igre, out_file )

    def preberi_iz_datoteke(self):
        with open("stanje_iger.json", "r" ) as in_file:
            igre= json.load(in_file) #mogoče bi to preimenoval v #igre_iz_diska

        self.igre = {}

        for id_igre , ((geslo, crke), stanje) in igre.items():
            (geslo, crke), stanje = igre[id_igre]
            self.igre[int(id_igre)] = Igra(geslo, crke), stanje   

