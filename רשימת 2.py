m_list = input("Enter something you want to buy:")
m_list = m_list.split()


def to_buy_list(n=0):
    global m_list
    if n == 1:
        return m_list
    elif n == 2:
        return len(m_list)
    elif n == 3:
        check = input("Enter product of search : ")
        if check in m_list:
            return f"{check} is already in your list!"
        else:
            return f"{check} isnt already in your list! if you want to ad him press 1 ."
    elif n == 4:
        count = input("Enter product : ")
        if count in m_list:
            return m_list.count(count)
        else:
            return f"{count} isnt already in your list! if you want to ad him press 1 ."
    elif n == 5:
        delete = input("Enter product you want to delete sir : ")
        if delete in m_list:
            return m_list.remove(delete), f"{delete} is gone."
        else:
            return f"{delete} isnt already in your list! if you want to ad him press 1 ."
    elif n == 6:
        new = input("Enter a new product : ")
        m_list.append(new)
        return f"{new} has been added to your list. "
    elif n == 7:
        all_wrong = []
        for wrong in \
                m_list:
            if wrong.isalpha():
                continue
            else:
                all_wrong.append(wrong)
        return all_wrong
    elif n == 8:
        for double in m_list:
            if m_list.count(double) > 1:
                m_list.remove(double)
            else:
                continue
        return "All the doubles are gone sir."





messege = 0
while messege != 9:
    messege = int(input("What you want to do sair ?"))
    print(to_buy_list(messege))
print("It was a pleasure to serv you sir. ")