import statistics

numbers = [10, 20, 30, 20, 40, 50, 20]


# Function 1: Calculate the sum
def calculate_sum(numbers):
    return sum(numbers)


# Function 2: Calculate the average (mean)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


# Function 3: Calculate median and mode
def calculate_median_mode(numbers):
    median = statistics.median(numbers)
    mode = statistics.multimode(numbers)

    return median, mode


# Call the three functions
if len(numbers) > 0:

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    median, mode = calculate_median_mode(numbers)

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Mean:", average)
    print("Median:", median)
    print("Mode:", mode)

else:
    print("The list is empty!")