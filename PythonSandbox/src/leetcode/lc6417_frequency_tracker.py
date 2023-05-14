class FrequencyTracker:

    def __init__(self):
        self.freqMap = {} # map: number -> frequency
        self.freqToNum = {} # map: freq -> set(numbers)

    def add(self, number: int) -> None:
        if number in self.freqMap.keys():
            f1 = self.freqMap[number]
            if f1 in self.freqToNum.keys():
                if number in self.freqToNum[f1]:
                    self.freqToNum[f1].remove(number)
                
            self.freqMap[number] += 1
        else:
            self.freqMap[number] = 1
        
        f2 = self.freqMap[number]
        if f2 in self.freqToNum.keys():
            self.freqToNum[f2].add(number)
        else:
            self.freqToNum[f2] = set([number])
        
    def deleteOne(self, number: int) -> None:
        if number in self.freqMap.keys():
            f1 = self.freqMap[number]
            
            if f1 in self.freqToNum.keys():
                self.freqToNum[f1].remove(number)
            
            if f1 > 0:
                self.freqMap[number] -= 1
            else:
                self.freqMap[number] = 0

            f2 = self.freqMap[number]
            if f2 in self.freqToNum.keys():
                self.freqToNum[f2].add(number)
            else:
                self.freqToNum[f2] = set([number])
        
    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freqToNum.keys() and len(self.freqToNum[frequency]) > 0:
            return True
        return False