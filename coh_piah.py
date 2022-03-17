# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:01:15 2022

@author: abeln
"""

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    similaridade = 0
    soma_tl_a_b = 0

    """ faz o somatorio da difernca entre os Traços Linguisticos de cada assinatura """
    while i < 6:
        soma_tl_a_b = soma_tl_a_b + abs(as_a[i] - as_b[i])
        i += 1
            
    similaridade = (soma_tl_a_b / 6)
    return similaridade


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_frases_a = []
    lista_palavras_a = []
    lista_palavras_texto = []
    num_palavras_unicas_a = 0
    num_palavras_diferentes_a = 0
    qtd_frases_a = 0
    qtd_caracteres_frases_a = 0
    
    lista_sentencas_a = separa_sentencas(texto)

    for i in lista_sentencas_a:
        lista_frases_a.append(separa_frases(i))

    for i in range(len(lista_frases_a)):
        frases_a = lista_frases_a[i]
        qtd_frases_a = qtd_frases_a + len(frases_a)
        for j in range(len(frases_a)):
            lista_palavras_a.append(separa_palavras(frases_a[j]))
            qtd_caracteres_frases_a = qtd_caracteres_frases_a + len(frases_a[j])

   #for i in range(len(lista_palavras_a)):
   #    num_palavras_unicas_a = num_palavras_unicas_a + n_palavras_unicas(str(lista_palavras_a[i]))

   #for i in range(len(lista_palavras_a)):
   #    num_palavras_diferentes_a = num_palavras_diferentes_a + n_palavras_diferentes(str(lista_palavras_a[i]))

    soma_tamanho_palavras_a = 0
    soma_caracteres_sentenca_a = 0
    soma_caracteres_frase_a = 0
    wal_a = 0
    num_palavras_a = len(lista_palavras_a)
    qtd_palavras_a = 0

    """ Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras. """
    for i in range(num_palavras_a):
        palavras_a = lista_palavras_a[i]
        for i in palavras_a:
            lista_palavras_texto.append(i)
        qtd_palavras_a = qtd_palavras_a + len(palavras_a)
        for j in range(len(palavras_a)):
            soma_tamanho_palavras_a = soma_tamanho_palavras_a + len(palavras_a[j])

    num_palavras_unicas_a = num_palavras_unicas_a + n_palavras_unicas(lista_palavras_texto)
    num_palavras_diferentes_a = num_palavras_diferentes_a + n_palavras_diferentes(lista_palavras_texto)

    
    wal_a = soma_tamanho_palavras_a / qtd_palavras_a

    """ Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. """
    ttr_a =  num_palavras_diferentes_a / qtd_palavras_a

    """ Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras """
    hlr_a = num_palavras_unicas_a / qtd_palavras_a

    """ Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número 
    de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença)."""
    for j in range(len(lista_sentencas_a)):
        soma_caracteres_sentenca_a = soma_caracteres_sentenca_a + len(lista_sentencas_a[j])
        
    sal_a = soma_caracteres_sentenca_a / len(lista_sentencas_a)
    
    """ Complexidade de sentença é o número total de frases divido pelo número de sentenças. """
    sac_a = qtd_frases_a / len(lista_sentencas_a)

    """ Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto """
  
    pal_a = qtd_caracteres_frases_a / qtd_frases_a
    
    ret = []
    ret.append(wal_a)
    ret.append(ttr_a)
    ret.append(hlr_a)
    ret.append(sal_a)
    ret.append(sac_a)
    ret.append(pal_a)
    
       
    return ret



def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    num_textos_a = len(textos)
    ind = 0 
    menor_indice = 0
    grau_simililaridade_ass = []
    ass_a = []
    while ind < num_textos_a:
        texto_aux = textos[ind]
        ass_a_aux = calcula_assinatura(texto_aux)
        ass_a.append(ass_a_aux)
        grau_simililaridade_ass_aux = compara_assinatura(ass_a[ind], ass_cp)
        grau_simililaridade_ass.append(grau_simililaridade_ass_aux)
        ind += 1
    ind, menor_indice = 1, 1
    menor_similaridade = grau_simililaridade_ass[0]
    while ind < num_textos_a:
        if grau_simililaridade_ass[ind] < menor_similaridade:
            menor_similaridade = grau_simililaridade_ass[ind]
            menor_indice = ind + 1
        ind += 1
            
    return menor_indice
    


""" retorna: wal_b, ttr_b, hlr_b, sal_b, sac_b, pal_b """
#ass_b = le_assinatura()
ass_b = [4.51, 0.693, 0.55, 70.82, 1.82, 38.5]
#ass_b = [4.325, 0.7375, 0.5875, 54.125, 2.0, 26.5625]
#lista_textos_a = le_textos()
lista_textos_a = ['Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.', 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.']
#lista_textos_a = ['Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.', 'Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.']
num_texto = avalia_textos(lista_textos_a, ass_b)
print("O autor do texto", num_texto, "está infectado com COH-PIA")
        
        

    
        




