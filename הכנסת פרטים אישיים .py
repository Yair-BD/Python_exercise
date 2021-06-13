def detail():
    details = ["name", "date of birth", "address", "personal goals"]
    update_details = []

    def memory_details(topics=[], update_topic=[]):
        i = 0
        for n in topics:
            txt = input(f"What is your {n} ?")
            if txt.isalpha() or txt.isnumeric():
                update_topic.append(f" - {topics[i].capitalize()}: {txt}\n")
            else:
                print("Enter a relevant answer :)")
                txt = input(f"What is your {n} ?")
                update_topic.append(f" - {topics[i].capitalize()}: {txt}\n")
            i += 1
        update_topic = "".join(update_topic)
        return update_topic

    print(memory_details(details, update_details))


if __name__ == '__main__':
    detail()
