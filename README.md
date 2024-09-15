# Desafios de Programação - Repositório para Vaga de Estágio

Bem-vindo ao meu repositório! Este projeto contém soluções para uma série de desafios de programação, desenvolvidas em Python, que foram submetidas como parte do processo seletivo para uma vaga de estágio.

## Índice

1. [Descrição dos Desafios](#descrição-dos-desafios)
2. [Execução do Código](#execução-do-código)
3. [Contato](#contato)

## Descrição dos Desafios

### Desafio 1: Sequência de Fibonacci

**Objetivo:** 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

**Arquivo:** `fibonacci.py`

```python

def fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

numero = int(input("Digite um número: "))

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
```

### Desafio 2: Contagem de Letras 'a'

**Objetivo:** 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

**Arquivo:** `letra_a.py`

```python

def letra_a(s):
    s = s.lower()
    contagem = s.count('a')
    return contagem

texto = input("Digite um texto: ")

quantidade = letra_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes no texto.")

```

### Desafio 3: Soma de Inteiros

**Objetivo:** 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

**Arquivo:** `desafio_de_soma.py`

```python
INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

#Resultado= 77
```

### Desafio 4: Complete a Sequência

**Objetivo:** 4) Descubra a lógica e complete o próximo elemento:

a) 1, 3, 5, 7, ___  
`Resposta: 9 (Sequência de números ímpares)  `

b) 2, 4, 8, 16, 32, 64, ____  
`Resposta: 128 (Sequência de potências de 2)  `

c) 0, 1, 4, 9, 16, 25, 36, ____  
`Resposta: 49 (Quadrados dos números naturais: 0², 1², 2²,…)  `

d) 4, 16, 36, 64, ____  
`Resposta: 100 (Quadrados dos números naturais multiplicados por 4: 1².4, 2².4, 3².4, 4².4, 5².4,...)  `

e) 1, 1, 2, 3, 5, 8, ____  
`Resposta: 13 (Sequência de Fibonacci)  `

f) 2,10, 12, 16, 17, 18, 19, ____  
`Resposta: 200 (Sequência de números iniciados com a letra "d", não há lógica numérica.)  `


**Arquivo:** `desafio4.txt`

### Desafio 5: Identificação de Interruptores e Lâmpadas

**Objetivo:** 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

```
As únicas variáveis para esta situação são: 
1- Lâmpada acesa ou apagada
2- Lâmpada fria ou quente (por ter ficado acesa)

A alternativa para duas idas seria acender uma lâmpada e ir verificar. 
Caso esteja acesa, já identificou uma. Caso esteja apagada, ja eliminou uma possibilidade.
Em seguida, apaga-se a que estava acensa, e consequentemente esquentando, e acende outra lâmpada indo imadiatamente verificar novamente e seguindo a mesma lógica, porém incluindo a variável e temperatura. 
Caso esteja acesa, já identificou. Caso esteja apagada, verifica-se a temperatura e, estando quente, é o primeiro interruptor que foi acionado, estando fria é o que não foi acionado nenhuma vez.
```

**Arquivo:** `desafio5.txt`

## Execução do Código

Para executar os códigos dos desafios:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

   ```

   ## Contato

   Email: kelrimymbb@gmail.com  
   Linkedin: https://www.linkedin.com/in/kelrimy/

   
