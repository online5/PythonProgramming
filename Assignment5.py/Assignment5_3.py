#permmuations



def PrintPermutations(xyz):
    from itertools import permutations,product
    List=list(permutations(xyz))

    print(List)




x=input("Enter String")
PrintPermutations(str(x))
