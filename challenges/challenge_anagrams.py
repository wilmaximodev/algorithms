def quick_sort(word):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(word) <= 1:
        return word
    else:
        # Elemento de referência (pivô) é o primeiro elemento da lista
        pivot = word[0]
        # Lista de elementos menores ou iguais ao pivô
        smaller_elements = [x for x in word[1:] if x <= pivot]
        # Lista de elementos maiores que o pivô
        larger_elements = [x for x in word[1:] if x > pivot]
        # Combinação recursiva das listas ordenadas
        return (
            quick_sort(smaller_elements)
            + [pivot]
            + quick_sort(larger_elements)
        )

def is_anagram(first_string, second_string):
    # Verifica se ambas as strings são vazias
    if not first_string and not second_string:
        return (first_string, second_string, False)

    # Converte as strings para minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Ordena os caracteres das strings
    first_sorted = "".join(quick_sort(first_string))
    second_sorted = "".join(quick_sort(second_string))

    # Verifica se as strings ordenadas são iguais (anagramas)
    return (first_sorted, second_sorted, first_sorted == second_sorted)
