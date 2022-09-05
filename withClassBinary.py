class binary:
    def __init__(self,list):
        self.list = list
        self.input = list['input']
        self.cards = self.input['cards']
        self.query = self.input['query']
        self.output = list['output']


    def show(self):
        print(self.list)
        print(self.input)
        print(self.cards)
        print(self.query)
        print(self.output)

    def linearSearch(self, cards, query):
        position = 0
        while position < len(cards):
            if cards[position] == query:
                return position
            position += 1
        return -1

    def locate_card(cards, query):
        lo, hi = 0, len(cards) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_number = cards[mid]
            
            print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
            
            if mid_number == query:
                return mid
            elif mid_number < query:
                hi = mid - 1  
            elif mid_number > query:
                lo = mid + 1
        
        return -1
