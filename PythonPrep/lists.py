class MyList:
    def __init__(self):
        self.list = []

    def append(self, newItem):
        self.list.append(newItem)


new_list = MyList()
new_list.append(1)
new_list.append(2)
print(str(new_list))