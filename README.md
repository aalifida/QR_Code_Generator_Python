
```markdown
# QR Code Generator

This is a Python script that generates QR codes based on user input. You can choose to create a simple QR code or a customizable QR code with specified version, box size, border size, and colors.

## Requirements

- Python 3.x
- qrcode library

You can install the required library using pip:

```bash
pip install qrcode[pil]
```

## Usage

1. Run the script.
2. Follow the prompts to input your website URL and select the type of QR code you want to generate.

### Script Prompts

1. **Enter Website URL**: Paste the URL for which you want to generate a QR code.
2. **Choose QR Code Type**:
    - Press `1` for a simple QR code.
    - Press `2` for a customizable QR code.

### Customizable QR Code Prompts

If you choose a customizable QR code, you will be prompted to enter additional details:
- **Version**: Enter the version of the QR code (1-40).
- **Box Size**: Enter the box size of the QR code.
- **Border Size**: Enter the border size of the QR code.
- **Background Color**: Enter the background color of the QR code (e.g., white, black).
- **Color**: Enter the color of the QR code (e.g., black, blue).

## Example

```python
import qrcode as qr

website = input("Please Paste Your Website's URL: ")
QR_type = int(input("For Simple QR Code Press 1:\nFor Customizable QR Code Press 2:\n"))

if QR_type == 1:
    code = qr.make(website)
    print(type(code))
    code.save("QR_sample1.png")
else:
    qr_version = int(input("Enter Version of QR Code (1-40): "))
    qr_boxsize = int(input("Enter Box Size of QR Code: "))
    qr_border = int(input("Enter Border Size of QR Code: "))
    qr_bgColor = input("Enter Background Color of QR Code: ").lower()
    qr_Color = input("Enter Color of QR Code: ").lower()
    
    code = qr.QRCode(
        version=qr_version,
        error_correction=qr.constants.ERROR_CORRECT_H,
        box_size=qr_boxsize,
        border=qr_border,
    )
    code.add_data(website)
    code.make(fit=True)
    
    image = code.make_image(fill_color=qr_Color, back_color=qr_bgColor)
    image.save("QR_sample2.png")
```

## Output

- For a simple QR code, the output file will be named `QR_sample1.png`.
- For a customizable QR code, the output file will be named `QR_sample2.png`.

## Notes

- Ensure the input colors are valid color names or hex codes.
- The version number should be between 1 and 40.
- Customize the script further if needed to fit your requirements.

---

Enjoy generating your QR codes!
```

This `README.md` provides an overview of the script, requirements, usage instructions, an example of the script, and notes on customization. Feel free to adjust any sections as needed.