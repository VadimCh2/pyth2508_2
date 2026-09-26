import pyotp
import qrcode
import io
import base64

secret = 'JBSWY3DPEHPK3PXP'

totp = pyotp.TOTP(secret)


uri = totp.provisioning_uri(
    name='vach.com',
    issuer_name='Hw_6',
)


qr = qrcode.make(uri)
qr.show()
qr.save("hh.png")
buffer = io.BytesIO()
qr.save(buffer, format='PNG')

base_64_qr = base64.b64encode(buffer.getvalue()).decode()
print(base_64_qr)

otp_user = input('enter otp: ')
is_valid = totp.verify(otp_user)
print(is_valid)
