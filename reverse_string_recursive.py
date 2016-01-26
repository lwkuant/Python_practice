def rev_string(s):
    if s == "":
        return ""

    return rev_string(s[1:]) + s[0:1]


# test

def main():
    word = input("Which words do you want to reverse? ")
    print(rev_string(word))

if __name__ == "__main__":
    main()

