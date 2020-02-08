#Average of the Ascii values in String

def Average(string):
    print(string)
    sume=int(sum([ord(c) for c in string]))
    length=len(([ord(c) for c in string]))
    avg=sume/length
    print(avg)



string=input("Enter String")
Average(string)
