#!/usr/bin/env python3

import argparse

def calculate(num1, operation, num2):
    try:
        if operation == 'add':
            return num1 + num2
        elif operation == 'sub':
            return num1 - num2
        elif operation == 'mul':
            return num1 * num2
        elif operation == 'div':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return None
            return num1 / num2
        else:
            print("Error: Invalid operation.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Basic CLI Calculator")
    parser.add_argument('num1', type=float, help='First number')
    parser.add_argument('operation', type=str, choices=['add', 'sub', 'mul', 'div'], help='Operation to perform: add, sub, mul, div')
    parser.add_argument('num2', type=float, help='Second number')

    args = parser.parse_args()

    result = calculate(args.num1, args.operation, args.num2)
    
    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
