import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_path, qr_size=1200, logo_size=300):
    qr = qrcode.QRCode(
        version=15,  # Increased version for higher quality
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,  # Increased box size for higher resolution
        border=1
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')
    
    # Open the logo image
    logo = Image.open(logo_path).convert("RGBA")
    
    # Resize logo
    logo = logo.resize((logo_size, logo_size))
    
    # Increase logo visibility by adding a white background
    logo_with_bg = Image.new("RGBA", (logo_size + 20, logo_size + 20), (255, 255, 255, 255))
    logo_with_bg.paste(logo, (10, 10), mask=logo)
    
    # Convert to RGB before pasting onto QR code
    logo_with_bg = logo_with_bg.convert("RGB")
    
    # Calculate position
    qr_width, qr_height = qr_img.size
    pos = ((qr_width - logo_with_bg.size[0]) // 2, (qr_height - logo_with_bg.size[1]) // 2)
    
    # Paste the logo onto the QR code
    qr_img.paste(logo_with_bg, pos)
    
    # Save the QR code with higher resolution
    qr_img = qr_img.resize((qr_size, qr_size), Image.ANTIALIAS)
    qr_img.save(output_path, quality=100)
    print(f"QR code saved at {output_path}")

# Example usage
generate_qr_with_logo("https://qr-code.click/i/p/67e06c0d83497", "logo.png", "qr_with_logo.png")
