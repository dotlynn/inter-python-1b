"""
From Intro to Python assignment 4
counter.py

To execute, run: python counter.py
"""

def main():
    """
    Enter your code below.
    """
    message = ['The numbers are: ']

    while True:

        start_value = input('Please enter a start value: ')
        end_value = input('Please enter an end value: ')
        step_value = input('Please enter a step value: ')

        # Validate if END value is empty, if empty keep prompting user
        if not end_value:
            print('-- Oops! You must provide and end value')
            continue
        else:
            #Validate if user hit enter(empty) for both start & step, end is a number
            if not start_value and not step_value and end_value.isnumeric():
                start_value = 0
                step_value = 1
                end_value = int(end_value) + step_value
                break
            #validate if user hit enter(empty) for start, end/step values are numbers
            elif not start_value and end_value.isnumeric() and step_value.isnumeric():
                start_value = 0
                step_value = int(step_value)
                end_value = int(end_value) + step_value
                break
            #validate start/end values are numbers, user hit enter(empty)
            elif start_value.isnumeric() and end_value.isnumeric() and not step_value:
                step_value = 1
                start_value = int(start_value)
                end_value = int(end_value) + step_value
                break
            #validates all values are numbers
            elif start_value.isnumeric() and end_value.isnumeric() and step_value.isnumeric():
                start_value = int(start_value)
                step_value = int(step_value)
                end_value = int(end_value) + step_value
                break
            else:
                print('-- Oops! Bad value. Please enter a number')
                continue
    for numbers in range(start_value, end_value, step_value):
        (message).append(numbers)
    print(*message)


if __name__ == '__main__':
    main()
