import numpy as np

def knapsack(uang, buah):
    n = len(buah)
    w = np.zeros((n + 1, uang + 1))

    for i in range(1, n + 1):
        for j in range(1, uang + 1):
            if buah[i-1]['harga'] <= j:
                w[i][j] = max(w[i-1][j], w[i-1][j - buah[i-1]['harga']] + buah[i-1]['kalori'])
            else:
                w[i][j] = w[i-1][j]

    return w[n][uang]

if __name__ == '__main__':
    uang = 25000
    buah = [
        {'nama': 'apel', 'kalori': 91, 'harga': 2360, 'stok': 3},
        {'nama': 'jeruk', 'kalori': 71, 'harga': 2120, 'stok': 3},
        {'nama': 'pisang', 'kalori': 105, 'harga': 1890, 'stok': 5},
        {'nama': 'kiwi', 'kalori': 103, 'harga': 3770, 'stok': 10},
        {'nama': 'mangga', 'kalori': 96, 'harga': 2870, 'stok': 5}
    ]

    result = knapsack(uang, buah)
    print(result)
