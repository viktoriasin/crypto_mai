from sem4.task2.hashlib.sha_1 import Hash1

if __name__ == '__main__':
    hh = Hash1()
    hh.hash(b'abcdefghijklmnopqrstuvwxyzhihowareyouiamfinethankshohohohohohohohihihhihihihi'*90)
    print(len(hh.get_result_as_bytes_object()))
    # print(len(hh.get_result_as_hex_str()))
    # print(len(bin(int(hh.get_result_as_hex_str(), 16))[2:].zfill(8)))
