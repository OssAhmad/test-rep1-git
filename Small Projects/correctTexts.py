# Function to replace 'f' with 'L' in a given string
def replace_f_with_L(input_string):
    return input_string.replace('	', ' ')


def main():

    input_string = """Erewhon	is	not a	member	of	the	European Union (‘EU’). It	is	a	party	to the	Paris
Convention	and is	a	member	of	the	World	Trade	Organization	and	signatory	to	the	
TRIPS	Agreement.	Treaties	are	not	self-executing	in	Erewhon.""" # input("Enter the text: ")
    result = replace_f_with_L(input_string)
    print("&&&&&&&&\n&&&&&&&&\n&&&&&&&&\n")
    print("Modified string: \n" + result)
    print("&&&&&&&&\n&&&&&&&&\n&&&&&&&&\n")


if __name__ == "__main__":
    main()




