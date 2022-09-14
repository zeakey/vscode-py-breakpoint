import os, argparse

def parse_args():
    parser = argparse.ArgumentParser(description='vscode python breakpoint')
    parser.add_argument('--arg', type=str, default=None)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.arg)

    for i in range(10):
        print(i)
