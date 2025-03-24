import qrcode
from PIL import Image


class QRCode:
    """constructor to initialize the QRCode object """
    def __init__(
        self,
        data, 
        logo_path, 
        output_path, 
        qr_size=1200, 
        logo_size=300
        ):
        self.data = data
        self.logo_path = logo_path
        self.output_path = output_path
        self.qr_size = qr_size
        self.logo_size = logo_size
        
    """qr code generater with logo """
    def generate_qr_with_logo(self):
        qr = qrcode.QRCode(
            version=15,  # Increased version for higher quality
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=15,  # Increased box size for higher resolution
            border=1
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

        # Open the logo image
        logo = Image.open(self.logo_path).convert("RGBA")

        # Resize logo
        logo = logo.resize((self.logo_size, self.logo_size))

        # Increase logo visibility by adding a white background
        logo_with_bg = Image.new(
            "RGBA", (self.logo_size + 10, self.logo_size + 10), (255, 255, 255, 255))
        logo_with_bg.paste(logo, (10, 10), mask=logo)

        # Convert to RGB before pasting onto QR code
        logo_with_bg = logo_with_bg.convert("RGB")

        # Calculate position
        qr_width, qr_height = qr_img.size
        pos = ((qr_width - logo_with_bg.size[0]) //
               2, (qr_height - logo_with_bg.size[1]) // 2)

        # Paste the logo onto the QR code
        qr_img.paste(logo_with_bg, pos)

        # Save the QR code with higher resolution
        qr_img = qr_img.resize((self.qr_size, self.qr_size), Image.ANTIALIAS)
        qr_img.save(self.output_path, quality=100)
        print(f"QR code saved at {self.output_path}")


if __name__ == "__main__":
    qr = QRCode("https://qr-code.click/i/p/67e06c0d83497",
                "logo.png", "qr_with_logo.png")
    qr.generate_qr_with_logo()
