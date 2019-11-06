## Return unique elements of a list
def unique_list(sample):
    uniques = set(sample)
    uniques = list(uniques)
    return uniques
sample = [1,1,1,1,2,2,3,3,3,3,4,5]
unique_list(sample)

# Multiply all numbers in a list

def multiply_list(arr):
    result = 1
    for i in arr:
        result = result*i
    print(result)
arr = [1,2,3,-4]
multiply_list(arr)

# String palindrome
def palindrome(s):
    if s==s[::-1]:
        print('palindrome')
    else:
        print('Not')
s = ['nurses run']
palindrome(s)

# String is pangram: contains each letter of alphabet at least once
def ispangram(str1,alphabet=string.ascii_lowercase):
    for i in alphabet:
        if i in str1:
            return True
        else:
            return False
ispangram("The quick brown fox jumps over the lazy dog")
