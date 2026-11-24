
# QR Code Generator

A simple Python application that generates QR codes from text or URLs and allows users to add a custom logo at the centre of the QR code.
![Image Description](image.png)
## Features

- Generate QR codes from text or URLs.
- Select a custom logo from your computer.
- Add the selected logo to the centre of the QR code.
- Customize QR code foreground and background colors.
- Save the generated QR code as an image.

## Technologies Used

- Python
- qrcode
- Pillow (PIL)
- Tkinter

## Requirements

- Python 3 installed on your computer.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/revocajana/qrcode.git
   ```

2. Navigate to the project directory:

   ```bash
   cd qrcode
   ```

3. Install the required packages in your virtual environment:

   ```bash
   pip install "qrcode[pil]" Pillow
   ```

## Usage

Run the Python script:

```bash
python qrcodegenerate.py
```

1. Enter the text or URL you want to encode.
2. Select a logo image from your computer.
3. The application generates a QR code with your logo.
4. The generated QR code is saved as an image.

## Project Structure

```text
qrcode/
│
├── qrcodegenerate.py
├── qrcode.png
├── gitlogo.png
└── .gitignore

```

## Example

The application can generate QR codes for:

- Website URLs
- Contact information
- Plain text
- Other text-based information

## License

This project is open-source and available for learning and personal use.
