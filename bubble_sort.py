# Bubble Sort Class
class BubbleSort:
    @staticmethod
    def sort(items, type="age"):
        type_index = 2 if type == "age" else 0
        for i in range(len(items)):
            for j in range(len(items) - 1):
                if items[j][type_index] > items[j + 1][type_index]:
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items
