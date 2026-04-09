
def crea_libro(titolo: str, autore: str, genere: str, copie_disponibili: int) -> dict:
    return {
        "titolo": titolo,
        "autore": autore,
        "genere": genere,
        "copie_disponibili": copie_disponibili 
    }

def info_libro(libro: dict) -> str:
    return f"{libro['titolo']} di {libro['autore']} ({libro['genere']}) - Copie disponibili: {libro['copie_disponibili']}"

def libro_disponibile(libro: dict) -> bool:
    if libro['copie_disponibili'] >= 0:
        return True
    else:
        return False

def crea_libreria() -> dict:
    return {'Libri': []}

def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
    risultati = []
    for libro in libri['Libri']:
        if libro['genere'] == genere:
            risultati.append(libro)
    return risultati

def libri_disponibili(libri: list[dict]) -> list[dict]:
    risultati = []
    for libro in libri['Libri']:
        if libro['copie_disponibili'] >= 0:
            risultati.append(libro)

def cerca_per_autore(libri: list[dict], autore: str) -> list[dict]:
    risultati = []
    for libro in libri['Libri']:
        if libro['autore'] == autore:
            risultati.append(libro)
    return risultati