#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program is the date approval program


def main():
    # this function can tell the user if they are allowed to date

    print("There is a grandmother who will only approve of you dating her"
          " grandchild if you are at a certain age.")
    print("")

    # input
    age_string = input("Type in your age: ")
    print("")

    # process & output
    try:
        age_number = int(age_string)

        if age_number > 25 and age_number < 40:
            print("You are allowed to date her grandchild!!")
        else:
            print("You are not allowed to date her grandchild."
                  " You must be older than 25 and younger than 40")

    except Exception:
        print("This is not a number!")


if __name__ == "__main__":
    main()
