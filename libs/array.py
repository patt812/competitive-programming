import typing

# Sort array by insertion sort
def insertionSort(a: typing.List[int]) -> None:
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v

# Sort array by insertion sort in descending order
def insertionSort(a: typing.List[int], descending: bool) -> None:
    if not descending:
        insertionSort(a)
        return

    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] < v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v

