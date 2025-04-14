class Unità_Militare:
    def __init__(self, nome, numero_militari):
        self.nome_unità = nome
        self.numero_militari = numero_militari

    def __str__(self):
        return f"Unità: {self.nome}, Numero di militari: {self.numero_militari}"
    
    def muovi(self, distanza):
        print(f"L'unità {self.nome_unità} si muove di {distanza} km.")
        
    def attacca(self, obiettivo):
        print(f"L'unità {self.nome_unità} attacca l'obiettivo {obiettivo}.")
        
    def ritirati(self):
        print(f"L'unità {self.nome_unità} si ritira.")
        
        class Fanteria(Unità_Militare):
            def __init__(self, nome, numero_militari, tipo_arma):
                super().__init__(nome, numero_militari)
                self.tipo_arma = tipo_arma

            def __str__(self):
                return f"Fanteria: {self.nome_unità}, Numero di militari: {self.numero_militari}, Tipo arma: {self.tipo_arma}"
            
            def attacca(self, obiettivo):
                print(f"La fanteria {self.nome_unità} attacca l'obiettivo {obiettivo} con {self.tipo_arma}.")
                
        class Cavalleria(Unità_Militare):
            def __init__(self, nome, numero_militari, tipo_veicolo):
                super().__init__(nome, numero_militari)
                self.tipo_veicolo = tipo_veicolo

            def __str__(self):
                return f"Cavalleria: {self.nome_unità}, Numero di militari: {self.numero_militari}, Tipo veicolo: {self.tipo_veicolo}"
            
            def attacca(self, obiettivo):
                print(f"La cavalleria {self.nome_unità} attacca l'obiettivo {obiettivo} con {self.tipo_veicolo}.")
                
        class Artiglieria(Unità_Militare):
            def __init__(self, nome, numero_militari, tipo_cannone):
                super().__init__(nome, numero_militari)
                self.tipo_cannone = tipo_cannone

            def __str__(self):
                return f"Artiglieria: {self.nome_unità}, Numero di militari: {self.numero_militari}, Tipo cannone: {self.tipo_cannone}"
            
            def attacca(self, obiettivo):
                print(f"L'artiglieria {self.nome_unità} attacca l'obiettivo {obiettivo} con {self.tipo_cannone}.")
                
        class Supporto_Logistico(Unità_Militare):
            def __init__(self, nome, numero_militari, tipo_supporto):
                super().__init__(nome, numero_militari)
                self.tipo_supporto = tipo_supporto

            def __str__(self):
                return f"Supporto Logistico: {self.nome_unità}, Numero di militari: {self.numero_militari}, Tipo supporto: {self.tipo_supporto}"
            
            def attacca(self, obiettivo):
                print(f"Il supporto logistico {self.nome_unità} attacca l'obiettivo {obiettivo} con {self.tipo_supporto}.")
                
        class Ricognizione(Unità_Militare):
            def __init__(self, nome, numero_militari, tipo_veicolo):
                super().__init__(nome, numero_militari)
                self.tipo_veicolo = tipo_veicolo

            def __str__(self):
                return f"Ricognizione: {self.nome_unità}, Numero di militari: {self.numero_militari}, Tipo veicolo: {self.tipo_veicolo}"
            
            def attacca(self, obiettivo):
                print(f"La ricognizione {self.nome_unità} attacca l'obiettivo {obiettivo} con {self.tipo_veicolo}.")