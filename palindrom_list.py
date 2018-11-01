text = input("Enter your text to see if its a palindrone: ")

def clean_text(text):
    """ takes out all spaces, converts to lower case, and removes all non alpha"""
    user_input = ""
    for char in text.lower():
        if char.isalpha():
            user_input = user_input + char
    return user_input


def is_palindron(user_input):
    """ checks to see if text is palindrone"""
    user_input = clean_text(user_input)
    if len(user_input) == 2 and user_input[0] == user_input[-1]:
        return "this is a palindrome"
    elif len(user_input) == 1:
        return "this is a palindrome"
    if len(user_input) > 1:
        return is_palindron(user_input[1:-1])
    else: 
        return "this is NOT a palindrome"
print(is_palindron(text))