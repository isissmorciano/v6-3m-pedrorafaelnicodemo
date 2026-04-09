from biblioteca import libri
def main() -> None:
    libro_1 = libri.crea_libro("1984", "George Orwell", "Fantascienza", 1)
    libro_2 = libri.crea_libro("Dune", "Frank Herbert", "Fantascienza", 2)
    libro_3 = libri.crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1)
    libro_4 = libri.crea_libro("Harry Potter", "J.K. Rowling", "Fantasy", 3)

    print(libri.info_libro(libro_1))
    print(libri.info_libro(libro_2))
    print(libri.info_libro(libro_3))
    print(libri.info_libro(libro_4))

    libri = libri.crea_libreria()

    genere = "Fantascienza"
    filtrati = libri.filtra_per_genere(libri, genere)
    print(filtrati)
    autore = "J.K. Rowling"
    risultati = libri.cerca_per_autore(libri, autore)
    disponibilità = libri.libri_disponibili(libri)
    print(f"Libri disponibili: {disponibilità['titolo']}")
    print(risultati)

    utente_1 = prestiti.crea_utente("Mario", "Rossi")
    utente_2 = prestiti.crea_utente("Laura", "Bianchi")
    utente_3 = prestiti.crea_utente("Carlo", "Verdi")

    biblioteca = crea_biblioteca()

    prestiti.aggiungi_libro(libro_1)
    prestiti.aggiungi_libro(libro_2)

    prestiti.presta_libro(biblioteca, libro_1)
    print(libri.info_libro(libro_1))

if __name__ == "__main__":
    main()