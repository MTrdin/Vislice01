import model

def izpis_poraza(igra):
    #ze vemo da je prislo do poraza
    return f"Žal si izgubil/a igro, geslo je bilo: {igra.geslo}"

def izpis_zmage(igra):
    return f"Čestitke, uganil/a si geslo: {igra.geslo} v {len(igra.crke)} ugibih."

def izpis_igre(igra):
    besedilo = f""" GESLO: {igra.pravilni_del_gesla()}
Nepravilne črke: {igra.nepravilni_ugibi()}
Zmotiš se lahko le še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak}-krat."""
    return besedilo

def zahtevaj_vnos():
    vnos = input("Ugibaj: ")

    if len(vnos) == 1:
        return vnos
    else:
        return None

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        while crka is None:
            print("Napačen vnos!")
            crka = zahtevaj_vnos()
        
        stanje = igra.ugibaj(crka)

        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()