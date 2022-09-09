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
        print(vetor_M[i])
        print(vetor_n[i])
        while((vetor_M[i]*mult)%vetor_n[i]!=1):
            mult =mult+1
        resultadoM.append(mult)
    return resultadoM





if __name__ == '__main__':
    # print(resolver_congruencia(35,1,3))

    # vetor_a = [1, 1, 1]
    # vetor_b = [1, 4, 1]
    # vetor_n = [3, 5, 7]


    vetor_a = [2, 4]
    vetor_b = [3, 2]
    vetor_n = [5, 7]
    # sol. válida 158

    for i in range (len(vetor_a)):
        j=1
        while(vetor_a[i]!=1):
            j=j+1
            if(((vetor_a[i]*j)%vetor_n[i])==1):
                vetor_a[i]=(vetor_a[i]*j)%vetor_n[i]
                vetor_b[i]=(vetor_b[i]*j)%vetor_n[i]

    vetor_M = resolverM(vetor_n)
    print(vetor_M)
    vetorM=resolverM_(vetor_M,vetor_n)
    resultado = 0
    soman=1
    for i in range (len(vetor_n)):
        soman = soman*vetor_n[i]
    for i in range (len(vetor_a)):
        resultado = resultado +vetor_b[i]*vetorM[i]*vetor_M[i]
    print(f'Resultado:{resultado%soman} * {soman}L')


