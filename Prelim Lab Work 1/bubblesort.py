import time

def bubble_sort_descending(arr):
    """
    Sorts an array in descending order using the bubble sort algorithm.
    """
    start_time = time.perf_counter()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    time_taken = time.perf_counter() - start_time
    return arr, time_taken


def read_dataset(filename):
    """
    Reads numbers from a file (one number per line).
    """
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]


# Main execution
if __name__ == "__main__":
    program_start = time.perf_counter()  # ⏱ Program timer starts

    print("Reading dataset from file...")
    dataset_file = "dataset.txt"

    try:
        data = read_dataset(dataset_file)
        print(f"Dataset loaded: {len(data)} elements")
        print(f"First 10 elements: {data[:10]}")
        print(f"Last 10 elements: {data[-10:]}")
        print()

        print("Sorting in descending order...")
        sorted_data, sort_time = bubble_sort_descending(data.copy())

        print("=" * 60)
        print("SORTED DATA (DESCENDING ORDER)")
        print("=" * 60)
        print(f"Total elements sorted: {len(sorted_data)}")
        print(f"Bubble sort time: {sort_time:.6f} seconds")
        print("-" * 60)

        for i, value in enumerate(sorted_data, 1):
            print(value, end=" ")
            if i % 20 == 0:
                print()

        print("\n" + "-" * 60)

        is_sorted = all(
            sorted_data[i] >= sorted_data[i + 1]
            for i in range(len(sorted_data) - 1)
        )
        print(f"Correctly sorted in descending order: {is_sorted}")

    except FileNotFoundError:
        print(f"Error: File '{dataset_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

    program_end = time.perf_counter()  # ⏱ Program timer ends
    print(f"\nTotal program execution time: {program_end - program_start:.6f} seconds")
