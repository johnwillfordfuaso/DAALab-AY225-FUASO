class SortingAlgorithms:
    """Sorting algorithms implemented from scratch"""
    
    @staticmethod
    def bubble_sort(data, compare_func):
        """Bubble Sort - O(n²)"""
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if compare_func(data[j], data[j + 1]) > 0:
                    data[j], data[j + 1] = data[j + 1], data[j]
    
    @staticmethod
    def insertion_sort(data, compare_func):
        """Insertion Sort - O(n²)"""
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and compare_func(data[j], key) > 0:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    
    @staticmethod
    def merge_sort(data, compare_func):
        """Merge Sort - O(n log n)"""
        if len(data) <= 1:
            return
        
        def merge_sort_helper(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort_helper(arr, left, mid)
                merge_sort_helper(arr, mid + 1, right)
                merge(arr, left, mid, right)
        
        def merge(arr, left, mid, right):
            left_arr = arr[left:mid + 1]
            right_arr = arr[mid + 1:right + 1]
            
            i = j = 0
            k = left
            
            while i < len(left_arr) and j < len(right_arr):
                if compare_func(left_arr[i], right_arr[j]) <= 0:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1
            
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1
            
            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
        
        merge_sort_helper(data, 0, len(data) - 1)
