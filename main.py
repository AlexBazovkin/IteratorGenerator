from decorator import logger


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class MyClass:
    def __init__(self, incoming_list, x: int = 0, y: int = 0):
        self.incoming_list = incoming_list
        self.x = x
        self.y = y

    def __iter__(self):
        return self

    def __next__(self):
        if self.x != len(self.incoming_list):
            if self.y < len(self.incoming_list[self.x]):
                result = self.incoming_list[self.x][self.y]
                self.y += 1
                if self.y == len(self.incoming_list[self.x]):
                    self.y -= len(self.incoming_list[self.x])
                    self.x += 1
                return result

        else:
            raise StopIteration


# # Вывод каждого элемента -----------------
# for item in MyClass(nested_list):
#     print(item)
#
# print("*"*20)

# Вывод в одну строку -------------------
@logger()
def make_flat_list(some_data):
    flat_list = [item for item in some_data]
    return flat_list


print(make_flat_list(MyClass(nested_list)))

# print("*"*30)
#
#
# # Создание и вывод генератора ----------------
# def flat_generator(incoming_list):
#     for list_ in incoming_list:
#         for el in list_:
#             yield el
#
#
# for item in flat_generator(nested_list):
#     print(item)
