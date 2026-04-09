from libri import info_libro, libro_disponibile

def crea_utente(nome: str, cognome: str) -> dict:
    return {
        "nome": nome,
        "cognome": cognome
        }

def crea_biblioteca() -> dict:
    return {'Libri': []}

def aggiungi_libro(biblioteca: dict, libro: dict) -> None:
    biblioteca['Libri'].append(libro)

def presta_libro(biblioteca: dict, libro: dict) -> bool:
    for libro in biblioteca['Libri']:
        verifica_libro = libri.libro_disponibile(libro)
        if verifica_libro is True:
            biblioteca['Libri']['libro'] -= 1
            return True and biblioteca['Libri']['libro']['copie_disponibili']
        if verifica_libro is False:
            return False

def restituisci_libro(biblioteca: dict, libro: dict) -> bool:
    for libro in biblioteca['Libri']:
        libro_prestito = presta_libro(biblioteca, libro)
        if libro_prestito is True:
            biblioteca['Libri']['libro']['copie_disponibili'] +=1
            return True
        else:
            return False

def libri_prestati(biblioteca: dict) -> list[dict]:
    pass
