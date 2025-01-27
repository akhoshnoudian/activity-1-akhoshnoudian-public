class Vehicle:
    def __init__(self, manufacturer, model, v_type, cost, mileage):
        self.manufacturer = manufacturer
        self.model = model
        self.v_type = v_type
        self.cost = cost
        self.mileage = mileage

    def __repr__(self):
        return (f"Vehicle(manufacturer={self.manufacturer}, model={self.model}, type={self.v_type}, "
                f"cost={self.cost}, mileage={self.mileage})")

    def __lt__(self, other):
        return self.cost < other.cost  # Default comparison (can be customized)


def selection_sort(lst, key=lambda x: x):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key(lst[j]) < key(lst[min_idx]):
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def bubble_sort(lst, key=lambda x: x):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if key(lst[j]) > key(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


def merge_sort(lst, key=lambda x: x):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid], key=key)
    right = merge_sort(lst[mid:], key=key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def sort(lst, alg, key=lambda x: x):
    return alg(lst[:], key=key)  # Return a sorted copy of the list


