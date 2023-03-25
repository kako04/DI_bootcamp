class Pagination:
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.currentPage = 1
        self.totalPages = max(1, len(items)//self.pageSize + (1 if len(items)%self.pageSize else 0))
        
    def getVisibleItems(self):
        startIndex = (self.currentPage - 1) * self.pageSize
        endIndex = startIndex + self.pageSize
        return self.items[startIndex:endIndex]
        
    def prevPage(self):
        self.currentPage = max(self.currentPage - 1, 1)
        return self
        
    def nextPage(self):
        self.currentPage = min(self.currentPage + 1, self.totalPages)
        return self
        
    def firstPage(self):
        self.currentPage = 1
        return self
        
    def lastPage(self):
        self.currentPage = self.totalPages
        return self
        
    def goToPage(self, pageNum):
        self.currentPage = min(max(1, int(pageNum)), self.totalPages)
        return self

alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())
p.nextPage().nextPage()
print(p.getVisibleItems()) 
p.lastPage()
print(p.getVisibleItems()) 
p.goToPage(10)
print(p.getVisibleItems())