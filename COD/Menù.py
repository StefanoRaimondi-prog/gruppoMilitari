from Unità_Militare import Unità_Militare
class UnitaMilitare:
    def __init__(self, nome, tipo, comandante):
        self.nome = nome
        self.tipo = tipo
        self.comandante = comandante

    def descrizione(self):
        return f"Unità: {self.nome}, Tipo: {self.tipo}, Comandante: {self.comandante}"


class Controllo_Militare:
    def __init__(self):
        self.opzioni = {
            1: "Mostra unità militari",
            2: "Aggiungi unità militari",
            3: "Dettagli unità militari",
            4: "Esci"
        }
        self.unita_registrate = {}

    def mostra_menu(self):
        print("\n=== Menu Controllo Militare ===")
        for k, v in self.opzioni.items():
            print(f"{k}. {v}")

    def aggiungi_unita(self):
        nome = input("Nome dell'unità: ")
        tipo = input("Tipo di unità: ")
        comandante = input("Nome del comandante: ")
        unita = UnitaMilitare(nome, tipo, comandante)
        self.unita_registrate[nome] = unita
        print(f"Unità '{nome}' aggiunta con successo.")

    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
        else:
            print("Unità registrate:")
            for nome in self.unita_registrate:
                print(f"- {nome}")

    def dettagli_unita(self):
        nome = input("Inserisci il nome dell'unità: ")
        unita = self.unita_registrate.get(nome)
        if unita:
            print(unita.descrizione())
        else:
            print(f"Nessuna unità trovata con nome '{nome}'.")

    def esegui(self):
        while True:
            self.mostra_menu()
            try:
                scelta = int(input("Scegli un'opzione: "))
                if scelta == 1:
                    self.mostra_unita()
                elif scelta == 2:
                    self.aggiungi_unita()
                elif scelta == 3:
                    self.dettagli_unita()
                elif scelta == 4:
                    print("Chiusura del sistema...")
                    break
                else:
                    print("Scelta non valida. Riprova.")
            except ValueError:
                print("Inserisci un numero valido.")


# ▶️ Esegui il sistema
if __name__ == "__main__":
    controllo = Controllo_Militare()
    controllo.esegui()
