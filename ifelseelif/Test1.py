def check(stringValue):
    if stringValue == "Hello":
        print("It is Hello")
    elif stringValue == "World":
        print("It is world ...")
    else:
        print("It is different ", stringValue)

def checkSpecialCase(stringValue):
    if stringValue == "Hello": print("It is hello...")
    # Usage of short hand
    print("It is hello") if stringValue == "Hello" else print("Some other value")

def checkAndOrCondition(stringParam):
    if stringParam is not None and len(stringParam) != 0:
        print("It is neither null nor blank")

    if stringParam != None and len(stringParam) != 0:
        print("It is also correct")

    if stringParam == "Hello" or stringParam == "World":
        print("It is either Hello or World")



if __name__ == "__main__":
    check("Hello")
    check("World")
    check("Some other value ...")
    checkSpecialCase("Hello")
    checkAndOrCondition("Hello")
