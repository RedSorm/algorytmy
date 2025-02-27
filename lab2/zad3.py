# Dokonaj symulacji poszczególnych algorytmów sortowania zapisanych w kolejnych arkuszach skoroszytu sortowanie xls.
# Następnie przetestuj podane algorytmy sortowanie w języku python, dla 100 elementowej listy, zawierającej liczby wygenerowane losowe z przedziału od 20 do 70.
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Driver code to test above
if __name__ == "__main__":
    arr = [24,7,15,34,5,18]

    bubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")