import qrcode
import qrcode.constants

def gen_qr_code(text,filename):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
text="https://python.org"
file_name="espn.png"
gen_qr_code(text,file_name)
print(f"qr code saved as {file_name}")