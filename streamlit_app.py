import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# Streamlit 페이지 제목 설정
st.title("QR 코드 생성기")

# 사용자 입력 받기
input_data = st.text_input("QR 코드에 넣을 텍스트 또는 URL을 입력하세요:")

# QR 코드 생성 함수
def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

# 버튼을 눌렀을 때 QR 코드 생성
if st.button("QR 코드 생성"):
    if input_data:
        qr_image = generate_qr_code(input_data)
        
        # QR 코드를 Streamlit에 표시하기 위해 바이트로 변환
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        st.image(buffer, caption="생성된 QR 코드")
        
        # QR 코드를 다운로드할 수 있는 버튼 생성
        buffer.seek(0)
        btn = st.download_button(
            label="QR 코드 다운로드",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.warning("텍스트 또는 URL을 입력하세요.")
