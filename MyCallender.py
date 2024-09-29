class MyCalendarTwo:

    def __init__(self):
        self.single=[]
        self.doubble=[]


    def book(self, start: int, end: int) -> bool:
        for s,e in self.doubble:
            if max(start,s)<min(end,e):
                return False

        for s,e in self.single:
            if max(start,s)<min(end,e):
                self.doubble.append((max(start,s),min(end,e)))
        self.single.append((start,end))
        return True