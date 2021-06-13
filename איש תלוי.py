def main():
    opening = """    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/   """

    print(opening)

    def check_valid_input(letter_guessed="", old_letters_guessed=[]):
        # הפונקציה בודקת תקינות קלט
        # הפונקציה מקבלת את האות שהשחקן ניחש ורשימה של אותיות שכבר נוחשו
        # האות מתקבלת כמחרוזת והרשימת האותיות כרשימה
        # מחזירה שקר על שגיאה בקלט ואמת על תקינות .
        # הערך המוחזר בוליאני
        global guess_word
        if len(letter_guessed) >= 2 or guess_letter.isnumeric() or letter_guessed in old_letters_guessed:
            print("Please enter a single letter. ")
            return False
        else:
            return True

    def try_update_letter_guessed(letter_guessed, old_letters_guessed=[]):
        # הפונקציה בודקת אם האות המנוחשת נמצאת במילה הסודית
        # הפונקציה מקבלת את האות שניחשו ואת רשימת האותיות שניחשו בניסיונות הקודמים .
        #  האות מתקבלת כמחרוזת והרשימת האותיות כרשימה
        # מחזיר אמת או שקר כערך בוליאני
        if value_true:
            if letter_guessed in guess_word:
                return True
            else:  # התוו תקין אבל לא בתוך המילה שלנו
                return False  # כשהערך הזה יחזור נעלה עוד איבר באיש התלוי
        else:
            print("X")
            for letter in old_letters_guessed:
                print(f"-->{letter}")
            return "wrong"

    HANGMAN_PHOTOS = {1: """
        x-------x
    """,
                      2: """
        x-------x
        |
        |
        |
        |
        |""",

                      3: """""
        x-------x
        |       |
        |       0
        |
        |
        |""",

                      4: """""
        x-------x
        |       |
        |       0
        |       |
        |
        |""",

                      5: """""
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |""",

                      6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |""",

                      7: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |"""}

    def choose_word(file_path, index):
        what_write = open(rf"{file_path}.txt", "r").read()
        what_write = what_write.replace("\n", "")
        what_write = what_write.split()
        dif_words = 0
        for w in what_write:
            if what_write.count(w) == 1:
                dif_words += 1
            else:
                continue
        secret_word = what_write[index]
        return secret_word

    def print_hangman(num_of_tries):
        # הפונקציה מציגה את מצב הטעויות האיש התלוי
        # הפונקציה מקבלת את מס הטעויות
        # הטעויות מתקבלות כמספרים .
        # הפונקציה מחזירה את תמונת המצב של האיש התלוי כמחרוזת
        return HANGMAN_PHOTOS[num_of_tries]

    def show_hidden_word(secret_word, old_letters_guessed):
        # הפונקציה מראה את מצב המילה הסודית
        # הפונקציה מקבלת את המילה הסודית ואת רשימת האותיות שניחשו אותן
        # המילה מגיעה כמחרוזת והרשימת מילים כערך רשימתי
        # הפונקציה מחזירה את המצב של המילה הסודית ביחס לכמות הניחושים הצודקים המחרוזת .
        for letter in secret_word:
            if letter not in old_letters_guessed:
                secret_word = secret_word.replace(letter, " _ ")
            else:
                continue
        return secret_word

    def check_win(secret_word, old_letters_guessed):
        # הפונקציה בודקת אם השחקן ניצח בכך שכל המילים במילה הסודית נמצאים במילים שנוחשו
        # הפונקציה מקבלת את רשימת המילים המנוחשות ואת המילה הסודית
        # את המילה היא מקבלת המחרוזת ואת רשימת המילים היא מקבלת כרשימה .
        # הפונקציה מחזיקה אמת ושקר כערך בוליאני
        for letter in secret_word:
            if letter in old_letters_guessed:
                continue
            else:
                return False
        return True

    number_of_tries = 1
    number_of_wrong = 1
    old_guessed = []
    path = input("Enter your word's file path :")
    ind = int(input("Enter the word's index :"))
    guess_word = choose_word(path, ind)
    guess_word = guess_word.lower()
    number_of_letter = len(guess_word)
    print(show_hidden_word(guess_word, old_guessed))
    print(print_hangman(number_of_wrong))

    while (not check_win(guess_word, old_guessed)) and not (print_hangman(number_of_wrong) == HANGMAN_PHOTOS[7]):
        # הכנסת הנחושים .
        if number_of_tries == 1:
            guess_letter = input("Guess a letter :")
        else:
            guess_letter = input("Take another shoot !")
        guess_letter = guess_letter.lower()

        # הצבעה על התוצאות של הפונקציות
        value_true = check_valid_input(guess_letter, old_guessed)
        not_in_old_guess = try_update_letter_guessed(guess_letter, old_guessed)

        # התניה לדעת גם אם האות היא תקינה וגם אם היא לא נמצאת כבר ברשימת הנסיונות
        # מודפס כל הכבוד וגם נוספת האות לרשימת הניסיונות
        if not_in_old_guess == "wrong":
            number_of_tries += 1
            continue
        elif not_in_old_guess:
            print(f"""GREAT SHOOT !! the letter {guess_letter} is in our secret word !""")
            old_guessed.append(guess_letter)
            hidden_word = show_hidden_word(guess_word, old_guessed)
            number_of_tries += 1
            print(hidden_word)
        elif not not_in_old_guess:
            number_of_wrong += 1
            print("YUO ARE WRONG !")
            print(print_hangman(number_of_wrong))
            number_of_tries += 1

    # C:\Users\יאיר בן דוד\PycharmProjects\תרגילים 101\secret words

    if print_hangman(number_of_wrong) == HANGMAN_PHOTOS[7]:
        print("You are going down")
    elif number_of_tries == number_of_letter:
        print("WOW !! IT'S A CRAZY STRIKE !!!")
    elif number_of_tries < number_of_letter + 2:
        print("WOW !! You are amazing !")
    elif (number_of_tries > number_of_letter + 2) and (number_of_tries < number_of_letter + 6):
        print("You did it very well :)")
    elif (number_of_tries > number_of_letter + 6) and (number_of_tries < number_of_letter + 9):
        print("You could do it better ")
    print(f"Its took you {number_of_tries} times.")


if __name__ == '__main__':
    main()
