# class ClassDecorator(object):

#     def __init__(self, function, arg1=5, arg2=6):
#         print("Arguements passed to decorator %s and %s" % (arg1, arg2))
#         self.arg1 = arg1
#         self.arg2 = arg2

#     def __call__(self, foo, *args, **kwargs):
#         pass

#     def inner_func(*args, **kwargs):
#         print("Args passed inside decorated function .%s and %s" % (self.arg1, self.arg2))
#         return foo(*args, **kwargs)
#         return inner_func

# class IsQueueEmpty:
#     def __init__(self, function, a=5, b=6, *args, **kwargs):
#         self.function = function
#         self.a = a
#         self.b = b

#     def __call__(self, obj, *args, **kwargs):
#         import pdb
#         pdb.set_trace()
#         if obj.queue:
#             return self.function(*args, **kwargs)
#         else:
#             print("queue is empty")
#             return
        
    # def inner_func(self, *args, **kwargs):
    #     if self:
    #         print("Args passed inside decorated function .%s and %s" % (self.arg1, self.arg2))
    #         return self.function(*args, **kwargs)
    #     return inner_func

    # def __get__(self, obj, type=None):
    #     if obj is None:
    #         return self
    #     def bound_decorated(*args):
    #         return self.__call__(obj, *args)
    #     return bound_decorated

    
import functools

# class IsQueueEmpty:
#     def __init__(self, orignal_function, ndecorator_argument=None):
#         """
#         Instantiation of decorator_object, like decorator_object = DecoratorClass(arg)
#         :param arg: Argument of decorator.
#         """
#         self.orignal_function = original_function
#         self.decorator_argument = decorator_argument

#     def __call__(self, orignal_function, decorator_argument=None):
#         """
#         Called when the decorator_object gets called, like decorator_closure = decorator_object(original_function).
#         Returns actual decorator_closure ready to be executed.
#         @decorator syntax executes this step automatically.
#         """

#         def wrapper(obj, *args, **kwargs):
#             # Adds logic before and after the original_function
#             import pdb
#             pdb.set_trace()
#             print('Logic before')
#             result = original_function(*args, **kwargs) # function execution
#             print('Logic after')
#             print(f'Decorator_argument = {self.decorator_argument}')
# 		# Any argument you need is still accessible inside the wrapper

#             return result
#         return wrapper

class IsQueueEmpty:

    def __init__(self, function):
        self.function = function
        # print("Arguements passed to decorator %s and %s" % (arg1, arg2))
        # self.arg1 = arg1
        # self.arg2 = arg2

    def __call__(self, obj, *args, **kwargs):
        print("785")
        if obj.queue:
            return self.function(*args, **kwargs)
        else:
            print("queue empty")
        # def inner_func(*args, **kwargs):
        #     print("nandndsn")
        #     return self.function(*args, **kwargs)
        # return inner_func

    def __get__(self, obj, type=None):
        if not obj:
            return self
        def bound_decorated(*args):
            return self.__call__(obj, *args)
        return bound_decorated


is_queue_empty = IsQueueEmpty

class Queue:

    def __init__(self):
        self.queue = []

    def _push_into_stack(self) -> None:
        element = int(input("Enter the element to be pushed into the queue\n"))
        self.queue.append(element)

    @is_queue_empty
    # @IsQueueEmpty    
    def __pop_from_queue(self) -> None:
        self.queue.pop(0)

    # @is_queue_empty()
    @IsQueueEmpty
    def __peek_from_queue(self) -> None:
        print(self.queue[-1])
    
    # @is_queue_empty()
    @IsQueueEmpty
    def __display_queue(self) -> None:
        print("\n".join(list(map(str, self.queue))))

    def __call__(self) -> None:
        while True:
            print("1. push into queue\n2. pop from queue\n3. peek from queue\n4. display queue\n")
            choice = input("Enter your choice\n")

            if choice == "1":
                self._push_into_stack()
            elif choice == "2":
                self.__pop_from_queue()
            elif choice == "3":
                self.__peek_from_queue()
            elif choice == "4":
                self.__display_queue()
            else:
                break


        pass

obj = Queue()
obj()
