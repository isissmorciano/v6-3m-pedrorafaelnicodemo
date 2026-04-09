from biblioteca import libri
def main() -> None:
    libro_1 = crea_libro("1984", "George Orwell", "Fantascienza", 1)
    libro_2 = crea_libro("Dune", "Frank Herbert", "Fantascienza", 2)
    libro_3 = crea_libro("Il piccolo principe", "Antoine de Saint-Exupéry", "Romanzo", 1)
    libro_4 = crea_libro("Harry Potter", "J.K. Rowling", "Fantasy", 3)

    print(info_libro(libro_1))
    print(info_libro(libro_2))
    print(info_libro(libro_3))
    print(info_libro(libro_4))