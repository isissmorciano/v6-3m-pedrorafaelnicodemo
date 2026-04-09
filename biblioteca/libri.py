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
    return {""}
    
def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
