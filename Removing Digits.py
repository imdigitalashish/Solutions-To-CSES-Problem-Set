

class RemoveDigit:
    
    def __init__(self, num: int):
        self.num = num
    
    
    def get_max_of_two_digit(self, num:int) -> int:
        number_array = [int(i) for i in str(num)]
        return max(number_array)
    
    def get_minimum_number_step(self) -> int:
        number_of_steps = 0
        while self.num != 0:
            max_digit = self.get_max_of_two_digit(self.num)
            self.num = self.num - max_digit
            number_of_steps += 1
        return number_of_steps
    
    
if __name__ == "__main__":
    input_number = int(input(""))
    remove_digit = RemoveDigit(input_number)
    print(remove_digit.get_minimum_number_step())
        
        