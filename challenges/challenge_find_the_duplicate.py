def find_duplicate(nums):
    if not nums or not all(isinstance(num, int) for num in nums):
        return False

    seen = set()
    for num in nums:
        if num < 0 or num > len(nums) - 1:
            return False
        if num in seen:
            return num
        seen.add(num)
    return False
