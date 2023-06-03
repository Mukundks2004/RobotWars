from random import Random

class Robot:

    def __init__(self):
        self.grid = []
        self.place = []
        for n in range(10):
            K = []
            for m in range(10):
                K.append('.')
            self.place.append(K)
                

    def generate_placements(self) -> list[tuple[str, str]]:
        board = []
        for n in range(10):
            K = []
            for m in range(10):
                K.append('.')
            board.append(K)
        
        L = [4, 5, 3, 3, 2]
        sols = []
        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  
        for ship in L:
            #print(ship)
            run = True
            direction = Random().choice(["across", "down"])
            
            while run:
                works = True
                a = Random().randint(0, 8)
                b = Random().randint(0, 8)
                #print(a,b, direction, ship)
                for m in range(ship):
                    if direction == "across" and (b + ship < 11):
                        if board[a][b + m] == 'X':
                            works = False
                            #input("out")
                            break
                    elif direction == "down" and (a + ship < 11):
                        if board[a + m][b] == 'X':
                            works = False
                            #input("in")
                            break
                    else:
                        works = False
                        break
                if works:
                    run = False

                    if direction == "across":
                        for m in range(ship):
                            board[a][b + m] = 'X'
                            
                    else:
                        for m in range(ship):
                            board[a + m][b] = 'X'
                    
                            
                    sols.append((char[a] + str(b + 1), direction))
                    
                    
        #print("done")
        return sols


    def get_attack(self) -> str:
        a = Random().randint(0, 9)
        b = Random().randint(1, 10)

        char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        coord = char[a] + str(b)
        if coord in self.grid:
            return Robot.get_attack(self)
        else:
            self.grid.append(coord)
            return coord
        
    def give_result(self, result: str, board_state: list[list[str]]) -> None:
        pass
