def letra_a(s):
    s = s.lower()
    contagem = s.count('a')
    return contagem

texto = input("Digite um texto: ")

quantidade = letra_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes no texto.")

