class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        # print('Start')
        self.counter = 0
        self.counter_too = -1
        return self

    def __next__(self):
        self.counter_too += 1
        if self.counter_too == len(self.list_of_list[self.counter]):
            self.counter += 1
            self.counter_too = 0
        # print(self.counter)
        if self.counter == len(self.list_of_list):
            raise StopIteration
        return self.list_of_list[self.counter][self.counter_too]


def test_1():
    list_of_lists_1 = [
        ["a", "b", "c"],
        ["d", "e", "f", "h", False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None, ]
    # print(list_of_lists_1)
    # print('fin')

if __name__ == "__main__":
    test_1()
