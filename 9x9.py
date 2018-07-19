def printLine(char,times):
    """
    列印字符串
    :param char: 字符
    :param times: 次数
    :return:
    """
    print(char * times)
    return

for row in range(1,10):
    for col in range(1,10):
        print("%d x %d = %d\t" % (row, col, row * col),end='')
    print('')

printLine('-',30)
for row in range(1,10):
    for col in range(1,row+1):
        print("%d x %d = %d\t" % (row, col, row * col),end='')
    print('')
