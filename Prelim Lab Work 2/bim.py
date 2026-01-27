import time
import sys

# Increase recursion depth for merge sort to handle 10,000 items
sys.setrecursionlimit(20000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def load_data():
    """Extracts numeric values from dataset.txt"""
    nums = []
    try:
        with open('dataset.txt', 'r') as f:
            for line in f:
                content = line.strip()
                if not content: continue
                # Remove tags if present
                if ']' in content:
                    content = content.split(']')[-1].strip()
                if content.isdigit():
                    nums.append(int(content))
        return nums
    except FileNotFoundError:
        print("Error: dataset.txt not found in the current directory.")
        return []

def display_data(arr):
    """Displays the entire dataset in a single column"""
    print("\n--- Sorted Results (1 Column) ---")
    for val in arr:
        print(val)
    print("---------------------------------")

def menu():
    while True:
        print("\n=== Sorting Menu ===")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Merge Sort")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '4':
            print("Goodbye!")
            break
            
        data = load_data()
        if not data:
            continue
            
        print(f"Sorting {len(data)} items...")
        start_time = time.time()
        
        if choice == '1':
            bubble_sort(data)
            algo_name = "Bubble Sort"
        elif choice == '2':
            insertion_sort(data)
            algo_name = "Insertion Sort"
        elif choice == '3':
            merge_sort(data)
            algo_name = "Merge Sort"
        else:
            print("Invalid selection. Please run in a Terminal to type choices.")
            continue
            
        end_time = time.time()
        
        # Automatically display data after sorting
        display_data(data)
        
        print(f"\nAlgorithm: {algo_name}")
        print(f"Time Spent: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    menu()