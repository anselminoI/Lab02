def carica_da_file(file_path):
    try:
        infile = open(file_path, "r", encoding="utf-8")
        num_sezione = infile.readline()
        elenco_libri = []
        for line in infile:
            line = line.strip().split(",")
            libro = {
                "num_sezione": num_sezione,
                "titolo": line[0],
                "autore": line[1],
                "anno": line[2],
                "pagine": line[3],
                "sez": line[4]
            }
            elenco_libri.append(libro)
        return elenco_libri
    except FileNotFoundError:
        print("Il path inserito non esiste")
        return None

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    try:
        for oggetto in biblioteca:
            if oggetto["titolo"] != titolo or int(oggetto["num_sezione"])<= sezione:
                libro = {
                        "titolo": titolo,
                        "autore": autore,
                        "anno": anno,
                        "pagine": pagine,
                        "sez": sezione
                }
                biblioteca.append(libro)
                return biblioteca
            else:
                return None
    except FileNotFoundError:
        print("il path del file che hai inserito non esiste")

def cerca_libro(biblioteca, titolo):
    for oggetto in biblioteca:
        if oggetto["titolo"] == titolo:
            risultato = (f"{titolo}, {oggetto["autore"]}, {oggetto["anno"]}, {oggetto["pagine"]}, {oggetto["sez"]}")
            return risultato

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    lista = []

    for oggetto in biblioteca:
        if int(oggetto["sez"]) == sezione and int(oggetto["num_sezione"])> sezione:
            titolo = oggetto["titolo"]
            lista.append(titolo)
    lista_ordinata = sorted(lista)
    return lista_ordinata

def main():
    biblioteca = []
    file_path = "biblioteca.csv"  # gestisci sta roba

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)

            if libro:
                print(f"Libro aggiunto con successo!")
                print(f'Titolo: {titolo}, Autore: {autore}')
                print(libro)
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()



