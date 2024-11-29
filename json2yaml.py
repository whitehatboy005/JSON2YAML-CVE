import json
import yaml
import os

def convert_json_to_yaml(json_file):
    try:
        # Read the JSON data
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Access CVE number from the nested structure
        cve_number = next(iter(data.get("data", {}).get("documents", {}).keys()), None)
        if not cve_number:
            raise ValueError("CVE number not found in JSON data.")

        # Create YAML file name based on the CVE number
        yaml_file = f"{cve_number}.yaml"

        # Convert JSON to YAML and write it to a file
        with open(yaml_file, 'w') as file:
            yaml.dump(data, file, default_flow_style=False, sort_keys=False)

        print(f"Conversion complete! YAML file saved as {yaml_file}")

    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found. Please check the file path.")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON. Please check if '{json_file}' contains valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Provide file paths dynamically
json_file = input('Please provide the JSON input file path: ').strip()

convert_json_to_yaml(json_file)
