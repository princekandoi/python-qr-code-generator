# Python QR Code Generator

## About
A beginner-friendly Python project that generates a QR code image from a URL entered by the user.

## Features
- Accepts a URL as input
- Lets the user choose the output filename
- Automatically adds the `.png` extension when it is missing
- Saves the generated QR code as a PNG image

## Requirements
- Python 3
- `qrcode` Python package

## Installation
Install the required package:

```bash
python -m pip install -r requirements.txt
```

## How to Run
Run the program from your terminal:

```bash
python qr_generator.py
```

Enter the URL and the filename when prompted. The QR code image will be saved in the current working directory.

## Example
```text
Enter the url : https://github.com
Enter the file name you want to save : github_qr
```

The generated file will be named `github_qr.png`.

## Learning Outcomes
- Using a Python library
- Taking user input
- Saving image files with Python
