libros = []

def agregarlibro():
    while True:
        autor = input("Ingrese autor del libro: ").strip()
        if len(autor)==0:
            print("El autor no puede estar vacio.")
        else:
            break
    while True:
        titulo = input("Ingresa el titulo del libro").strip().title()
        if len(titulo) == 0:
            print("El título no puede estar vacío.")
        else:
            repetido = False

            for l in libros:
                if l["titulo"] == titulo:
                    repetido = True
                    break

            if repetido:
                print("No puede estar repetido.")
            else:
                break
    libro = {
        "autor": autor,
        "titulo": titulo
    }
    libros.append(libro)
    print("Libro agregado con exito")