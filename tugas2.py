def greedy_change(amount):
    denominations = [50000, 20000, 10000, 5000, 2000, 1000]

    result = {}

    for coin in denominations:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin

    return result

# Input dari pengguna
money = int(input("Masukkan jumlah kembalian (Rp): "))

change = greedy_change(money)

print("\nJumlah Kembalian : Rp", format(money, ","))

print("\nPecahan yang digunakan:")
for coin, count in change.items():
    print(f"Rp{coin:,} x {count}")