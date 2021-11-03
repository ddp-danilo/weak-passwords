import time
import code_check as cdd

start_time = 0
def addfrt_zeros(num):
    size = len(num)
    if size == 1:
        return '00000' + num
    if size == 2:
        return '0000' + num
    if size == 3:
        return '000' + num
    if size == 4:
        return '00'
    if size == 5:
        return '0'
    else:
        return num
def main():
    code = 0
    loop = True
    while loop:
        str_zero_code = addfrt_zeros(str(code))
        if cdd.checar_codigo(str_zero_code):
            return str_zero_code
        else:
            code += 1
    return None


if __name__ == '__main__':
    start_time = int(time.time())
    cdd = main()
    end_time = int(time.time())
    print(cdd, 'The script took', end_time - start_time, ' seconds to find the code.')

