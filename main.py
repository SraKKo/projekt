import argparse

def main():
    parser = argparse.ArgumentParser(description="Konwerter")
    parser.add_argument('--example', type=str, help='An example argument')
    args = parser.parse_args()
    print(args.example)

if __name__ == "__main__":
    main()

