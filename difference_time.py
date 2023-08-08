from datetime import datetime

def subtract_time_difference(input_string):
    try:
        # Extract timestamps from the input string
        started_str = input_string.split('@started(')[1].split(')')[0]
        done_str = input_string.split('@done(')[1].split(')')[0]

        # Convert timestamps to datetime objects
        started_time = datetime.strptime(started_str, '%y-%m-%d %H:%M')
        done_time = datetime.strptime(done_str, '%y-%m-%d %H:%M')

        # Calculate time difference
        time_difference = done_time - started_time

        return time_difference

    except Exception as e:
        return f"Error: {e}"

# Example input string
input_string = "@started(23-08-07 19:45) @done(23-08-07 21:38)"

# Call the function and print the result
result = subtract_time_difference(input_string)
print(f"Time Difference: {result}")
