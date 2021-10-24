class Foo:
    def __init__(self):
        self.lock = 1


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        while self.lock != 1:
            pass
        printFirst()
        self.lock += 1


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while self.lock != 2:
            pass
        printSecond()
        self.lock += 1


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while self.lock != 3:
            pass
        printThird()
        self.lock += 1