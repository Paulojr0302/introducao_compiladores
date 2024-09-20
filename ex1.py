import os
os.system('cls')

def analisar_expressao(expressao):
    tokens = []
    i = 0
    while i < len(expressao):
        if expressao[i].isdigit():
            numero = ''
            while i < len(expressao) and expressao[i].isdigit():
                numero += expressao[i]
                i += 1
            tokens.append(('Numero', numero))
        elif expressao[i] == '+':
            tokens.append(('Operador', 'SOMA'))
            i += 1
        elif expressao[i] == '-':
            tokens.append(('Operador', 'SUB'))
            i += 1
        elif expressao[i] == '*':
            tokens.append(('Operador', 'MULT'))
            i += 1
        elif expressao[i] == '/':
            tokens.append(('Operador', 'DIV'))
            i += 1
        elif expressao[i] == '(':
            tokens.append(('Pontuacao', 'PARESQ'))
            i += 1
        elif expressao[i] == ')':
            tokens.append(('Pontuacao', 'PARDIR'))
            i += 1
        else:
            i += 1
    return tokens

def imprimir_tokens(tokens):
    print("===== Análise =====")
    for token in tokens:
        print("Tipo:", token[0], "-- Valor:", token[1])

def main():
    os.system('cls')  
    expressao = input("Digite uma expressão: ")
    tokens = analisar_expressao(expressao)
    os.system('cls')  
    imprimir_tokens(tokens)

main()
