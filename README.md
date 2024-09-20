2024/02 - INTRODUÇÃO AOS COMPILADORES - CI_ECP_A_M_103030802
02/09/2024 - AULA 4 - ANÁLISE LÉXICA E ANÁLISE SINTÁTICA
ANALISADOR LÉXICO DE EXPRESSÕES ARITMÉTICAS

Analise Léxica para Expressões
Expressão: 38 + (600 * 25) - 14000;
===== Analise =====
Tipo: Numero -- Valor: 38
Tipo: Operador -- Valor: SOMA
Tipo: Pontuacao -- Valor: PARESQ
Tipo: Numero -- Valor: 600
Tipo: Operador -- Valor: MULT
Tipo: Numero -- Valor: 25
Tipo: Pontuacao -- Valor: PARDIR
Tipo: Operador -- Valor: SUB
Tipo: Numero -- Valor: 14000

Regras: o programa deve ler uma entrada (expressão aritmética) a ser inserida pelo usuário. Essa expressão só pode conter números inteiros, operador aritméticos básicos (+, -, /, *) e parênteses. 
