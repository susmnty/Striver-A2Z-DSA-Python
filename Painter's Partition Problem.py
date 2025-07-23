def findLargestMinDistance(boards:list, k:int) -> int:
    def is_possible(limit):
        painters = 1
        curr_sum = 0

        for length in boards:
            if length > limit:
                return False

            if curr_sum + length > limit:
                painters += 1
                curr_sum = length
                if painters > k:
                    return False
            else:
                curr_sum += length

        return True 
    
    low = max(boards)
    high = sum(boards)
    result = high 

    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


    # Write your code here
    # Return an integer