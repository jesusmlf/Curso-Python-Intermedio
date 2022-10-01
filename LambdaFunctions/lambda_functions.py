def run():
    palindrome = lambda string:string == string[::-1]
    print(palindrome("ana"))
    
    #Sin lambda functions
    def palindrome(string:str):
        return string == string[::-1]

    print(palindrome("ana"))
if __name__ == '__main__':
    run()