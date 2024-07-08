class Translator:
    def __init__(self):
        self.data = {"jablko": ("apple", 5),
                     "stůl": ("table", 8),
                     "kočka": ("cat", 7),
                     "kniha": ("book", 4),
                     "auto": ("car", 5),
                     "slunce": ("sun", 4),
                     "dům": ("house", 8),
                     "květina": ("flower", 2),
                     "pes": ("dog", 5),
                     "hory": ("mountains", 8),
                     "řeka": ("river", 6),
                     "most": ("bridge", 2),
                     "pták": ("bird", 7),
                     "ryba": ("fish", 2),
                     "káva": ("coffee", 1),
                     "telefon": ("phone", 9),
                     "obloha": ("sky", 8),
                     "tráva": ("grass", 1),
                     "pláž": ("beach", 3),
                     "město": ("city", 0),
                     "strom": ("tree", 7),
                     "hvězdy": ("stars", 58),
                     "vítr": ("wind", 4),
                     "sníh": ("snow", 4),
                     "dešť": ("rain", 6),
                     "kytara": ("guitar", 8),
                     "cesta": ("road", 0),
                     "kolo": ("bike", 4),
                     "vlak": ("train", 7),
                     "letadlo": ("airplane", 30),
                     "oceán": ("ocean", 6),
                     "ostrov": ("island", 3),
                     "písek": ("sand", 7),
                     "zahrada": ("garden", 2),
                     "hora": ("mountain", 1),
                     "louka": ("meadow", 2),
                     "les": ("forest", 36),
                     "jezero": ("lake", 4),
                     "voda": ("water", 7),
                     "měsíc": ("moon", 4),
                     "planeta": ("planet", 1),
                     "vesmír": ("universe", 9),
                     "země": ("earth", 3),
                     "vesnice": ("village", 2)
                     }

    def add_word(self, word, translation):
        self.data.update({word: (translation, 0)})

    def translate(self, word):
        self.data.get(word)[1] += 1
        return self.data.get([word])[0]

    def remove_word(self, word):
        self.data.pop([word])

    def replace_translation(self, word, translation):
        self.data.get(word)[0] = translation

    def print_data(self):
        self.sort_data()
        t = self.data
        print(t)
        print(t.__class__)
        for key in list(self.data.keys()):
            print(f"{key} --> {self.data[key][0]} and was {self.data[key][1]} translated")

    def sort_data(self):
        self.data = dict(sorted(self.data.items(), key=lambda x: x[1][1], reverse=True))       #doesnt work

    def del_translation(self, word):
        del self.data[word][0]

    def show_10best(self):
        self.sort_data()
        for i in range(10):
            print(f"{i + 1}. {list(self.data.keys())[i]} --> {list(self.data.values())[i][0]} with popularity of {list(self.data.values())[i][1]}")

    def show_10worst(self):
        self.sort_data()
        for i in range(10):
            print(
                f"{i + 1}. {list(self.data.keys())[-i]} --> {list(self.data.values())[-i][0]} with popularity of {list(self.data.values())[-i][1]}")
