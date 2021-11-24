import threading 

rs = []
lock = threading.RLock ()

class Isprime (threading.Thread):

    def __init__ (self, num, name = None):
        threading.Thread .__init__ (self)
        self.num = num
        self.isstop = False
    
    def run (self):
        global rs, lock          
        isprime = False     
        m = self.num 
        for i in range (2, m//2 + 1):
            if m% i == 0:
                isprime = True
                break 
        lock.acquire ()
        if not isprime:
            rs.append (m)
        lock.release ()
                
def main (n):
    global rs 
    threads = []

    for i in range (2, n): 
        threads.append (Isprime (i))
    print(threads)
    for x in threads:
        x.start ()

    for s in threads:
        x.join ()
  
    print(rs)

n = int(input('Enter n: '))
main (n)