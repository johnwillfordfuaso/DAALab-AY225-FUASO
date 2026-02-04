from data_loader import DataLoader
from benchmark_engine import BenchmarkEngine, SortColumn, SortAlgorithm
import csv
from datetime import datetime
import os

def display_header():
    """Display application header"""
    print("\nSorting Algorithm Benchmarking Tool")
    print("(Bubble, Insertion, Merge Sort)\n")

def get_num_rows():
    """Get number of rows to load from user"""
    while True:
        try:
            num = int(input("Enter number of rows to load (or -1 for all): "))
            if num >= -1:
                return num if num != -1 else None
            print("Invalid input. Please enter a positive number or -1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_sort_column():
    """Get sort column from user"""
    print("\nSelect column to sort by:")
    print("1. ID")
    print("2. FirstName")
    print("3. LastName")
    
    while True:
        choice = input("Choice (1-3): ")
        if choice == "1":
            return SortColumn.ID
        elif choice == "2":
            return SortColumn.FIRST_NAME
        elif choice == "3":
            return SortColumn.LAST_NAME
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_algorithms_to_run():
    """Get which algorithms user wants to run"""
    print("\nSelect Sorting Algorithms:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Merge Sort")
    print("4. All")
    
    while True:
        choice = input("Choice (1-4): ").strip()
        
        if choice == "1":
            return [SortAlgorithm.BUBBLE_SORT]
        elif choice == "2":
            return [SortAlgorithm.INSERTION_SORT]
        elif choice == "3":
            return [SortAlgorithm.MERGE_SORT]
        elif choice == "4":
            return [SortAlgorithm.BUBBLE_SORT, SortAlgorithm.INSERTION_SORT, SortAlgorithm.MERGE_SORT]
        else:
            print("Invalid choice. Please enter 1-4.")

def format_time(milliseconds):
    """Convert milliseconds to seconds or minutes"""
    seconds = milliseconds / 1000
    if seconds < 60:
        return f"{seconds:.2f}s"
    else:
        minutes = seconds / 60
        return f"{minutes:.2f}m"

def display_results(results, sort_column):
    """Display benchmark results"""
    print("\nBENCHMARK RESULTS\n")
    
    print(f"Records Sorted: {results[0].record_count:,}")
    print(f"Sorted By: {sort_column.name}\n")
    
    sorted_results = sorted(results, key=lambda x: x.sort_time_ms)
    
    print("Algorithm               Time")
    print("-" * 35)
    for result in sorted_results:
        time_str = format_time(result.sort_time_ms)
        print(f"{result.algorithm_name:<20} {time_str:>12}")
    print()
    
    print("First 10 Sorted Records\n")
    print(f"{'ID':<12} {'FirstName':<20} {'LastName':<20}")
    for person in sorted_results[0].sorted_data[:10]:
        print(person)
    
    return sorted_results

def save_results_to_csv(results, sort_column):
    """Save benchmark results to CSV file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"benchmark_results_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Algorithm', 'Time (ms)', 'Record Count', 'Sorted By'])
            for result in results:
                writer.writerow([result.algorithm_name, f"{result.sort_time_ms:.2f}", 
                               result.record_count, sort_column.name])
        
        print(f"Results saved to: {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")

def save_sorted_data_to_csv(sorted_data, algorithm_name, sort_column):
    """Save sorted data to CSV file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sorted_data_{algorithm_name.replace(' ', '_')}_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'FirstName', 'LastName'])
            for person in sorted_data:
                writer.writerow([person.id, person.first_name, person.last_name])
        
        print(f"Sorted data saved to: {filename}")
    except Exception as e:
        print(f"Error saving sorted data: {e}")

def post_sort_menu(results, sort_column):
    """Display menu options after sorting"""
    while True:
        print("\nOptions:")
        print("1. View full sorted data")
        print("2. Save benchmark results")
        print("3. Save sorted data")
        print("4. Run another benchmark")
        print("5. Exit")
        
        choice = input("Choice (1-5): ").strip()
        
        if choice == "1":
            sorted_results = sorted(results, key=lambda x: x.sort_time_ms)
            print(f"\nFull Sorted Data ({len(sorted_results[0].sorted_data):,} records)\n")
            print(f"{'ID':<12} {'FirstName':<20} {'LastName':<20}")
            for person in sorted_results[0].sorted_data:
                print(person)
        
        elif choice == "2":
            save_results_to_csv(results, sort_column)
        
        elif choice == "3":
            sorted_results = sorted(results, key=lambda x: x.sort_time_ms)
            save_sorted_data_to_csv(sorted_results[0].sorted_data, 
                                   sorted_results[0].algorithm_name, 
                                   sort_column)
        
        elif choice == "4":
            return True
        
        elif choice == "5":
            print("\nExit")
            return False
        
        else:
            print("Invalid choice. Please enter 1-5.")

def main():
    """Main application"""
    display_header()
    
    # Get CSV path from current directory
    csv_path = os.path.join(os.path.dirname(__file__), "generated_data.csv")
    
    while True:
        num_rows = get_num_rows()
        
        print("\nLoading data...")
        data, load_time = DataLoader.load_csv(csv_path, num_rows)
        
        if not data:
            print("Failed to load data.")
            return
        
        load_time_str = format_time(load_time)
        print(f"Loaded {len(data):,} records in {load_time_str}")
        
        sort_column = get_sort_column()
        algorithms = get_algorithms_to_run()
        
        print("\nRunning benchmarks...\n")
        
        results = []
        try:
            for algorithm in algorithms:
                print(f"Running {algorithm.value}...")
                result = BenchmarkEngine.run_benchmark(data, algorithm, sort_column)
                results.append(result)
                time_str = format_time(result.sort_time_ms)
                print(f"Completed in {time_str}")
        except Exception as e:
            print(f"Error during sorting: {e}")
            return
        
        sorted_results = display_results(results, sort_column)
        
        if not post_sort_menu(results, sort_column):
            break

if __name__ == "__main__":
    main()