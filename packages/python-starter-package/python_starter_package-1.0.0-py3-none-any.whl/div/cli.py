#!/usr/bin/env python3

import argparse

import colorama

from div.lib import divide

# Allow the script to be run standalone (useful during development).
if __name__ == "__main__":
    colorama.init(autoreset=True, strip=False)

    # Initializing Parser
    parser = argparse.ArgumentParser(description="Divider")
    required = parser.add_argument_group("required arguments")
    # Adding Argument
    required.add_argument("-a", help="numerator", type=float, default=None)
    required.add_argument("-b", help="denominator", type=float, default=None)
    args = parser.parse_args()

    a = args.a
    b = args.b

    if a is not None and b is not None:
        print(
            f"{colorama.Fore.CYAN}{a}{colorama.Fore.RESET}/{colorama.Fore.CYAN}{b}"
            f"{colorama.Fore.RESET} = "
            f"{colorama.Fore.GREEN}{divide(a, b)}{colorama.Fore.RESET}"
        )
    else:
        print("Please specify a and b. Use --help or -h")
