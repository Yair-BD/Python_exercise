def palindrome():
    def ask_for_words():
        txt = input("Hey friend enter a sentence :\n")
        txt = txt.lower()
        return txt

    def clear_sentence(before=""):
        after = ""
        for letter in before:
            if letter.isalpha() or letter.isnumeric() or letter == " ":
                after += letter
            else:
                after += ""
        return after

    def find_palindrome(sentence=""):
        p, np = [], []
        words = sentence.split(" ")
        [p.append(word) if word == word[::-1] else np.append(word) for word in words]
        p = "\n- ".join(p)
        np = "\n- ".join(np)
        return p, np

    def main():
        poli, not_poli = find_palindrome(clear_sentence(ask_for_words()))
        if len(poli) == 0:
            print("There was none palindrome in your sentence. ")
        else:
            print(f"That's the palindrome words in your sentence:\n- {poli}")
        if len(not_poli) == 0:
            print("You are really a palindrome man :)")
        else:
            print(f"That's the regular words in your sentence:\n- {not_poli}")

    main()

if __name__ == '__main__':
    palindrome()