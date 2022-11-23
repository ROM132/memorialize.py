import random
import time


class memorialize:
    def __init__(self):
        self.board = ["x", "x", "x", "x", "x", "o", "x", "x", "x"]

    def make_board(self):
        random.shuffle(self.board)
        m.print_Board(self.board)
        print("You have 5 second to remember this!")
        letters = [1,2,3,4,5]
        for l in letters[::-1]:
            print(l)
            time.sleep(1)
        m.the_question()

    def the_question(self):
        input("\n\n\n\n\n\n\n\n\n\n\n\n\nTimes up!\nPress enter to continue: ")
        while True:
            print(f"0 1 2")
            print(f"3 4 5")
            print(f"6 7 8")
            qus = input("what was the 'o' number in the board (You have one try!) where?: ")
            if qus in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
                qus = int(qus)
                m.check_if_qus_equal_o(qus)
            else:
                print("Invalid input try again!")
                continue
    
    def check_if_qus_equal_o(self, index):
        if self.board[index] == "o":
            print("Nice job you won!"), exit()
        else:
            qus = input("You lose you want another chance (yes)/(no): ")
            if qus != "yes":
                print("Ok good bey!")
            else:
                m.__init__


    def print_Board(self, b):
        print(f"{b[0]} {b[1]} {b[2]}")
        print(f"{b[3]} {b[4]} {b[5]}")
        print(f"{b[6]} {b[7]} {b[8]}")


m = memorialize()
m.make_board()