def szamol(amit, amiben):
    szamlalo = 0
    for szamlalando in amiben:
        if szamlalando == amit:
            szamlalo += 1
    return szamlalo


def beolvas():
    with open('astronauts.csv', 'r', encoding='utf-8') as asztronautak:
        olvas = asztronautak.read().strip().split('",,')
    return olvas


def szazalek_szamitas(ami, aminek):
    szazalek = ami / aminek * 100
    szazalek = round(szazalek, 2)
    return str(szazalek) + '%'


def keres(amit, amiben):
    for kulcs in amiben:
        if amiben[kulcs] == amit:
            return kulcs


def main():
    bemenet = beolvas()
    for index, item in enumerate(bemenet):
        if item == '':
            bemenet.pop(index)

    szuletesek = []
    for sor in bemenet:
        itemek = sor.split(',')
        szuletesek.append(itemek[4])
    szuletesek.pop(0)

    honapok = []
    for datum in szuletesek:
        honapok.append(datum[0])

    osszesites = {
        '1': szamol('1', honapok),
        '2': szamol('2', honapok),
        '3': szamol('3', honapok),
        '4': szamol('4', honapok),
        '5': szamol('5', honapok),
        '6': szamol('6', honapok),
        '7': szamol('7', honapok),
        '8': szamol('8', honapok),
        '9': szamol('9', honapok),
        '10': szamol('10', honapok),
        '11': szamol('11', honapok),
        '12': szamol('12', honapok),
    }

    legnagyobb = osszesites['1']
    for kulcs in osszesites:
        if osszesites[kulcs] > legnagyobb:
            legnagyobb = osszesites[kulcs]

    masodik_legnagyobb = osszesites['2']
    for kulcs in osszesites:
        if osszesites[kulcs] != legnagyobb and osszesites[kulcs] > masodik_legnagyobb:
            masodik_legnagyobb = osszesites[kulcs]

    harmadik_legnagyobb = osszesites['3']
    for kulcs in osszesites:
        if osszesites[kulcs] != legnagyobb and osszesites[kulcs] != masodik_legnagyobb and osszesites[
            kulcs] > harmadik_legnagyobb:
            harmadik_legnagyobb = osszesites[kulcs]

    legnagyobb_szazalek = szazalek_szamitas(legnagyobb, len(honapok))
    masodik_legnagyobb_szazalek = szazalek_szamitas(masodik_legnagyobb, len(honapok))
    harmadik_legnagyobb_szazalek = szazalek_szamitas(harmadik_legnagyobb, len(honapok))

    legnagyobb_honap = keres(legnagyobb, osszesites)
    masodik_legnagyobb_honap = keres(masodik_legnagyobb, osszesites)
    harmadik_legnagyobb_honap = keres(harmadik_legnagyobb, osszesites)

    print(f'A legtöbb űrhajós a(z) {legnagyobb_honap}. hónapban született: {legnagyobb_szazalek}')
    print(f'A második legtöbb űrhajós a(z) {masodik_legnagyobb_honap}. hónapban született: {masodik_legnagyobb_szazalek}')
    print(
        f'A harmadik legtöbb űrhajós a(z) {harmadik_legnagyobb_honap}. hónapban született: {harmadik_legnagyobb_szazalek}')


main()
