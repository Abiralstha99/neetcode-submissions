class TimeMap:
    # 1. Initialise a hashmap for storing key and value 
    # 2. Use a list for storing value i.e. (val, time)
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If exist append to the list
        if key in self.dict:
            val = (value, timestamp)
            self.dict[key].append(val)
        else:
            self.dict[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            data = self.dict[key]
            # Now apply binary search 
            left = 0
            right = len(data) - 1
            while(left <= right):
                mid = (left + right) // 2
                if (data[mid][1] == timestamp):
                    return data[mid][0]
                elif (data[mid][1] < timestamp):
                    left = mid + 1
                else:
                    right = mid - 1
            if right >= 0:
                return data[right][0]
        
        return ""




