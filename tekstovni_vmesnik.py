import model

trenutna_igra = model.nova_igra()

def izpis_poraz(igra):
    return f"IZGUBIL SI, geslo je bilo: {igra.geslo}"

def izpis_zmage(igra):
    return (f"ZMAGAL SI, geslo je bilo: {igra.geslo}," +
            f"potreboval si {len(igra.napacne_crke())} ugibov.")

def izpis_igre(igra):
    text = (
        f"Stanje gesla: {igra.pravilni_del_gesla()} \n"
        f"Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napako."
    )

    return text 

def zahtevaj_vnos():
    return input("Vpiši naslednjo črko:")

def pozeni_vmestnik():
    #naredimo novo igro
    trenutna_igra = model.nova_igra()

    while True: 
        #pokazemo mu stanje 
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka) #poracuna nam stvari za zmago doda novo crko 

        if trenutna_igra.zmaga():
            print(izpis_zmage(trenutna_igra))
            break #skocimo vn iz funkcije isto ku break alpa return none 
        
        if trenutna_igra.poraz():
            print(izpis_poraz(trenutna_igra))
            break

        
pozeni_vmestnik()
        



    #ponavljamo 
    #vnos
    #preveri zmago ali poraz
    #nazaj na vnos 
print(izpis_poraz(trenutna_igra))