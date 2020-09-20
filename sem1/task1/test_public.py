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

@pytest.mark.parametrize('num,k,res', [
    ('101010', '2', '101000'),
    ('11101010101011', '1', '11101010101010'),
    ('1010101111101', '5', '1010101101101'),
])
def test_reset_k_bit(capsys, monkeypatch, num: str, k: str, res: int):
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'{num}\n{k}\n'))
    reset_k_bit()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int(f'{res}', 2)
    assert captured.err == ''


@pytest.mark.parametrize('num,i,j,res', [
    ('101010', '1', '2', '101001'),
    ('11101010101011', '1', '3', '11101010101110'),
    ('1010101111101', '5', '8', '1010111101101'),
])
def test_swap_bit(capsys, monkeypatch, num: str, i: str, j: str, res: int):
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'{num}\n{i}\n{j}'))
    swap_bits()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int(f'{res}', 2)
    assert captured.err == ''


@pytest.mark.parametrize('num,k,res', [
    ('101111', '3', '101000'),
    ('11101010101011', '2', '11101010101000'),
    ('1010101111111', '5', '1010101100000'),
])
def test_reset_first_k_bit(capsys, monkeypatch, num: str, k: str, res: int):
    monkeypatch.setattr(sys, 'stdin', io.StringIO(f'{num}\n{k}\n'))
    reset_first_k_bit()
    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == int(f'{res}', 2)
    assert captured.err == ''

