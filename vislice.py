import bottle
import model

#konstanti
DATOTEKA_S_STANJEM = "stanje.json"

SECRET = "VISLICE"


bottle.TEMPLATE_PATH.insert(0, "views")

vislice = model.Vislice(DATOTEKA_S_STANJEM)

@bottle.get("/")
def index():
    #prva stran
    return bottle.template("index")

@bottle.get("/img/<picture>")
def static_file(picture):
    return bottle.static_file(picture, "img")

@bottle.post("/nova_igra/")
def nova_igra():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = vislice.nova_igra()
    #preusmeri na naslov za igranje nove igre
    vislice.zapisi_igre_v_datoteko()
    bottle.response.set_cookie("id_igre", id_igre, path="/", secret="SECRET")
    bottle.redirect("/igra/")


@bottle.get("/igra/")
def pokazi_igro():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = bottle.request.get_cookie("id_igre", secret=SECRET)
    (igra, stanje) = vislice.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, stanje=stanje, id_igre=id_igre, ZMAGA=model.ZMAGA, PORAZ=model.PORAZ)

@bottle.post("/igra/")
def ugibaj():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = bottle.request.get_cookie("id_igre", secret=SECRET)
    crka = bottle.request.forms.crka #ce das get zgubis šumnike

    vislice.ugibaj(id_igre, crka)
    vislice.zapisi_igre_v_datoteko()

    bottle.redirect(f"/igra/")
   

bottle.run(debug=True, reloader=True)

#neki je narobe