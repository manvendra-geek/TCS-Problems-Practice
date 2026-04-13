def dna_storage(n,s):
    mapping = {
    '00':'A',
    '01':'T',
    '10':'C',
    '11':'G'
    }
    result = ''
    for i in range(0,n,2):
        pair = s[i:i+2]
        result += mapping[pair]
        
    return result
        




t = int(input())

while t > 0:
    n = int(input())
    s = input()
    print(dna_storage(n,s))
    t -= 1