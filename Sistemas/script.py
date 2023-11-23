import sys

def cifra_monoalfabetica(texto, chave, modo):
    resultado = ''
    alfabeto = 'abcdefghijklmnopqrstuvwxyzáéíóúâêîôûàèìòùãõäëïöü'

    for char in texto:
        char_original = char

        if char_original.lower() in alfabeto:
            index = alfabeto.index(char_original.lower())
            if modo == 'criptografar':
                novo_index = (index + chave) % len(alfabeto)
            elif modo == 'descriptografar':
                novo_index = (index - chave) % len(alfabeto)
            else:
                raise ValueError("Modo inválido. Use 'criptografar' ou 'descriptografar'.")
            
            if char.isupper():
                resultado += alfabeto[novo_index].upper()
            else:
                resultado += alfabeto[novo_index]
        else:
            resultado += char_original

    return resultado

def main():
    if len(sys.argv) != 4:
        print("Argumentos inválidos use: python script.py <arquivo.txt> <chave> <criptografar ou decriptografar>")
        sys.exit(1)

    arquivo = sys.argv[1]
    chave = int(sys.argv[2])
    modo = sys.argv[3].lower()

    with open(arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()

    resultado = cifra_monoalfabetica(texto, chave, modo)

    nome_saida = f"{arquivo.split('.')[0]}_{modo.capitalize()}.txt"

    with open(nome_saida, 'w', encoding='utf-8') as f:
        f.write(resultado)

    print(f"Operação concluída. Resultado salvo em '{nome_saida}'.")

if __name__ == "__main__":
    main()