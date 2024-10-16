import random

#função que gera a introdução da história
def gerar_introducao():
    introducoes =["era uma vez," "há muito tempo atrás", "num reino distante"]
    return random.choice(introducoes)

#fução que gera o desenvolvimento da história
def gerar_desenvolvimento():
    desenvolvimentos = ["um valente cavaleiro", "uma desmetida guerreira", "um bravo guerreiro",
                        "uma poderosa feiticeira", "um sábio mago"]
    return random.choice(desenvolvimentos)

#funçã0 que gera o final da história
def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.", 
              "descobrindo um tesouro escondindo.", "salvando o reino da escuridão.",
              "encontrando um amor verdadeiro."]
    return random.choice(finais)

#função principal que gera toda a historia
def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()   
    final = gerar_final()   

    historia = f"{introducao} {desenvolvimento} {final}"
    return historia

# exibe a história gerada
if __name__ == "_main_" :
 print(gerar_historia())
       



