import streamlit as st
import qrcode
from io import BytesIO
# from PIL import Image
st.title(":blue[QRCODE GENERATOR] ")
input=st.text_input("Enter Text/Url here")
if st.button("Generate QR Code"):
    if input=="":
            st.warning("Please enter text or URL to generate the QR code.")

    else:
        def gen_qr_code(input):
            qr=qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4
            )
            qr.add_data(input)
            qr.make(fit=True)
            img=qr.make_image(fill_color="black", back_color="white")
            return img
            
        
    
        with st.spinner("Processing"):
        

                qr_image=gen_qr_code(input)

                text=f"https://{input}"
                # st.image("code.png",width=300)
                
                    
                # Save the image to a BytesIO object for download
                buffered = BytesIO()
                qr_image.save(buffered, format="PNG")
                buffered.seek(0)
                # Display the QR code in Streamlit
                st.image(buffered, width=300)
                
                # Display the download button
                st.download_button(
                    label="Download QR Code",
                    data=buffered,
                    file_name="code.png",
                    mime="image/png"
                )
        
                st.balloons()
                st.success("QR Code generated")




