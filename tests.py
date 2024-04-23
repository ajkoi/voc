class A():
    def __init__(self) -> None:
        print("class A")
    def test(self) -> None:
        print('test')
    
class B(A):
    def __init__(self) -> None:
        super().__init__()
    
t = B()
t.test()