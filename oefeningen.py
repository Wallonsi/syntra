def eid(nummer: int):
        a = str(nummer)

        eerste_10 = int(a[:-2])
        laatste_2 = int(a[-2:])
        rest = eerste_10 % 97

        if laatste_2 == rest or laatste_2 == 100 - rest:
            return 'Echt'
        else:
            return 'Vals'

print(eid(595483996268))


def is_geldig_rijksregisternummer(rrn: int) -> bool:
    nummer_str = str(rrn)

    hoofddeel = int(nummer_str[:9])
    controlegetal = int(nummer_str[9:])

    controle_voor_2000 = 97 - (hoofddeel % 97)

print(is_geldig_rijksregisternummer(int("01010100180")))

def check_rrn(rrn: int) -> bool:
    first_9 = 1 // 100
    last_2 = 1 % 100
    return first_9 % 97 == last_2



def sex(r: str):
    return "man" if int(r[6:9]) % 2 else "vrouw"

print(sex("86031914743"))


def schrikkeljaar(jaar: int):
    if jaar % 4 == 0 and jaar % 100 != 0:
        return f"{jaar} is een schrikkeljaar"
    return f"{jaar} is geen schrikkeljaar"

print(schrikkeljaar(2028))

def is_leapyear(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

print(is_leapyear(2000))


def aantal_dagen_in_maand(maand: int, jaar: int):
    if maand in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif maand in [4, 6, 9, 11]:
        return 30
    elif maand == 2:
        if is_leapyear(jaar):
            return 29
        else:
            return 28
    else:
        return 'Wtf heb jij getypt?'

print(aantal_dagen_in_maand(13, 2025))


def priemgetal(getal):
    if getal < 2:
        return f"{getal} is geen priemgetal"

    for deler in range(2, getal):
        if getal % deler == 0:
            return f"{getal} is geen priemgetal"

    return f"{getal} is een priemgetal"

print(priemgetal(3541))

