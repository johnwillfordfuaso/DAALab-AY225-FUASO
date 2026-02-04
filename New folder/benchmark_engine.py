import time
import copy
from enum import Enum
from sorting_algorithms import SortingAlgorithms

class SortColumn(Enum):
    """Columns available for sorting"""
    ID = 1
    FIRST_NAME = 2
    LAST_NAME = 3

class SortAlgorithm(Enum):
    """Sorting algorithms"""
    BUBBLE_SORT = "Bubble Sort"
    INSERTION_SORT = "Insertion Sort"
    MERGE_SORT = "Merge Sort"

class BenchmarkResult:
    """Store benchmark results"""
    
    def __init__(self, algorithm_name, sort_time_ms, record_count, sorted_data):
        self.algorithm_name = algorithm_name
        self.sort_time_ms = sort_time_ms
        self.record_count = record_count
        self.sorted_data = sorted_data

class BenchmarkEngine:
    """Benchmarking engine for sorting algorithms"""
    
    @staticmethod
    def get_compare_function(sort_column):
        """Get comparison function based on column"""
        if sort_column == SortColumn.ID:
            return lambda a, b: a.id - b.id
        elif sort_column == SortColumn.FIRST_NAME:
            return lambda a, b: -1 if a.first_name < b.first_name else (1 if a.first_name > b.first_name else 0)
        elif sort_column == SortColumn.LAST_NAME:
            return lambda a, b: -1 if a.last_name < b.last_name else (1 if a.last_name > b.last_name else 0)
    
    @staticmethod
    def run_benchmark(data, algorithm, sort_column):
        """
        Run a benchmark for a sorting algorithm
        
        Args:
            data: List of Person objects
            algorithm: SortAlgorithm enum value
            sort_column: SortColumn enum value
        
        Returns:
            BenchmarkResult object
        """
        if not data:
            raise ValueError("Data is empty")
        
        # Warn for O(n²) algorithms with large datasets (BEFORE timing starts)
        if algorithm in [SortAlgorithm.BUBBLE_SORT, SortAlgorithm.INSERTION_SORT] and len(data) > 10000:
            print(f"Warning: {algorithm.value} with {len(data):,} rows may take a very long time.")
        
        # Create a copy of data
        data_copy = copy.deepcopy(data)
        compare_func = BenchmarkEngine.get_compare_function(sort_column)
        
        # Time the sorting (START TIMER AFTER SETUP)
        start_time = time.time()
        
        if algorithm == SortAlgorithm.BUBBLE_SORT:
            SortingAlgorithms.bubble_sort(data_copy, compare_func)
        elif algorithm == SortAlgorithm.INSERTION_SORT:
            SortingAlgorithms.insertion_sort(data_copy, compare_func)
        elif algorithm == SortAlgorithm.MERGE_SORT:
            SortingAlgorithms.merge_sort(data_copy, compare_func)
        
        sort_time = (time.time() - start_time) * 1000  # Convert to ms
        
        return BenchmarkResult(algorithm.value, sort_time, len(data), data_copy)
