
import os
from mdc import mdc

def clear():
    os.system("clear")

def resolverM(vetor_n):
    produto = 1
    for ni in vetor_n:
        produto *= ni
    vetor_M = []
    for ni in vetor_n:
        vetor_M.append(int(produto / ni))
    return vetor_M


def resolverM_(vetor_M,vetor_n):
    resultadoM=[]
    for i in range (len(vetor_n)):
        mult=1
        while((vetor_M[i]*mult)%vetor_n[i]!=1):
            mult =mult+1
        resultadoM.append(mult)
    return resultadoM


def validar_entradas(vetor_a, vetor_n):
    tam = len(vetor_a)

    for i in range (tam):
        a=vetor_a[i]
        n=vetor_n[i]
        mdcan = mdc(a,n)

        if(mdcan == -1):
            print(f"Sistema sem solução pois a{i+1} e n{i+1} são zero e não tem mdc")
            return False

        if(mdcan != 1):
            print(f"Sistema sem solução pois mdc(a{i+1},n{i+1}) = {mdcan} ≠ 1")
            return False
    
    for i in range (tam):
        for j in range (i+1, tam):

            ni=vetor_n[i]
            nj=vetor_n[j]
            mdcnn = mdc(ni,nj)

            if(mdcan == -1):
                print(f"Sistema sem solução pois n{i+1} e n{j+1} são zero e não tem mdc")
                return False

            if(mdcnn != 1):
                print(f"Sistema sem solução pois mdc(n{i+1},n{j+1}) = {mdcnn} ≠ 1")
                return False
    
    return True


def ler_inteiro(msg, msg_erro="Erro! Digite um número inteiro: ", min=None):
    print(msg, end="")

    while True:
        numero = input("")

        try:
            numero = int(numero)

            if min is not None and numero < min:
                print(f"Erro! Digite um número ≥ {min}: ",end='')
                continue

            return numero
        except:
            print(msg_erro, end="")


def ler_natural(msg, msg_erro = "Erro! Digite um número natural: "):

    while True:
        numero = ler_inteiro(msg, msg_erro=msg_erro)

        if(numero < 1):
            print(msg_erro, end="")
            continue

        return numero


def resolver_equacoes(vetor_a, vetor_b, vetor_n):
    for i in range (len(vetor_a)):
        j=1
        while(vetor_a[i]!=1):
            j=j+1
            if(((vetor_a[i]*j)%vetor_n[i])==1):
                vetor_a[i]=(vetor_a[i]*j)%vetor_n[i]
                vetor_b[i]=(vetor_b[i]*j)%vetor_n[i]

    vetor_M = resolverM(vetor_n)
    # print(vetor_M)
    vetorM=resolverM_(vetor_M,vetor_n)
    resultado = 0
    soman=1

    for i in range (len(vetor_n)):
        soman = soman*vetor_n[i]
    
    for i in range (len(vetor_a)):
        resultado = resultado + vetor_b[i]*vetorM[i]*vetor_M[i]

    # print(f'Resultado: {resultado%soman} + {soman}L')
    vi = resultado%soman
    print(f"A solução é qualquer valor x tal que x = {vi} + {soman}L (L ∈ ℤ) \n")
    print(f"Exemplo: para L=0, x é {vi} \n")


def mostrar_equacoes(qtd_equacoes, vetor_a, vetor_b, vetor_n):
    clear()
    for i in range(qtd_equacoes):
        a = f"{vetor_a[i]:2}" if i < len(vetor_a) else f"a{(i+1)}"
        b = f"{vetor_b[i]:2}" if i < len(vetor_b) else f"b{(i+1)}"
        n = f"{vetor_n[i]:2}" if i < len(vetor_n) else f"n{(i+1)}"

        print(f"{a:2}*x ≡ {b:2} (mod {n:2})")
    print("")


if __name__ == '__main__':

    vetor_a = []
    vetor_b = []
    vetor_n = []

    qtd_equacoes = ler_natural("Digite a quantidade de equações: ")

    print("")

    for i in range(1, qtd_equacoes+1):

        mostrar_equacoes(qtd_equacoes, vetor_a, vetor_b, vetor_n)
        vetor_a.append(ler_inteiro(f"Digite o valor de a{i}: "))

        mostrar_equacoes(qtd_equacoes, vetor_a, vetor_b, vetor_n)
        vetor_b.append(ler_inteiro(f"Digite o valor de b{i}: "))

        mostrar_equacoes(qtd_equacoes, vetor_a, vetor_b, vetor_n)
        vetor_n.append(ler_inteiro(f"Digite o valor de n{i}: ", min=2))

    mostrar_equacoes(qtd_equacoes, vetor_a, vetor_b, vetor_n)

    if not validar_entradas(vetor_a, vetor_n):
        exit(0)

    resolver_equacoes(vetor_a, vetor_b, vetor_n)


