def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
    elementsLessThanPivot = []
    elementsEqualToPivot = []
    elementsMoreThanPivot = []

    # Partition the elements based on the pivot value
    # Elements less than the pivot go to the left
    # Elements equal to the pivot go to the middle
    # Elements greater than the pivot go to the right
    for i in range(len(nums)):
        if nums[i] < pivot:
            elementsLessThanPivot.append(nums[i])
        elif nums[i] > pivot:
            elementsMoreThanPivot.append(nums[i])
        else:
            elementsEqualToPivot.append(nums[i])
    
    return elementsLessThanPivot + elementsEqualToPivot + elementsMoreThanPivot

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(n). The space complexity is due to the three lists elementsLessThanPivot, elementsEqualToPivot, and elementsMoreThanPivot, which store the elements less than, equal to, and greater than the pivot, respectively. The total space used by these lists is O(n).