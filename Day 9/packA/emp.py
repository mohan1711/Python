class employee:
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def dispemp(self):
        print(self.eid,self.ename,self.sal)
