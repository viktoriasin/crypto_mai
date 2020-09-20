import io
import sys
import typing as tp

from .task3 import xor_all


def test_xor_all(capsys, monkeypatch):  # type: ignore
    monkeypatch.setattr(sys, 'stdin', io.StringIO('11100111\n'))
    xor_all()

    captured = capsys.readouterr()
    assert int(captured.out.replace('\n', '')) == 0
    assert captured.err == ''
