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
        self.hanoiHelper(n-1, f, t, a, moves)
        moves.append((f,t))
        self.hanoiHelper(n-1, a, f, t, moves)

    def testHanoi(self):
        moves = self.hanoi(4, "A", "B", "C")
        for ind,move in enumerate(moves):
            print("move {}: {}".format(ind+1, move))

def main():
    toh = TowerOfHanoi()
    toh.testHanoi()

if __name__ == "__main__":
    main()