# Inizializza la variabile per la somma
somma = 0

# Continua a chiedere numeri finché l'utente non inserisce zero
while True:
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    
    if numero == 0:
        break  # Esce dal ciclo se l'utente inserisce 0
    
    somma += numero  # Aggiunge il numero alla somma

# Dopo che il ciclo è terminato, stampa la somma totale
print("La somma totale dei numeri inseriti è:", somma)

# Aggiungi una pausa prima che il programma si chiuda
input("Premi Invio per uscire...")
