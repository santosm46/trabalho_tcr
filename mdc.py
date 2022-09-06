

def mdc(a: int, b: int) -> int:

    # números positivos, e pelo menos um não nulo
    if a==0 and b==0: return -1
    if a<0 or b<0: return -1

    if (b>a): a, b = b, a

    while True:

        q = int(a / b)
        r = a % b

        # descomentar linha abaixo para mostrar o passo a passo
        # print(f"{a} = {b} * {q} + {r}")

        if r == 0:
            return b

        a,b = b,r

# teste
# print("mdc = " + str(mdc(350, 155)))

