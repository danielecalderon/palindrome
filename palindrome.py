def is_palindrome(user_input):
    sentence = len(user_input)
    n = 0
    for i in range(sentence):
        if user_input[i] == user_input[-(i+1)]:
            n=n+1
        if n == sentence:
            print(user_input, "is polindrome")
        else:
            print(user_input, "is not polindrome")
def main():
    user_input = input("Type in a sentence! \n ")
    is_palindrome(user_input)

main()
