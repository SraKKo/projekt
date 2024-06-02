import argparse
import json
import yaml
import xml.etree.ElementTree as ET

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

def save_json(data, file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving JSON: {e}")

# Example usage
data = {"example_key": "example_value"}
save_json(data, 'output.json')

def load_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            return data
    except yaml.YAMLError as e:
        print(f"Error decoding YAML: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
data = load_yaml('data.yml')
print(data)

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False)
    except Exception as e:
        print(f"Error saving YAML: {e}")

# Example usage
data = {"example_key": "example_value"}
save_yaml(data, 'output.yml')

def load_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
root = load_xml('data.xml')
print(ET.tostring(root, encoding='unicode'))

def save_xml(root, file_path):
    try:
        tree = ET.ElementTree(root)
        tree.write(file_path)
    except Exception as e:
        print(f"Error saving XML: {e}")

# Example usage
root = ET.Element("root")
child = ET.SubElement(root, "child")
child.text = "example_value"
save_xml(root, 'output.xml')
