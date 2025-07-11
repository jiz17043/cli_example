import argparse


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Example")
    parser.add_argument("name", type=str, help="Your name")
    args = parser.parse_args()
    print(f"Hello, {args.name}! Welcome to the CLI example.")


if __name__ == "__main__":
    main()
