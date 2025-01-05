def monotonicDecreasing(nums):
    stack = []
    result = []

    # Traverse the array
    for num in nums:
        # While stack is not empty AND top of stack is less than the current element
        while stack and stack[-1] < num:
            # Pop the top element from the stack
            stack.pop()
        
        # Construct the result array
        if stack:
            result.append(stack[-1])
        # else:
        #     result.append(0)
        
        # Push the current element into the stack
        print(f'Before push: {stack}')
        stack.append(num)

    return result

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6]
result = monotonicDecreasing(nums)
print("Monotonic decreasing stack:", result)