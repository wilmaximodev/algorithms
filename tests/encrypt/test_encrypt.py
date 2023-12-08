import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Teste para key inválido (deve levantar TypeError)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        result = encrypt_message("teste", "f")
        assert result is None, f"Esperava None, mas obteve {result}"

    # Teste para message inválido (deve levantar TypeError)
    with pytest.raises(TypeError, match="tipo inválido para message"):
        result = encrypt_message(8, "f")
        assert result is None, f"Esperava None, mas obteve {result}"

    # Teste para criptografia com key igual a 8
    # Espera-se que a palavra seja invertida
    result = encrypt_message("teste", 8)
    assert result == "etset", f"Esperava 'etset', mas obteve {result}"

    # Teste para criptografia com key igual a 3
    # Espera-se que os três últimos caracteres sejam movidos para o início
    result = encrypt_message("teste", 3)
    assert result == "set_et", f"Esperava 'set_et', mas obteve {result}"

    # Teste para criptografia com key igual a 2 em uma palavra mais longa
    # Espera-se que os dois últimos caracteres sejam movidos para o início
    result = encrypt_message("errooouu", 2)
    assert result == "uuooor_re", f"Esperava 'uuooor_re', mas obteve {result}"
