station1 = {
    "url": "rijeka-omisalj",
    "name": "Omišalj"
}

station2 = {
    "url": "bresca",
    "name": "Brešca"
}

station4 = {
    "url": "rijeka-hosti",
    "name": "Rijeka-Hosti"
}

station5 = {
    "url": "delnice",
    "name": "Delnice"
}

station6 = {
    "url": "bakar",
    "name": "Bakar"
}

station8 = {
    "url": "bale2",
    "name": "Bale"
}

station10 = {
    "url": "begovo-razdolje",
    "name": "Begovo Razdolje"
}

station12 = {
    "url": "buzet-griza",
    "name": "Buzet"
}

station13 = {
    "url": "brsec",
    "name": "Brseč"
}

station17 = {
    "url": "cres",
    "name": "Cres"
}

station18 = {
    "url": "cres-ivanje",
    "name": "Cres-Ivanje"
}

station22 = {
    "url": "drivenik",
    "name": "Drivenik"
}

station27 = {
    "url": "grobnik",
    "name": "Grobnik"
}

station29 = {
    "url": "hreljin-ruzic-selo",
    "name": "Hreljin-Ružić Selo"
}

station30 = {
    "url": "ilirska-bistrica",
    "name": "Ilirska Bistrica"
}

station32 = {
    "url": "jadranovo",
    "name": "Jadranovo"
}

station39 = {
    "url": "koper-kapitanija",
    "name": "Koper"
}

station40 = {
    "url": "kraljevica-ostro",
    "name": "Kraljevica"
}

station43 = {
    "url": "krk-brzac",
    "name": "Krk-Brzac"
}

station44 = {
    "url": "krk-zagrebacka",
    "name": "Krk"
}

station46 = {
    "url": "kukuljanovo",
    "name": "Kukuljanovo"
}

station49 = {
    "url": "lovran-dobrec",
    "name": "Lovran-Dobreć"
}

station53 = {
    "url": "matulji",
    "name": "Matulji"
}

station55 = {
    "url": "mrkopalj",
    "name": "Mrkopalj"
}

station56 = {
    "url": "novalja",
    "name": "Novalja"
}

station57 = {
    "url": "novigrad",
    "name": "Novigrad"
}

station61 = {
    "url": "pag",
    "name": "Pag"
}

station62 = {
    "url": "pazin-kolodvorska",
    "name": "Pazin"
}

station64 = {
    "url": "platak",
    "name": "Platak"
}

station66 = {
    "url": "porec-marina",
    "name": "Poreč-marina"
}

station67 = {
    "url": "porec-vranici",
    "name": "Poreč-Vranići"
}

station68 = {
    "url": "portoroz-letalisce",
    "name": "Portorož-Letališče"
}

station69 = {
    "url": "pula-tartinijeva",
    "name": "Pula"
}

station70 = {
    "url": "pula-loborika",
    "name": "Pula-Loborika"
}

station71 = {
    "url": "rab-mundanije",
    "name": "Rab"
}

station75 = {
    "url": "rovinj-jvp",
    "name": "Rovinj"
}

station77 = {
    "url": "senj",
    "name": "Senj"
}

station87 = {
    "url": "umag-nazorova",
    "name": "Umag"
}

station89 = {
    "url": "vele-mune",
    "name": "Vele Mune"
}


stations_all = [station1, station2, station4, station5, station6, station8, station10, station12, station13, station17, station18, station22, station27, station29, station30, station32, station39, station40, station43, station44, station46, station49, station53, station55, station56, station57, station61, station62, station64, station66, station67, station68, station69, station70, station71, station75, station77, station87, station89]

stations_selected = [station1, station2, station4, station5, station6, station13, station17, station22, station27, station32, station53, station64]

def fetch_all_stations():
    return stations_selected