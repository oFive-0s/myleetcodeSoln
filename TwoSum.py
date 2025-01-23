class Solution:
    # Method to find two numbers in 'nums' that add up to the 'target'
    def twoSum(self, nums, target):
        # Dictionary to store numbers and their respective indices
        num_to_index = {}

        # Iterate over the list of numbers along with their index
        for index, num in enumerate(nums):
            # Calculate the complement (what we need to add to 'num' to reach 'target')
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
                # If found, return the indices of the complement and the current number
                return [num_to_index[complement], index]
            
            # If not found, store the number with its index in the dictionary
            num_to_index[num] = index

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]  # List of numbers
target = 9  # The target sum we're looking for
result = solution.twoSum(nums, target)  # Find the two numbers that sum to the target
print(result)  # Output the result, which should be [0, 1] (since 2 + 7 = 9)
