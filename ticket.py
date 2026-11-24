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
    
ticket1 = Ticket()
print(ticket1.numbers)