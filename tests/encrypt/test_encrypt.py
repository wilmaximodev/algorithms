from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("abcdef", "f") == "invalid type for key"

    with pytest.raises(TypeError):
        encrypt_message(10, "f") == "invalid type for message"

    assert encrypt_message("trybe", 8) == "ebyrt"

    assert encrypt_message("trybe", 3) == "yrt_eb"

    assert encrypt_message("trybe", 2) == "eby_rt"
