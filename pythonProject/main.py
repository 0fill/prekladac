from translator import Translator

t = Translator()

while True:
    print(
        f"welcome to my translator from cz to en enjoy\n\n1-translate\n2-change words\n3-change translations"
        f"\n4-show 10 best words\n5-show 10 worst words\n6-exit")
    choice = input("Enter your choice: ")
    if choice == "1":  #translation
        for i in t.translate(t.find_czword()):
            print(i)

    elif choice == "2":
        print("""1-add a word
        2-delete a word
        3-replace a word""")
        choice2 = input("Enter your choice: ")
        if choice2 == "1":
            t.add_word(input("Enter a word: "), input("enter translation: "))
        elif choice2 == "2":
            t.remove_word(t.find_czword())
        elif choice2 == "3":
            t.replace_word(t.find_czword(), input(f"Enter a new word: "))

    elif choice == "3":
        print("""1-add a translation
        2-delete a translation
        3- replace a translation""")
        choice3 = input("Enter your choice: ")
        if choice3 == "1":
            t.add_translation(t.find_czword(), input("Enter a translation: "))
        elif choice3 == "2":
            t.del_translation(t.find_czword())
        elif choice3 == "3":
            t.replace_translation(t.find_czword())

    elif choice == "4":
        t.show_10best()
    elif choice == "5":
        t.show_10worst()
    elif choice == "6":
        break
    elif choice == '*':
        t.print_data()
