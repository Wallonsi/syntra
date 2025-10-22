#print("*" * 15, "William", "*" * 16)
#print("*" * 40)

def starred_name(last_name: str, first_name: str,total_width: int = 60, char: str = "*" "$"):

    assert type(last_name) == str, "last_name must be a string"
    assert type(first_name) == str, "first_name must be a string"
    assert type(total_width) == int, "total_width must be a number"
    assert type(char) == str, "char must be a string"

    name = last_name + f" {char} " + first_name
    prefix = (total_width - 2 - len(name)) // 2
    postfix = total_width - 2 - len(name) - prefix

    print("*" * prefix, name, "*" * postfix)

starred_name("Allonsius", "William")
starred_name(last_name="Allonsius", first_name="William",total_width=40,char="£")
starred_name(last_name="Allonsius", first_name="William", char="=")
starred_name(total_width=30, last_name="Allonsius", char="#", first_name="William")
starred_name("Hong", "May", 40, "'")
starred_name(10, 10, 10, 10)


#functie begint altijd met 'def' dan geef je die een naam, dan verplichte ronde haken ook al heb je geen parameters
#tussen de haken parameters, boven heb je er 2, altijd ':' op het einde
#dan tab gebruiken, alles in tab zit in de functie
#optionele parameter total_width, deze is nu standaard 60, optionele parameter is ook char
#'*' zorgt ervoor dat je de benaming van de parameters moet gebruiken, anders krijg je een foutmelding als je '*' toevoegt bij 'def starred_name(*,...)
#hinting zorgt ervoor waar je een string verwacht je ook een string moet ingeven, anders krijg je een waarschuwing (gele onderlijning), zoals op lijn 16
#assert = veronderstellingen, veronderstel dat last_name een string is

