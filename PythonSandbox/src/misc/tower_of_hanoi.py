class TowerOfHanoi:
    """
    n: num disks
    f: from name
    a: auxilary name
    f: to name
    """
    def hanoi(self, n, f, a, t):
        moves = []
        self.hanoiHelper(n, f, a, t, moves)
        return moves
    
    def hanoiHelper(self, n, f, a, t, moves):
        if n==0:
            return
        # moves A->B (assuming f->t movement from root call, then f->a is A->B)
        self.hanoiHelper(n-1, f, t, a, moves)
        # moves A->C (assuming f->t movement from root call, then f->t is A->C)
        moves.append((f,t))
        # moves B->C (assuming f->t movement from root call, then a->t is B->C)
        self.hanoiHelper(n-1, a, f, t, moves)

    def testHanoi(self):
        moves = self.hanoi(4, "A", "B", "C")
        for ind,move in enumerate(moves):
            print("move {}: {}".format(ind+1, move))
    
    # demonstrate that the number of moves, y, follows the equation: y = (2^n)-1
    def testHanoiNumberMoves(self):
        games = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        for n in games:
            moves = self.hanoi(n, "A", "B", "C")
            y = (2**n) - 1
            print("moves for {} discs: {}".format(n, len(moves)))
            print("y = (2^{})-1 = {}".format(n, y))
            print("")

def main():
    toh = TowerOfHanoi()
    #toh.testHanoi()
    toh.testHanoiNumberMoves()

if __name__ == "__main__":
    main()