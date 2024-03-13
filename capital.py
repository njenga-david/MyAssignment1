def capitalize_first_letter(sentence):
    return sentence.title()
def main():
    myString = input("Enter a string: ")
    capitalized_string = capitalize_first_letter( myString )
    print(" The final Capitalized String is:", capitalized_string)


main()
