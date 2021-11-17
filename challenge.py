n = int(input("Enter the number of which you want the factorial: "))
counter = 1
nfactorial = n
typed_answer = str(n)

while counter < n:
    nfactorial = nfactorial * (n - counter)
    typed_answer = typed_answer + " * " + str(n - counter)
    counter += 1

if n == 0:
    nfactorial = 1
    typed_answer = "1"

print(f"{n}! = {typed_answer} = {nfactorial}")