class MoneySums:
    
    def __init__(self, coins: list[int]):
        self.coins = coins
        
    def get_combinations(self, start: int, target_sum: int, current: list[int], all_sums: set[int]) -> None:
        all_sums.add(target_sum)
        
        for i in range(start, len(self.coins)):
            current.append(self.coins[i])
            self.get_combinations(i + 1, target_sum + self.coins[i], current, all_sums)
            current.pop()
    
    def get_money_sums(self) -> str:
        all_sums = set()
        self.get_combinations(0, 0, [], all_sums)
        all_sums.remove(0)
        return " ".join(str(x) for x in sorted(all_sums))
    
if __name__ == "__main__":
    number_of_coins = int(input(""))
    input_coins = list(input(""))
    input_coins = [int(i) for i in input_coins]
    print(input_coins)
    money_sums = MoneySums(input_coins)
    print(money_sums.get_money_sums())