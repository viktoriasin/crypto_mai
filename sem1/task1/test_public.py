import io
import sys

import pytest

from .task1 import get_k_bit, set_k_bit, reset_k_bit, swap_bits, reset_first_k_bit


@pytest.mark.parametrize('num,k,res', [
    ('101010', '2', 1),
    ('101010', '1', 0),
    ('1010101111101', '5', 1),
])
def test_get_ks_bit(capsys, monkeypatch, num: str, k: str, res: int):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'{num}\n{k}\n'))
    get_k_bit()
    captured = capsys.readouterr()
    assert captured.out.replace('\n', '') == str(res)
    assert captured.err == ''


def test_set_ks_bit(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('10010\n3\n'))
    set_k_bit()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('10110', 2)
    assert captured.err == ''


def test_reset_k_bit(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('10110\n3\n'))
    reset_k_bit()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('10010', 2)
    assert captured.err == ''


def test_swap_bit(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('101101\n1\n2'))
    swap_bits()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('101110', 2)
    assert captured.err == ''


def test_reset_first_k_bit(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'stdin', io.StringIO('101111\n3\n'))
    reset_first_k_bit()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int('101000', 2)
    assert captured.err == ''

