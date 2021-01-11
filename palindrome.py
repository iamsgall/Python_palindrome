def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    invertedWord = word[::-1]
    if(word == invertedWord):
        return True
    else:
        return False


def main():
    word = input('write a word: ')
    isPalindrome = palindrome(word)
    if(isPalindrome):
        print('palindrome')
    else:
        print('no palindrome')


if __name__ == "__main__":
    main()
