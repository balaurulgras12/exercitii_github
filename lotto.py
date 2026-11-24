from random import randint


class Lotto:
    def __init__(self, nume: str, player_numbers: list[int]):
        self.player_numbers = player_numbers
        self.nume = nume
        self.lotto_numbers: list[int] = []
    
    
    def __str__(self):
        return f"Numerele alese de jucatorul {self.nume} sunt {self.player_numbers}"
    
    @property
    def lotto_numbers_generator(self) -> None:
        total_numbers = 6
        
        while total_numbers > 0:
            winning_number = randint(1,49)        
            while winning_number in self.lotto_numbers:
                winning_number = randint(1,49)   
            total_numbers -= 1
            self.lotto_numbers.append(winning_number)

    
    def check_guessed_numbers(self) -> str:
        guessed_number: int = 0
        for player_number in self.player_numbers:
            for lotto_number in self.lotto_numbers:
                if player_number == lotto_number:
                    guessed_number += 1
                    
        if guessed_number == 6:
            return "You have won the Lottery! You can retire now!"
        
        return f"You have guessed {guessed_number} numbers, better luck next time!"
    

player1 = Lotto("Ion", [1,2,3,4,5,6])

print(player1)
player1.lotto_numbers_generator
print(player1.lotto_numbers)
player1.check_guessed_numbers()

            
    
