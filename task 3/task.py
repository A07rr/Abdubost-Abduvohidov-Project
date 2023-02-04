data = "abcdefghijklmnopqrstuvwxyz"
def checking_english_words(data, search_input):
    if  data.find(search_input):
        return True
    else:
        return False
print(checking_english_words(data, input("Enter a checking string: ")))