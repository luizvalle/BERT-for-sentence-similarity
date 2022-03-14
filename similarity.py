import sys

def read_pairs():
    first, second = list(), list()
    for line in sys.stdin:
        f, s = line.split("[SEP]")
        first.append(f.strip())
        second.append(s.strip())
    return first, second

def main():
    first, second = read_pairs()

if __name__ == "__main__":
    main()
