import argparse

# Example 2: CLI with Optional Argument
def greet_cli():
    parser = argparse.ArgumentParser(description="Greet with an optional message")
    parser.add_argument("name", type=str, help="Your name")
    parser.add_argument("--greeting", type=str, default="Hello", help="Greeting message")
    args = parser.parse_args()
    print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    greet_cli()
