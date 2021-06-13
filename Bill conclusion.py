def tip():
    def input_bill():
        bill = int(input("Your bill gentelman, the total is about "))
        perc = int(input("How much tip you want to pleasure me ? "))
        people = int(input("How many gentelman you are her ? "))
        return bill, perc, perc/100*bill, perc/100*bill + bill, people

    def main():
        bil, per, total_perc, total_bill, people = input_bill()
        print(f"{per}% tip is {total_perc:.2f} NIS, which brings your total to {total_bill} NIS")
        print(f"And its split even to {total_bill/people:.2f} NIS for each one of you.")

    main()


if __name__ == '__main__':
    tip()