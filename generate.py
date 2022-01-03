#!/usr/bin/env python3

import argparse
import random

def setup_arguments(argument_parser):
    argument_parser.add_argument(
        '--version',
        type=int,
        required=True,
        help=(
            """
            version, 1=with argument, 2=no argument
            """)
    )
    argument_parser.add_argument(
        '--length',
        type=int,
        required=True,
        help=(
            """
            maximum length
            """)
    )
    argument_parser.add_argument(
        '--workload',
        type=int,
        required=True,
        help=(
            """
            maximum workload
            """)
    )

    argument_parser.add_argument(
        '-n',
        type=int,
        required=True,
        help=(
            """
            maximum number of calls to map
            """)
    )
    argument_parser.add_argument(
        '--seed',
        type=int,
        required=True,
        help=(
            """
            random seed
            """)
    )


def preamble():
    filename = "base1.ml" if args.version == 1 else "base2.ml"
    with open(filename, 'r') as file:
        data = file.read()

    return data

def emit_code():
    n = random.randint(1,args.n)
    s = preamble()
    print(s)
    s = "let _ = Random.init({seed});\n".format(seed=args.seed)
    print(s)
    calls = ""
    for i in range(n):
        length = random.randint(10,args.length)
        calls += "  let _ = map {arg} fibonacci (List.init {length} (fun _ -> rand_range 10 {max})) in\n".format(
            arg="1" if args.version == 1 else "", length=length, max=args.workload)
    print(calls)
    print("  ()")


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    setup_arguments(argument_parser)
    args = argument_parser.parse_args()
    random.seed(args.seed)

    emit_code()
