# JSON2YAML
**JSON2YAML** is a Python-based utility that simplifies the process of converting CVE (Common Vulnerabilities and Exposures) data from JSON format into well-structured YAML files. This tool allows security analysts and developers to easily manage, analyze, and integrate CVE data into their vulnerability management systems.

With **JSON2YAML**, you can seamlessly convert detailed CVE records into a readable YAML format, making it easier to work with tools that require YAML files or to maintain your own vulnerability databases.

## Features:
- **Automatic CVE Parsing:** Automatically extracts the CVE number from the provided JSON data and uses it as the filename for the YAML output.
- **Structured Output:** Converts raw CVE JSON data into a neatly formatted YAML file, retaining important information such as descriptions, CVSS scores, references, and affected software.
- **Error Handling:** Provides error messages when the required CVE data is missing or improperly formatted.
- **Easy-to-Use:** A simple, command-line based tool that converts individual CVEs or batches of CVE data quickly and efficiently.
#
## Example Input:
**Provide a JSON file with CVE details such as ID, description, CVSS score, references, and affected products.**
![Screenshot 2024-12-04 082124](https://github.com/user-attachments/assets/18e24f94-0912-4d3f-b9bc-1e9706c39b98)

## JSON2YAML conversion
![Screenshot 2024-12-04 082034](https://github.com/user-attachments/assets/ac9575aa-8cbd-4422-abaa-96b84b0a1e27)

## Example Output:
**A neatly formatted YAML file with structured CVE information.**
![Screenshot 2024-12-04 082205](https://github.com/user-attachments/assets/edd6b840-7cd7-4c0c-9fa2-499bf5e0efb5)

#
## Installation
## Clone the Repository
```bash
git clone https://github.com/whitehatboy005/JSON2YAML-CVE
cd JSON2YAML-CVE
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Usage:
**To convert a CVE JSON file to YAML, run the script:**
```bash
python json2yaml.py
```
- **Input the path to your JSON file when prompted.**
- **The script will automatically generate a YAML file named after the CVE ID.**

## Contribution:
**Contributions are welcome! If you have any suggestions for improvements or bug fixes, feel free to submit a pull request.**

## License:
This project is licensed under the terms of the [MIT license](LICENSE.md).
