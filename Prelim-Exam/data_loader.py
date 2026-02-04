import time
from person import Person

class DataLoader:
    """Load CSV data with timing"""
    
    @staticmethod
    def load_csv(file_path, num_rows=None):
        """
        Load CSV file and return data with load time
        
        Args:
            file_path: Path to CSV file
            num_rows: Number of rows to load (None for all)
        
        Returns:
            Tuple of (data list, load time in ms)
        """
        start_time = time.time()
        data = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Skip header
                next(f)
                
                row_count = 0
                for line in f:
                    if num_rows and row_count >= num_rows:
                        break
                    
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        try:
                            person = Person(parts[0], parts[1], parts[2])
                            data.append(person)
                            row_count += 1
                        except (ValueError, IndexError):
                            continue
        
        except FileNotFoundError:
            print(f"❌ Error: File not found at {file_path}")
            return [], 0
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
            return [], 0
        
        load_time = (time.time() - start_time) * 1000  # Convert to ms
        return data, load_time
