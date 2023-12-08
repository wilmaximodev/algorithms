import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message_wilson():
    # Testando com key inválido (deve levantar TypeError)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Wilson", "42")

    # Testando com message inválido (deve levantar TypeError)
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123, 3)

    # Testando a criptografia com key igual a 1
    # Espera-se que o último caractere seja movido para o início
    assert encrypt_message("Wilson", 1) == "nWilso"

    # Testando a criptografia com key igual a 3
    # Espera-se que os três últimos caracteres sejam movidos para o início
    assert encrypt_message("Wilson", 3) == "sonWil"

    # Testando a criptografia com key igual a 6
    # Espera-se que nada seja alterado, já que 6 % len("Wilson") == 0
    assert encrypt_message("Wilson", 6) == "Wilson"
