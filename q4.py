# Decorator to print statistics for a list of numbers
def stats_decorator(func):
    def wrapper(t):
        # Call the original function to get the numbers
        numbers_list = func(t)
        # Process and print statistics for each line of numbers
        for numbers in numbers_list:
            print("Numbers read:", numbers)
            print("Count:", len(numbers))
            print("Average:", sum(numbers) / len(numbers) if numbers else 0)
            print("Maximum:", max(numbers) if numbers else "None")
    return wrapper

@stats_decorator
def printStats(t):
    # Open the file, read lines, and convert them into lists of integers
    numbers_list = []
    with open(t, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))
            numbers_list.append(numbers)  # Store each line of numbers
    return numbers_list  # Return the list of numbers for the decorator to process

# Example usage
printStats('numbers.txt')
