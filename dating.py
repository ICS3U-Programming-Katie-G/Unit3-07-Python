#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 19th, 2022
# This program asks the user if they are
# good looking and if they are rich.
# If they are either good looking or rich,
# then the program will tell the user that
# they are eligible to date my grandchild.
# The program will also tell the user if
# their response is invalid, which is anything
# other than "1" (for yes) or "0" (for no).


# this function checks to see if the user
# is either rich or good looking, and displays
# the results back to the user. This function also
# checks to make sure the user input is valid.
def main():
    # introducing the user to the program
    # and describing what the program will do.
    print(
        "I am the grandparent of this lovely being. Oh? "
        "What’s that? You want to date my grandchild?? Well, "
        "I have two (2) questions for you. Answer carefully; "
        "these questions shall determine thine fate. "
        "Answer these two questions using 1 for 'yes' and 0 for 'no'. "
    )

    # gets the input from the user on if they are
    # good looking and if they are rich.
    userRich = input("First: are you rich? (1 for yes or 0 for no) ")
    userGoodLooking = input(
        "Second: are you extraordinarily good looking? (1 or yes or 0 for no) "
    )

    # try-catch statement to see if the user's
    # input on if they are good looking and rich
    # is a valid response.
    try:
        userRichInt = int(userRich)
        userGoodLookingInt = int(userGoodLooking)
        if userRichInt and userGoodLookingInt == 1 or 0:
            if userRichInt or userGoodLookingInt == 1:
                print(
                    "Congratulations! The council (which "
                    "consists only of myself and many, many "
                    "mirrors) has determined that you are "
                    "eligible to date my grandchild! You "
                    "better not make me regret this decision. :-)"
                )
            else:
                print(
                    "Sorry! The council (which consists only "
                    "of myself and many, many mirrors) has determined "
                    "that you are NOT eligible to date my grandchild! "
                    "Please leave now :-)"
                )
        else:
            print(
                "This response was not valid. Respond only with '1' for 'yes' or '0' for 'no', please."
            )
    except Exception:
        print(
            "This response was not valid. Respond only with '1' for 'yes' or '0' for 'no', please."
        )
    finally:
        print("Thank you for using this program :-)")


if __name__ == "__main__":
    main()
