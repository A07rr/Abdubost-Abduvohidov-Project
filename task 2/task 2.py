def checking_similar_string(main_string, instant_string):
    if main_string.find(instant_string):
        return "Scilicet string already exists!"
    else:
        return "Existence of such string is not defined"

print(checking_similar_string(main_string = input("Enter the string: "), instant_string = input("Enter the string for research: ")))
