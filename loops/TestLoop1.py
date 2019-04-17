def printWhileLoops():
    val = 1;
    while val < 10:
        print("Value : ", val)
        val = val + 1
        if val == 7:
            break
        else:
            continue

def print1To5():
    for i in range(5):
        print("Now i = ",i)


def printWIthTwoRanges():
    # for(i = 2 < i < 10 ; I++) in java
    for i in range(2, 10):
        print("I = ", i)

    # for(i = 0 i < 10 ; i = i+3)
    for i in range(0, 10, 3):
        print("Value of i incremented by 3 : ", i)

def useOfElseInForLoop():
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")


if __name__ == "__main__":
    printWhileLoops()
    print("----------")
    print1To5()
    printWIthTwoRanges()
    useOfElseInForLoop()
