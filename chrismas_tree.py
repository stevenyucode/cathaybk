
n = 5  

for i in range(1, n+1):
    # 起始點
    print(' ' * (n-i), end='')

    # *0的重複次數
    print('*0' * (i-1) + '*')
