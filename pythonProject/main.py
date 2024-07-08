from translator import Translator


t =  Translator()


while True:
    print(f"welcome to my translator from cz to en enjoy\n\n1-translate\n2-add world\n3-delete translation\n4-show 10 best words"
          f"\n5-show 10 worst words\n6-replace translation\n7-exit")
    choice = input("Enter your choice: ")
    if choice == "1":       #translation
        t.translate(t.find_czword())
    elif choice == "2":
        t.add_word(input("Enter a czech word: "),input("Enter english translation: "))
    elif choice == "3":
        t.remove_word(t.find_czword())
    elif choice == "4":
        t.del_translation(t.find_enword())
    elif choice == "5":
        t.show_10best()
    elif choice == "6":
        t.show_10worst()
    elif choice == "7":
        t.replace_translation(t.find_czword(), input("Enter a new translation: "))
    elif choice == "8":
        break
    elif choice == '*':
        t.print_data()