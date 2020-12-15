from sem4.task2.hashlib.constants import INT_SIZE


def f_first_stage(b, c, d):
    return (b & c) | (~b & d)


def f_second_stage(b, c, d):
    return b ^ c ^ d


def f_third_stage(b, c, d):
    return (b ^ c) | (b & d) | (c & d)


f = (f_first_stage, f_second_stage, f_third_stage, f_second_stage)


def left_rotate(data, by=1):
    return ((data << by) | (data >> (INT_SIZE - by))) & 0xffffffff
