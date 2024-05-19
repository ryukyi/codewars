# Write a function that given, an array arr, returns an array containing 
# at each index i the amount of numbers that are smaller than arr[i] to the right.

# For example:

# * Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
# * Input [1, 2, 0] => Output [1, 1, 0]
# If you've completed this one and you feel like testing your performance 
# tuning of this same kata, head over to the much tougher version 
# How many are smaller than me II?

def smaller_generator(arr):
    def count_smaller(i):
        counter = 0
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                counter += 1
        return counter
    
    for i in range(len(arr)):
        yield count_smaller(i)

def smaller(arr):
    return list(smaller_generator(arr))

if __name__ == "__main__":
    print(smaller([5, 4, 3, 2, 1]))