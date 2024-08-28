from app.main import get_coin_combination
import pytest


class TestsForGetCentsFunction:
    @pytest.mark.parametrize(
        "cents,result",
        [
            (1, [1, 0, 0, 0]),
            (6, [1, 1, 0, 0]),
            (17, [2, 1, 1, 0]),
            (50, [0, 0, 0, 2])
        ]
    )
    def test_for_get_coins(self,
                           cents: int,
                           result: list) -> None:
        assert get_coin_combination(cents) == result
