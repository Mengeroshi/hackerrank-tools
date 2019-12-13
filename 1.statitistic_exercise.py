# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mode
x = int(input())
 
n = list(map(int, input().split()))
"""
dude = []
for z in n:
    dude.append(z)
print(dude)
n = dude
"""
def mean(n, x):
    sigma = 0
    for i in n:
        sigma += i
    return round(sigma/x, 1)

def median(n):
    n = sorted(n)
    list_len = len(n)
    if list_len < 1:
        return None
    elif list_len % 2 == 0:
        return (n[int((list_len-1)/2)] + n[int((list_len+1)/2)])/2.0
    else:
        return n[(list_len-1)/2]


print(mean(n, x))
print(median(n))
print(mode(n))