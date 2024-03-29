def countvowel(string):
    count = 0
    for char in string:
        if char in "a e o i u":
            count += 1
            return count
        word= input("enter any word")
        print("number of vowels are : ", countvowel(word) )
        