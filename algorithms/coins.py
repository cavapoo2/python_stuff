def coins(n):
    result = 0
    coin = [0] * (n + 1)
    for i in range(1, n + 1):
        k = i
        print('k=',k,',i=',i)
        while (k <= n):
            coin[k] = (coin[k] + 1) % 2
            k += i
            print(coin)
        result += coin[i]
    return result

res = coins(5)
print(res)
