#input: user input
#output: user input
def takeOrders():
    return input("What would you like today?\n")

#input: string of comma-separated types of pancakes
#output: list of types of pancakes
#ex: input: "rice, whole wheat, chocolate" output: [“rice”, “whole wheat”, “chocolate”]
def separateOrders(str):
    lst = []
    if (str.find(",") == -1):
        return [str]
    return [str[: str.find(",")]] + separateOrders(str[str.find(",") + 1:])
		

#input: pancakes–a list that contains a stack of pancakes
#output: you answer :)
def onePlateToAnother(pancakes):
    if(len(pancakes) == 0):
	return []
    else:
	return [pancakes[len(pancakes)-1]] + onePlateToAnother(pancakes[:len(pancakes) - 1])

def orderUp(totalNum, orders): 
    #your code here!
    return

#What is this function doing?
def main():
    pancakeStack = [takeOrders()]
    while(input("Would you like anything else? y/n\n").lower() != “n”):
	pancakeStack.append(takeOrders())
    madeOrder = onePlateToAnother(pancakeStack)
    print("Your order of {} is up!".format(madeOrder))

if __name__ == "__main__":
    main()
