from gendiff.cli import description_of_thegender_spread
from gendiff.generate_diff import generate_diff


def main():
    args = description_of_thegender_spread()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()