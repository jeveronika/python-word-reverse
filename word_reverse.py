# string = "type your string"
# split_string = string.split()
# split_string.reverse()
# print(" ".join(split_string))

user_input = input("Co chcete obrátit: ")
def word_reverser(phrase):
    string = phrase.split()
    string.reverse()
    reversed_string = " ".join(string)
    return reversed_string
print(word_reverser(user_input))
