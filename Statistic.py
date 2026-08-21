"""
Sorting 
Quick comparison:
         |Bubble	           | Selection	   | Insertion
Idea     |Swap neighbors     | Pick the min  | Insert into place
Best for | Learning concepts | Simple lists  | Nearly sorted data
Speed	   |Slow	             | Slow	         | Fast if nearly sorted

All three are simple but slow on large lists — that's why real programs use built-in sorts (which use faster algorithms like Merge Sort or Quick Sort under the hood).
"""
#Bubble Sort
"""
Compares two neighbors side by side, and swaps them if they're in the wrong order. Repeats this over and over until nothing needs swapping — like bubbles rising to the top.

[5, 3, 8, 1]
 ↑  ↑         → 5 > 3? swap → [3, 5, 8, 1]
    ↑  ↑      → 5 > 8? no   → [3, 5, 8, 1]
       ↑  ↑   → 8 > 1? swap → [3, 5, 1, 8]
Repeat again... until sorted → [1, 3, 5, 8]

Think of it as: keep swapping neighbors until done.
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#Selection Sort
"""
Scans the whole list to find the smallest number, then puts it at the front. Then finds the next smallest, puts it second. Repeats until done.
[5, 3, 8, 1] → find smallest (1) → swap with first → [1, 3, 8, 5]
[_, 3, 8, 5] → find smallest (3) → already in place → [1, 3, 8, 5]
[_, _, 8, 5] → find smallest (5) → swap → [1, 3, 5, 8]
Done!

Think of it as: pick the smallest each time and place it.
"""
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Insertion Sort
"""
Works like sorting playing cards in your hand. Pick up one card at a time and insert it into its correct position among the already-sorted cards.
[5, 3, 8, 1]
 ✓            → 5 is alone, already "sorted"
 ✓  3         → 3 < 5? insert before → [3, 5, 8, 1]
 ✓  ✓  8      → 8 > 5? stays → [3, 5, 8, 1]
 ✓  ✓  ✓  1  → 1 < everything? insert at front → [1, 3, 5, 8]
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
