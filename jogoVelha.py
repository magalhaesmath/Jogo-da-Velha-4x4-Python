# Trabalho Final - Jogo da Velha 4x4


import random

def exibeTela(jogoVelha,linha,coluna,caracter):
    """Retorna a atualização do tabuleiro do Jogo da Velha.
    list(list),int,int,str -> str"""
    
    print('    0    1    2    3')
    if linha != ' ': 
        jogoVelha[linha][coluna] = caracter
        
    for j in range(len(jogoVelha)):
        jogoAtualiza = '  '
        for v in jogoVelha[j]:
            jogoAtualiza += v + '    '
            
        print(j,jogoAtualiza)    
    return '\n'
    
def verificaVitoria(jogoVelha,jogadas,caracter):
    """Verifica as posições das peças e retorna se houve vitória ou não.
    list(list),int,str -> str"""
    vitoria = 'N'
    indiceLinha = 0
    indiceColuna = 0

    # Verifica Linha
        
    while indiceLinha < 4:
        casasUsadas = 0
        indiceColuna = 0
        while indiceColuna < 4:
            if jogoVelha[indiceLinha][indiceColuna] == caracter:
                casasUsadas += 1
            indiceColuna += 1
        indiceLinha += 1
        if casasUsadas == 4:
            vitoria = 'S'
            
    # Verifica Coluna
        
    for indice_coluna in range(0,4):
        casasUsadas = 0
        for linha in jogoVelha:
            if linha[indice_coluna] == caracter:
                casasUsadas += 1
        if casasUsadas == 4:
            vitoria = 'S'
                    
            
    # Verifica Diagonal 1

    if jogoVelha[0][0] == caracter and jogoVelha[1][1] == caracter and jogoVelha[2][2] == caracter and jogoVelha[3][3] == caracter:
        vitoria = 'S'
                
    # Verifica Diagonal 2

    if jogoVelha[3][0] == caracter and jogoVelha[2][1] == caracter and jogoVelha[1][2] == caracter and jogoVelha[0][3] == caracter:
        vitoria = 'S'

    # Verifica Quadrado:

    if jogoVelha[0][0] == caracter and jogoVelha[0][1] == caracter and jogoVelha[1][0] == caracter and jogoVelha[1][1] == caracter:
        vitoria = 'S'
    if jogoVelha[0][2] == caracter and jogoVelha[0][3] == caracter and jogoVelha[1][2] == caracter and jogoVelha[1][3] == caracter:
        vitoria = 'S'
    if jogoVelha[2][0] == caracter and jogoVelha[2][1] == caracter and jogoVelha[3][0] == caracter and jogoVelha[3][1] == caracter:
        vitoria = 'S'
    if jogoVelha[2][2] == caracter and jogoVelha[2][3] == caracter and jogoVelha[3][2] == caracter and jogoVelha[3][3] == caracter:
        vitoria = 'S'
    if jogoVelha[0][1] == caracter and jogoVelha[0][2] == caracter and jogoVelha[1][1] == caracter and jogoVelha[1][2] == caracter:
        vitoria = 'S'
    if jogoVelha[1][0] == caracter and jogoVelha[1][1] == caracter and jogoVelha[2][0] == caracter and jogoVelha[2][1] == caracter:
        vitoria = 'S'
    if jogoVelha[2][1] == caracter and jogoVelha[2][2] == caracter and jogoVelha[3][1] == caracter and jogoVelha[3][2] == caracter:
        vitoria = 'S'
    if jogoVelha[1][2] == caracter and jogoVelha[1][3] == caracter and jogoVelha[2][2] == caracter and jogoVelha[2][3] == caracter:
        vitoria = 'S'
    if jogoVelha[1][1] == caracter and jogoVelha[1][2] == caracter and jogoVelha[2][1] == caracter and jogoVelha[2][2] == caracter:
        vitoria = 'S'

    return vitoria


def main():
    """Programa principal para a execução do Jogo da Velha 4x4
    None -> None"""

    print('-------------------- Bem-vindo ao Jogo da Velha! --------------------')
    
    jogadas = 0
    caracter = ' '
    linha = ' '
    coluna = ' '
    lista_posicoes = []
    jogoVelha = [['-','-','-','-'],['-','-','-','-'],['-','-','-','-'],['-','-','-','-']]
    opcao_caracter_jogador_str = input('Jogador 1 - Escolha o símbolo [1 - X ou 2 - O]:\n')
    
    
    while opcao_caracter_jogador_str not in '12':
        print('Opção inválida!')
        opcao_caracter_jogador_str = input('Jogador 1 - Escolha o símbolo [1 - X ou 2 - O]:\n')
    if int(opcao_caracter_jogador_str) == 1:
        caracter_jogador = 'X'
        caracter_cpu = 'O'
    if int(opcao_caracter_jogador_str) == 2:
        caracter_jogador = 'O'
        caracter_cpu = 'X'   

    print(exibeTela(jogoVelha,linha,coluna,caracter))
    
    while jogadas < 17:
        # Jogador 1:
        posicao_str = input('Jogador 1 - Escolha uma posição [x,y]:\n')
        
        while len(posicao_str) != 5 or posicao_str[1] not in '0123' or posicao_str[3] not in '0123' or [int(posicao_str[1]),int(posicao_str[3])] in lista_posicoes or posicao_str not in str.format('[{},{}]',int(posicao_str[1]),int(posicao_str[3])):
            posicao_str = input('Posição inválida. Jogador 1 - Escolha uma posição [x,y]:\n')

        linha = int(posicao_str[1])
        coluna = int(posicao_str[3])

        caracter_jogador = caracter_jogador
        caracter_cpu = caracter_cpu
            
        lista_posicoes += [[linha,coluna],]

            
        print(exibeTela(jogoVelha,linha,coluna,caracter_jogador))
        jogadas +=1
        print(str.format('Número de jogadas {}\n',jogadas))

        # Verificação de vitória:
        verificacao_jogador = verificaVitoria(jogoVelha,jogadas,caracter_jogador)
        if jogadas >= 7:
            # Verificação para o jogador 1:
            if verificacao_jogador == 'S':
                print('-------------------- Jogador 1 é o Campeão! --------------------\n')
                novaPartida = str.upper(input('Deseja iniciar uma nova partida?[S/N]\n'))
                while novaPartida != 'S' and novaPartida != 'N':
                    novaPartida = str.upper(input('Comando inválido. Deseja iniciar uma nova partida?[S/N]\n'))
                if novaPartida == 'S':
                    print(main())
                elif novaPartida == 'N':
                    print('-------------------------- Volte sempre! --------------------------')
                    jogadas = 17

        

        # CPU:
        if verificacao_jogador != 'S':
            print('Vez do Jogador 2') 
            linha = random.randint(0,3)
            coluna = random.randint(0,3)
        
            while [linha,coluna] in lista_posicoes:
                linha = random.randint(0,3)
                coluna = random.randint(0,3)

            lista_posicoes += [[linha,coluna],]
                    
            print(exibeTela(jogoVelha,linha,coluna,caracter_cpu))
            print(str.format('Jogador  2 - Escolheu a posição [{},{}]',linha,coluna))
            jogadas +=1
            print(str.format('Número de jogadas {}\n',jogadas))
        
            
        # Verificação de vitória:
               
            # Verificação para a CPU:
            verificacao_cpu = verificaVitoria(jogoVelha,jogadas,caracter_cpu)
            if verificacao_cpu == 'S':
                print('-------------------- Jogador 2 é o Campeão! --------------------\n')
                novaPartida = str.upper(input('Deseja iniciar uma nova partida?[S/N]\n'))
                while novaPartida != 'S' and novaPartida != 'N':
                    novaPartida = str.upper(input('Comando inválido. Deseja iniciar uma nova partida?[S/N]\n'))
                if novaPartida == 'S':
                    print(main())
                elif novaPartida == 'N':
                    print('-------------------------- Volte sempre! --------------------------')
                    jogadas = 17
               
    

        if jogadas == 16:
            
            novaPartida = str.upper(input('Empate! Deseja iniciar uma nova partida?[S/N]\n'))
            
            while novaPartida != 'S' and novaPartida != 'N':
                novaPartida = str.upper(input('Comando inválido. Deseja iniciar uma nova partida?[S/N]\n'))

            if novaPartida == 'S':
                print(main())  
                
            elif novaPartida == 'N':
                print('-------------------------- Volte sempre! --------------------------')
                jogadas += 1
                
            

main()    
