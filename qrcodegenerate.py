import qrcode #pip install qrcode
from PIL import Image, ImageDraw #pip install pillow - Python Image Library
from tkinter import Tk, filedialog #included in python's standard library - available on installation

# Hide the main Tkinter window
root = Tk()
root.withdraw()

# Get QR data
data = input("Enter anything to generate QR: ") #try https://github.com/revocajana

# Select a logo from your computer, i have saved gitlogo.png in this folder for trial
logo_path = filedialog.askopenfilename(
    title="Select your logo",
    filetypes=[
        ("Image files", "*.png *.jpg *.jpeg"),
        ("All files", "*.*")
    ]
)

if not logo_path:
    print("No logo selected!")
    exit()

# Generate QR code
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

qr_image = qr.make_image(
    fill_color=(241, 78, 50), #the gitlogo color code
    back_color="white"
).convert("RGB")

# Load selected logo
logo = Image.open(logo_path).convert("RGBA")

# Resize logo
logo.thumbnail(
    (qr_image.width // 5, qr_image.height // 5),
    Image.Resampling.LANCZOS
)

# Calculate centre position
position = (
    (qr_image.width - logo.width) // 2,
    (qr_image.height - logo.height) // 2
)

# Create white background behind logo
padding = 2
draw = ImageDraw.Draw(qr_image)

draw.rounded_rectangle(
    [
        position[0] - padding,
        position[1] - padding,
        position[0] + logo.width + padding,
        position[1] + logo.height + padding
    ],
    radius=2,
    fill="white"
)

# Paste logo
qr_image.paste(logo, position, logo)

# Save generated QR code
qr_image.save("qrcode.png")

# Display result
qr_image.show()

print("QR code generated successfully!")
