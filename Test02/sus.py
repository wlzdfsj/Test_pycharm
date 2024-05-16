class Base:
    def test(self):
        print('----Base----')

class A(Base):
    def test(self):
        print('AAAAAAAAAA')

class B(Base):
    def test1(self):
        print('BBBBBBBBBB')

class C(Base):#C继承A和B
    def test2(self):
        print('CCCCCCC')
class D(A,B,C):
    pass

d = D()
d.test() #结果打印的是AAAAAA