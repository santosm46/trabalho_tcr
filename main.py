
from mdc import mdc

def ler_entrada():
    pass


def resolver_congruencia(a, b, n):
    # formato ax 三 b (mod n)
    if(b%mdc(a,n)==0):
        b=b%n #b na menor fração
        for i in range(0, n): # melhorar range
            if((a*i)%n ==b):
                return i
    else: return -1


def resolver_M(vetor_n):
    produto = 1
    for ni in vetor_n:
        produto *= ni
    
    vetor_M = []
    
    for ni in vetor_n:
        vetor_M.append(int(produto / ni))
    
    return vetor_M


def resolver_solucoes_particulares(vetor_a, vetor_b, vetor_n):

    vetor_x = []

    for i in range(len(vetor_a)):
        ai, bi, ni = vetor_a[i], vetor_b[i], vetor_n[i]
        xi = resolver_congruencia(ai, bi, ni)
        vetor_x.append(xi)
    
    return vetor_x


def achar_solucao_geral(vetor_b, vetor_M, vetor_x):
    solucao = 0

    for i in range(len(vetor_x)):
        solucao += vetor_b[i] * vetor_M[i] * vetor_x[i]
    
    return solucao



if __name__ == '__main__':
    # print(resolver_congruencia(35,1,3))

    vetor_a = [1, 1, 1]
    vetor_b = [1, 4, 1]
    vetor_n = [3, 5, 7]

    vetor_x = resolver_solucoes_particulares(vetor_a, vetor_b, vetor_n)
    print(f"solucoes {vetor_x}")

    vetor_M = resolver_M(vetor_n)

    solucao = achar_solucao_geral(vetor_b, vetor_M, vetor_x)

    print(f"Solução: {solucao}")






