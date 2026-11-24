from random import randint


class Lotto:
    def __init__(self):
        self.lotto_numbers: list[int] = []
    
    
    def lotto_numbers_generator(self) -> list[int]:
        while len(self.lotto_numbers) < 6:
            number = randint(1,49)
            if not number in self.lotto_numbers:
                self.lotto_numbers.append(number)
        return self.lotto_numbers


class Ticket:
    def __init__(self):
        self.numbers = self.user_input()
        
       
    def user_input(self) -> list[int]:
        player_numbers: list[int] = []
        
        while len(player_numbers) < 6:
            number = int(input("Introduceti un numar de la 1 la 49: "))
        
            if 0 < number < 50 and isinstance(number, int):
                if not number in player_numbers:
                    player_numbers.append(number)
        
        return player_numbers

lotto1 = Lotto()
lotto1.lotto_numbers_generator()

player1 = Ticket()

def guessed_number(winning_numbers: list[int], player_numbers: list[int]) -> str:
    numbers_guessed = 0
    for player_number in player_numbers:
        if player_number in winning_numbers:
            numbers_guessed += 1
            
    match numbers_guessed:
        case 1: 
            return "You have 1 guessed number!"
        case 2: 
            return "You have 2 guessed number!"
        case 3: 
            return "You have 3 guessed number!"
        case 4: 
            return "You have 4 guessed number!"
        case 5: 
            return "You have 5 guessed number!"
        case 6: 
            return "You have won the lottery!"
        case 0:
            return "Better luck next time"

print(guessed_number(lotto1.lotto_numbers, player1.numbers))