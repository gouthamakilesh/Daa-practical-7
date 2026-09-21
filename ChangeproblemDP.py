def making_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]


n = int(input("Enter the number of coin denominations: "))

print("Enter the coin denominations:")
coins = []

for i in range(n):
    coins.append(int(input()))

amount = int(input("Enter the amount: "))

minimum_coins = making_change(coins, amount)

if minimum_coins == float('inf'):
    print("Change cannot be made for the given amount.")
else:
    print("\nMinimum number of coins required:", minimum_coins)

print("EN.No:92460118683")