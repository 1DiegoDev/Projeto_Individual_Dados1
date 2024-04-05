# Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade
# de um candidato com uma vaga de acordo com seu resultado nas etapas do
# processo seletivo.
# Para isso foi criado um teste que devolve uma string no seguinte formato:
# eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em
# uma das etapas do processo - entrevista, teste teórico, teste prático e
# avaliação de soft skills).
# CONTEXTO
# Criar com Python uma lista para armazenar esses resultados
# (e outros resultados que quiser no mesmo formato, o código
# precisa funcionar para qualquer lista que seja inserida nesse
# formato) e depois uma função que busca o candidato de
# acordo com os critérios digitados pelo usuário.
# Entrega: deverá ser realizada em um único arquivo .py (que
# será entregue em um repositório do Github).

# Você deve criar com Python uma lista para armazenar esses resultados
# (e outros resultados que quiser no mesmo formato, o código precisa
# funcionar para qualquer lista que seja inserida nesse formato) e depois
# uma função que busca o candidato de acordo com os critérios
# digitados pelo usuário. O usuário vai informar qual a nota mínima de
# e, t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os
# candidatos disponíveis com nota maior ou igual a essas informadas
# pelo usuário.
# ⇨ Ao buscar por alguém com resultados 4,4,8,8 por exemplo vamos
# receber que os candidatos 1 e 5 atendem esse critério, foram bem no
# teste prático e apresentaram um ótimo nível de soft skills!


# ========================= Começo do Trabalho Individual ==================================


#Criar com python uma lista para armazenar esses resultados
#Pode ter lista dentro de uma lista!
candidatos = [
    ['candidato 1','e5_t10_p8_s8'], # Importante colocar a ',' para separá-los!
    ['candidato 2','e10_t7_p7_s8'],
    ['candidato 3','e8_t5_p4_s9'],
    ['candidato 4','e2_t2_p2_s1'],
    ['candidato 5','e10_t10_p8_s9']
]

def buscaCandidato(candidatos, entrevista, teorico, pratico, soft):
    candidatosAprovados = [] # Váriavel coringa
    for candidato, resultado in candidatos: # Usa o for para percorrer a lista de candiatos
        notas = resultado.split('_') # Chama resultado referente a candidatos # Split = Fatia a lista, faz parte de um metodo que recorta e separa a lista através de algun delimitador, o "_" separa os resultados
        e = int(notas[0][1:])
        t = int(notas[1][1:])
        p = int(notas[2][1:])
        s = int(notas[3][1:])
        if e >= entrevista and t >= teorico and p >= pratico and s >= soft:  # não entra em conflito pois etá no escopo local da função For, e nã entar em conflito com entrevistaa no escopo do def
            candidatosAprovados.append(candidato) # Executa se em cima for verdade. ê se o candidato é compativel cm o que o recrutador quer. Coloca o candidato dentro da lista vazia candidatosAprovados, a variavel coringa
    return candidatosAprovados # Retornar os candidatos aprovados.


# É mostrado para o usuário
entrevista = int(input("Qual a nota mínima necessária da entrevista?[e]:  "))
teorico = int(input("Qual a nota mínima necessária para o teste teórico?[t]:  "))
pratico = int(input("Qual a nota mínima necessária para o teste prático?[p]:  "))
soft = int(input("Qual a nota mínima necessária para o teste de soft skills?[s]:  "))

candidatosAprovados = buscaCandidato(candidatos, entrevista, teorico, pratico, soft) # invoca a função, # Candidatos aprovads é diferente da de cima, é uma lista que está recebendo o retono e uma lista por isso pode usar o for abaixo poirs o for é usado em çista.

if candidatosAprovados:
    print("Candidatos Aprovados: ")
    for candidato in candidatosAprovados:
        print(candidato)
else:
    print("Não existem candidatos aptos para a vaga...")



    





