class Translator:
    def __init__(self):
        self.data: dict = {"jablko": [42, "apple"],
                           "kočka": [17, "cat"],
                           "strom": [91, "tree"],
                           "dům": [58, "house"],
                           "slunce": [29, "sun"],
                           "knihovna": [64, "library"],
                           "hory": [5, "mountains"],
                           "káva": [88, "coffee"],
                           "vlak": [12, "train"],
                           "dítě": [37, "child"],
                           "květina": [19, "flower"],
                           "voda": [76, "water"],
                           "čas": [81, "time"],
                           "pes": [66, "dog"],
                           "město": [94, "city"],
                           "most": [50, "bridge"],
                           "pláž": [3, "beach"],
                           "ryba": [8, "fish"],
                           "kniha": [25, "book"],
                           "okno": [70, "window"],
                           "křeslo": [45, "chair"],
                           "telefon": [75, "phone"],
                           "stůl": [14, "table"],
                           "papír": [31, "paper"],
                           "klobouk": [60, "hat"],
                           "dveře": [10, "door"],
                           "krabice": [47, "box"],
                           "kruh": [23, "circle"],
                           "hvězda": [84, "star"],
                           "kamion": [55, "truck"],
                           "písek": [36, "sand"],
                           "kostel": [68, "church"],
                           "hodiny": [97, "clock"],
                           "tráva": [2, "grass"],
                           "písmeno": [18, "letter"],
                           "kámen": [72, "stone"],
                           "kolo": [33, "wheel"],
                           "kabelka": [49, "purse"],
                           "křídlo": [7, "wing"],
                           "koule": [22, "ball"],
                           "křižovatka": [41, "intersection"],
                           "kružnice": [15, "circle"],
                           "koberec": [53, "carpet"],
                           "klíč": [90, "key"],
                           "křoví": [27, "bush"],
                           "křišťál": [79, "crystal"],
                           "kabát": [38, "coat"],
                           }

        #searches

    def find_czword(self):
        choice = input(f"what are you looking for(cz)? ")
        words = self.data.keys()
        for m in words:
            if choice in m:
                if input(f"is this your choice {m}? (y/n) ").lower() == "y":
                    return m

    def find_enword(self):
        choice = input(f"what are you looking for(en)? ")
        words = self.data.items()
        for m in words:
            for k in m[1:]:
                if choice in k:
                    if input(f"is this your choice {k}? (y/n) ").lower() == "y":
                        return k

    def translate(self, word):
        self.data.get(word)[0] += 1
        return (i for i in self.data.get(word)[1:])

    # words operation

    def add_word(self, word, translation):
        self.data.update({word: [0, translation]})

    def remove_word(self, word):
        self.data.pop(word)

    def replace_word(self, word, new_word):
        temp = self.data.get(word)
        self.data.pop(word)
        self.data.update({new_word: temp})

    # translation operation

    def add_translation(self, word, translation):
        self.data.get(word).append(translation)

    def replace_translation(self, word):
        for t in range(len(self.data.get(word)[1:])):
            if input(f"do you want to replace {self.data.get(word)[t + 1]} y/n: ").lower() == "y":
                self.data.get(word)[t + 1] = input(f"set a new translation: ")

    def del_translation(self, word):
        for t in range(len(self.data.get(word)[1:])):
            if input(f"do you want to remove {self.data.get(word)[t + 1]}").lower() == "y":
                self.data.get(word).pop(t + 1)

    # others
    def print_data(self):
        self.sort_data()
        for key in list(self.data.keys()):
            print(f"{key} --> {self.data[key][1:]} and was {self.data[key][0]} translated")

    def sort_data(self):
        self.data = dict(sorted(self.data.items(), key=lambda x: x[1][0], reverse=True))

    def show_10best(self):
        self.sort_data()
        for i in range(10):
            print(
                f"{i + 1}. {list(self.data.keys())[i]} --> {list(self.data.values())[i][1:]} with popularity of "
                f"{list(self.data.values())[i][0]}")

    def show_10worst(self):
        self.sort_data()
        for i in range(10):
            print(
                f"{i + 1}. {list(self.data.keys())[-i - 1]} --> {list(self.data.values())[-i - 1][1:]} with popularity of "
                f"{list(self.data.values())[-i - 1][0]}")
