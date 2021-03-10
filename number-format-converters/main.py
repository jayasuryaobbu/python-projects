def dec_to_bin(n): print(bin(n).replace("0b", ""))


def dec_to_hex(n): print(hex(n))


def dec_to_oct(n): print(oct(n).replace("0o", ""))


def dec_to_bcd(n):
    str_n = str(n)
    str_n_arr = list(str_n)
    bcd_arr = []
    final_arr = []
    print_bcd = ""
    i = 0
    while i <= (len(str_n_arr) - 1):
        str_new_n = str_n_arr[i]
        new_n = int(str_new_n)
        bcd_new_n = bin(new_n).replace("0b", "")
        bcd_arr.append(bcd_new_n)
        i += 1

    for j in range(len(bcd_arr)):
        bcd_single_arr = bcd_arr[j]
        if len(bcd_single_arr) == 1:
            x = "000" + bcd_arr[j]
            final_arr.append(x)
        elif len(bcd_single_arr) == 2:
            x = "00" + bcd_arr[j]
            final_arr.append(x)
        elif len(bcd_single_arr) == 3:
            x = "0" + bcd_arr[j]
            final_arr.append(x)
        elif len(bcd_single_arr) == 4:
            x = bcd_arr[j]
            final_arr.append(x)

    final_arr_len = 0
    while final_arr_len <= (len(final_arr) - 1):
        print_bcd = print_bcd + final_arr[final_arr_len] + " "
        final_arr_len += 1

    print(print_bcd)


def bin_to_hex(n): print(hex(int(str(n), 2)))


def bin_to_dec(n): print(int(str(n), 2))


def bin_to_oct(n): print(oct(int(str(n), 2)).replace("0o", ""))


def bin_to_bcd(n): dec_to_bcd(int(str(n), 2))


def hex_to_dec(n): print(int(str(n), 16))


def hex_to_bin(n): print(bin(int(str(n), 16)).replace("0b", ""))


def hex_to_oct(n): print(oct(int(str(n), 16)).replace("0o", ""))


def hex_to_bcd(n): dec_to_bcd(int(str(n), 16))


def oct_to_dec(n): print(int(str(n), 8))


def oct_to_hex(n): print(hex(int(str(n), 8)))


def oct_to_bin(n): print(bin(int(str(n), 8)).replace("0b", ""))


def oct_to_bcd(n): dec_to_oct(int(str(n), 8))


def bcd_to_dec(n):
    bcd_arr = n.split(" ")
    dec_num = []
    print_dec = ""
    for i in range(len(bcd_arr)):
        bcd_arr_num = int(bcd_arr[i], 2)
        dec_num.append(str(bcd_arr_num))
    for j in range(len(dec_num)):
        print_dec = print_dec + dec_num[j] + ""

    bcd_to_dec_val = int(print_dec)

    return bcd_to_dec_val


def bcd_to_bin(n): print(bin(bcd_to_dec(n)).replace("0b", ""))


def bcd_to_hex(n): print(hex(bcd_to_dec(n)))


def bcd_to_oct(n): print(oct(bcd_to_dec(n)).replace("0o", ""))


if __name__ == '__main__':
    print("----Decimal Conversions----")
    dec_to_bin(8)
    dec_to_hex(8)
    dec_to_oct(8)
    dec_to_bcd(8)
    print("----Binary Conversions----")
    bin_to_hex(1000)
    bin_to_dec(1000)
    bin_to_oct(1000)
    bin_to_bcd(1000)
    print("----Hexa-Decimal Conversions----")
    hex_to_dec(0x8)
    hex_to_bin(0x8)
    hex_to_oct(0x8)
    hex_to_bcd(0x8)
    print("----Octal Conversions----")
    oct_to_bin(10)
    oct_to_dec(10)
    oct_to_hex(10)
    oct_to_bcd(10)
    print("----BCD Conversions----")
    print(bcd_to_dec('0000 0000 1000'))
    bcd_to_bin('0000 0000 1000')
    bcd_to_hex('0000 0000 1000')
    bcd_to_oct('0000 0000 1000')
