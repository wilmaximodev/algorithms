def is_palindrome_iterative(word):
      # Verifica se a palavra é vazia
    if not word:
        return False

    # Inicializa os índices
    start, end = 0, len(word) - 1

    # Itera até que os índices se cruzem
    while start < end:
        # Compara os caracteres nas posições opostas
        if word[start] != word[end]:
            return False

        # Move os índices para o centro
        start += 1
        end -= 1

    # Se a verificação for bem-sucedida, é um palíndromo
    return True
