import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Konwerter")
    parser.add_argument('--example', type=str, help='An example argument')
    args = parser.parse_args()
    print(args.example)

if __name__ == "__main__":
    main()

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
data = load_json('data.json')
print(data)
