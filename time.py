import time

# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Hashing (using dictionary)
def hashing_search(hash_table, key):
    return hash_table.get(key, -1)

# MAIN MENU
def main():
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    key = int(input("Enter number to search: "))
    
    while True:
        print("\n--- MENU ---")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Hashing")
        print("4. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            start = time.time()
            result = linear_search(arr, key)
            end = time.time()
            
            print("Result:", result)
            print("Time taken:", end - start)
        
        elif choice == 2:
            arr.sort()
            start = time.time()
            result = binary_search(arr, key)
            end = time.time()
            
            print("Result:", result)
            print("Time taken:", end - start)
        
        elif choice == 3:
            hash_table = {arr[i]: i for i in range(len(arr))}
            
            start = time.time()
            result = hashing_search(hash_table, key)
            end = time.time()
            
            print("Result:", result)
            print("Time taken:", end - start)
        
        elif choice == 4:
            break
        else:
            print("Invalid choice")

main()