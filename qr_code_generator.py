# Import the library
import qrcode
import os

# create the qr code function
def generate_qr_code():
    
# create an instance of the qr code class and assign the properties
    qr = qrcode.QRCode (
        
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
        
    )
    
# Ask user for text or url to convert and filename to save
    text = input('Enter the text or Url: ')
    filename = input(f'Enter the name you want to: ') + '.png'
    
# Design the properties of the qr code
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color= 'black', back_color = 'white')
    img.save(filename)
    
    # filename = os.path.basename('qrimg1s.png')
    
    print(f'Your qr code was saved successfully as {filename}')
    
generate_qr_code()