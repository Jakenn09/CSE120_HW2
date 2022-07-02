fork_set = {"forks", "knorks", "splayds", "sporks"}
spoon_set = {"spoons", "sporks", "splayds", "spifes"}
knife_set = {"knifes", "knorks", "splayds", "spifes"}


def CheckSet(userFork, userSpoon, userKnife):
        if userFork == "yes" and userSpoon == "yes" and userKnife == "yes":
            print(fork_set.intersection(spoon_set, knife_set))

        elif userFork == "no" and userSpoon == "yes" and userKnife == "yes":
            print(spoon_set.intersection(knife_set))

        elif userFork == "yes" and userSpoon == "yes" and userKnife == "no":
            print(fork_set.intersection(spoon_set))

        elif userFork == "yes" and userSpoon == "no" and userKnife == "yes":
            print(fork_set.intersection(knife_set))

        elif userFork == "yes" and userSpoon == "no" and userKnife == "no":
            print(fork_set)

        elif userFork == "no" and userSpoon == "yes" and userKnife == "no":
            print(spoon_set)

        elif userFork == "no" and userSpoon == "no" and userKnife == "yes":
            print(knife_set)
        elif userFork == "no" and userSpoon == "no" and userKnife == "no":
            print("Then why are you using this program?")
        else:
            print("Invalid input, please only use yes or no")

def UserInputs():
    i = True
    while i == True:
        userFork = input("Do you need a fork: ")
        userFork = userFork.lower()

        userSpoon = input("Do you need a spoon: ")
        userSpoon = userSpoon.lower()

        userKnife = input("Do you need a knife: ")
        userKnife = userKnife.lower()

        CheckSet(userFork, userSpoon, userKnife)

        Cont = input("Do you want to continue: ")
        Cont = Cont.lower()

        if Cont == 'no':
                i = False
        elif Cont != 'yes' and Cont != 'no':
            print("Invalid Input! System Closing")
            i = False
        else:
            continue


    


UserInputs()