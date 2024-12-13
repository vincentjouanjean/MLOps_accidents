from dataclasses import dataclass


@dataclass
class Accident:
    place: int
    catu: int
    sexe: int
    secu1: float
    year_acc: int
    victim_age: int
    catv: int
    obsm: int
    motor: int
    catr: int
    circ: int
    surf: int
    situ: int
    vma: int
    jour: int
    mois: int
    lum: int
    dep: int
    com: int
    agg_: int
    int_: int
    atm: int
    col: int
    lat: float
    long: float
    hour: int
    nb_victim: int
    nb_vehicules: int

    def __init__(self,
                 place,
                 catu,
                 sexe,
                 secu1,
                 year_acc,
                 victim_age,
                 catv,
                 obsm,
                 motor,
                 catr,
                 circ,
                 surf,
                 situ,
                 vma,
                 jour,
                 mois,
                 lum,
                 dep,
                 com,
                 agg_,
                 int_,
                 atm,
                 col,
                 lat,
                 long,
                 hour,
                 nb_victim,
                 nb_vehicules):
        super().__init__()
        self.place = place
        self.catu = catu
        self.sexe = sexe
        self.secu1 = secu1
        self.year_acc = year_acc
        self.victim_age = victim_age
        self.catv = catv
        self.obsm = obsm
        self.motor = motor
        self.catr = catr
        self.circ = circ
        self.surf = surf
        self.situ = situ
        self.vma = vma
        self.jour = jour
        self.mois = mois
        self.lum = lum
        self.dep = dep
        self.com = com
        self.agg_ = agg_
        self.int_ = int_
        self.atm = atm
        self.col = col
        self.lat = lat
        self.long = long
        self.hour = hour
        self.nb_victim = nb_victim
        self.nb_vehicules = nb_vehicules
