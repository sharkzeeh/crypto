from utils.eval_ma import eval_ma
from utils.format_time import format_time
from utils.format_window import format_window
import time


def test_eval_ma():
    assert eval_ma([1., 1., 1., 1., 1.]) == 1.
    assert eval_ma([1., 1., 1., 1., 1.]) == 1.
    assert round(eval_ma([34234.43, 34233.39, 34233.39,
                 34234.99, 34234.44]), 2) == round(34234.128, 2)
    assert eval_ma([1, 2., 3.25, 4.6453]) is None


def test_format_window():
    assert format_window(5) == '5s'
    assert format_window(60) == '1m_0s'
    assert format_window(61) == '1m_1s'
    assert format_window(3599) == '59m_59s'
    assert format_window(3600) == '1h_0m_0s'
    assert format_window(3661) == '1h_1m_1s'
    assert format_window(82861) == '23h_1m_1s'


def test_format_time():
    event_time = time.struct_time((2021, 7, 5, 12, 9, 38, 0, 186, 0))
    print_time = '05-07-2021 12:09:38'
    assert format_time(event_time) == print_time
