def merge(left, right):
    result = []
    i, j = 0, 0

    # Percorre ambas as listas comparando elementos
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Adiciona os elementos restantes de ambas as listas (caso existam)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    # Caso base: lista com 0 ou 1 elemento já está ordenada
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Combina as duas metades ordenadas
    return merge(left_half, right_half)


def is_anagram(str1, str2):
    # Se uma das strings for vazia, não são anagramas
    if not str1 or not str2:
        sorted_str1, sorted_str2 = merge_sort(str1), merge_sort(str2)
        return sorted_str1, sorted_str2, False

    # Converte as strings para minúsculas
    str1, str2 = str1.lower(), str2.lower()

    # Se as strings têm comprimentos diferentes, não são anagramas
    if len(str1) != len(str2):
        sorted_str1, sorted_str2 = merge_sort(str1), merge_sort(str2)
        return sorted_str1, sorted_str2, False

    # Ordena as strings e verifica se são iguais
    sorted_str1, sorted_str2 = merge_sort(str1), merge_sort(str2)
    return sorted_str1, sorted_str2, sorted_str1 == sorted_str2
