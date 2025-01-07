def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    return sum(numbers) / len(numbers)