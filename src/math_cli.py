import argparse

# Example 3: CLI with Multiple Arguments and Choices
def math_cli():
    parser = argparse.ArgumentParser(description="Math operation CLI")
    parser.add_argument("x", type=int, help="First number")
    parser.add_argument("y", type=int, help="Second number")
    parser.add_argument("--operation", choices=["add", "subtract", "multiply"], default="add", help="Operation to perform")
    args = parser.parse_args()

    if args.operation == "add":
        result = args.x + args.y
    elif args.operation == "subtract":
        result = args.x - args.y
    else:
        result = args.x * args.y

    print(f"Result: {result}")

if __name__ == "__main__":
    math_cli()
