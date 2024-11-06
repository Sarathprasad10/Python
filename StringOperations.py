#Write a menu-driven program that performs the following operations on strings
#1.Check if the String is a Substring of Another String
#2.Count Occurrences of Character
#3.Replace a substring with another substring
#4.Convert to Capital Letters
def isSubstring(Mstring,Substring):
    return Substring in Mstring
def CountOccurance(String, Char):
    return String.count(Char)
def ReplaceSubstring(String,old,new):
    return String.replace(old,new)
def ConvertToCapital(String):
    return String.upper()

def main():
    while True:
        print("\nMenu")
        print("1.Check if the String is a Substring of Another String")
        print("2.Count Occurrences of Character")
        print("3.Replace a substring with another substring")
        print("4.Convert to Capital Letters")
        print("5.Exit")

        choice=input("enter your choice:")
        
        if choice=="1":
            Mstring=input("Enter the main string:")
            Substring=input("Ente the Substring to check:")
            if isSubstring(Mstring,Substring):
                print(f"'{Substring}'is a Substring of '{Mstring}'")
            else:
                print(f"'{Substring}'is not a Substring of '{Mstring}'")
        elif choice=="2":
            String=input("enter the string")
            Char=input("enter the character to count")
            if len(Char)!=1:
                print("enter a single character")
            else:
                count=CountOccurance(String,Char)
                print(f"the character'{Char}occurs{count} times in {String}")
        elif choice=="3":
            Mstring=input("Enter the main string:")
            oldSubstring=input("Ente the Substring to change :")
            newSubstring=input("enter the New Substring")
            newString=ReplaceSubstring(Mstring,oldSubstring,newSubstring)
            print(f"the new string after replacing '{oldSubstring}' with '{newSubstring}' is {newString}")
        elif choice=="4":
            String=input("Enter the string to convert to capital letters:")
            print(f"the string in capital letters is {ConvertToCapital(String)}")
        else:
            exit()
                

if __name__ == "__main__":
    main()