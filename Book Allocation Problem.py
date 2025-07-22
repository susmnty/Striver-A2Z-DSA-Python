def is_valid(arr: list[int], n: int, m: int, max_pages: int) -> bool:
    """
    Check if it's possible to allocate books to at most m students
    so that no student reads more than max_pages, with contiguous allocation.
    """
    students = 1
    pages_sum = 0
    
    for p in arr:
        # If any single book exceeds max_pages, it's invalid
        if p > max_pages:
            return False
        if pages_sum + p > max_pages:
            # Assign current book to next student
            students += 1
            pages_sum = p
            if students > m:
                return False
        else:
            pages_sum += p
    
    return True

def findPages(arr: list[int], n: int, m: int) -> int:
    """
    Finds the minimum possible maximum pages assigned to any student
    when distributing n books among m students in contiguous fashion.
    Returns -1 if allocation isn't possible (e.g., more students than books).
    """
    # Edge case: more students than books
    if m > n:
        return -1
    
    low = max(arr)      # Lower bound: the biggest single book
    high = sum(arr)     # Upper bound: all books to one student
    
    answer = -1
    while low <= high:
        mid = (low + high) // 2
        # If valid allocation under mid, try smaller max
        if is_valid(arr, n, m, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return answer
