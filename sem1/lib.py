import sys
import typing as tp


def read_input():
    input_: tp.IO[str] = sys.stdin
    data: tp.Any = []
    for line in input_:  # To end reading process from the terminal press CTRL-D (EOF in Python)
        data.append(line)
    #data: tp.Any = input_.readlines()
    return data


def write_output(data_to_write):
    output: tp.IO[str] = sys.stdout
    output.write(f'{data_to_write}\n')
    output.flush()