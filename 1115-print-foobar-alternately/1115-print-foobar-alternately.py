from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_foo = Lock()
        self.lock_bar = Lock()
        self.lock_bar.acquire() # bar locked, foo unlocked.

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_foo.acquire() # acquire foo lock
            printFoo() # do work
            self.lock_bar.release() # release other lock


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_bar.acquire() # acquire bar lock
            printBar() # do bar work
            self.lock_foo.release() # release other lock
