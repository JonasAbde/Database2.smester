class Bog:
    def __init__(self, titel, forfatter, pris):
        self.titel = titel
        self.forfatter = forfatter
        self.pris = pris

    def vis_info(self):
        print(f"Bogen '{self.titel}' af {self.forfatter}. Pris: {self.pris} kr.")

class Kunde:
    def __init__(self, navn):
        self.navn = navn
        self.købte_bøger = []

    def tilføj_bog(self, bog):
        self.købte_bøger.append(bog)
        print(f"{bog.titel} er tilføjet til {self.navn}'s købte bøger.")

    def vis_køb(self):
        print(f"{self.navn} har købt følgende bøger:")
        for bog in self.købte_bøger:
            print(f"- {bog.titel}")

bog1 = Bog("Python Programming.pdf", "John Smith", 299)
bog2 = Bog("Learn Java.pdf", "Jane Doe", 249)

kunde = Kunde("Mikkel")

bog1.vis_info()
bog2.vis_info()

kunde.tilføj_bog(bog1)
kunde.tilføj_bog(bog2)

kunde.vis_køb()
