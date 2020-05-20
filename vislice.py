import bottle
import model

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0, "views")

@bottle.get("/")
def index():
    #prva stran
    return bottle.template("index.tpl")

@bottle.get("/img/<picture>")
def static_file(picture):
    return bottle.static_file(picture, "img")

@bottle.post("/igra/")
def nova_igra():
    #naredi novo igro
    id_igre = vislice.nova_igra()
    #preusmeri na naslov za igranje nove igre
    bottle.redirect(f"/igra/{id_igre}/")

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    (igra, stanje) = vislice.igre[id_igre]
    return bottle.template("igra.tpl", igra= igra, stanje=stanje, id_igre=id_igre, ZMAGA=model.ZMAGA, PORAZ=model.PORAZ)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj(id_igre):
    crka = bottle.request.forms.get("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f"/igra/{id_igre}/")
    #neki je narobe

bottle.run(debug=True, reloader=True)
