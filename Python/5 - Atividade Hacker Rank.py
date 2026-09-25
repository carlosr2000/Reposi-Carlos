# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
telefones = {}
for _ in range(n):
    celulares = input().split()
    telefones[celulares[0]] = celulares[1]
for _ in range(n):
    x = input()
    if x in telefones.keys():
        print(f'{x}={telefones.get(x)}')
    else:
        print('Not Found')