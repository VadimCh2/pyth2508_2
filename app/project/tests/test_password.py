import pytest
from password_hw2 import check_password


class TestCheckPassword:
    @pytest.mark.parametrize(
        'password, expected',
        [
            ('Pups127!', True),
            ('p2shok1!', True),
            ('supopoye129.', True),
            ('NoSigmasHere!', False),
            ('Speccccc123', False),
            ('12345678', False),
            ('abcdefgh', False),
            ('Pass 123!', False),
            (' Pass123!', False),
            ('Pass123! ', False),
            ('P1s-aaaaa', True),
            ('', False),
        ]
    )
    def test_check_password_general(self, password: str, expected: bool):
        actual = check_password(password)
        assert expected is actual

    @pytest.mark.skip(reason='Test is not ready yet')
    def test_check_password_variety_of_characters(self):
        pass
