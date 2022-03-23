import time
from threading import Thread, Lock, Condition

class MyThread(Thread):
    def __init__(self, a: int, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None) -> None:
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self.a = a
        self.lock = Lock()
        # print(kwargs)

    def run(self) -> None:
        for i in range(5):
            time.sleep(self.a)
            # print(Condition(self.lock))
            print(f"Custom Thread - {i+1}")


obj = MyThread(name="Custom Thread Name", a=1, kwargs={"b": 2})
obj.start()
print(obj.getName())
# obj.join()

print("Main Thread Executed")
