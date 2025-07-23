import streamlit as st
import requests
import os
import time

# ✅ Set page metadata
st.set_page_config(page_title="Lane + Object Detection", layout="centered")

# ✅ Inject Bootstrap
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

# ✅ Page title
st.title("🚗 Lane Detection + Object Detection")

# ✅ Styled container for app
st.markdown('<div class="container p-4 border rounded shadow bg-light">', unsafe_allow_html=True)

# ✅ File uploader (supports both image and video)
uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "png", "jpeg", "mp4"])

if uploaded_file:
    file_type = uploaded_file.type

    # ------------------------------
    # ✅ IMAGE PROCESSING
    # ------------------------------
    if "image" in file_type:
        with open("static/input.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image("static/input.jpg", caption="Uploaded Image", use_column_width=True)

        if st.button("Process Image"):
            with st.spinner("Processing image..."):
                try:
                    res = requests.post(
                        "http://127.0.0.1:8000/process/",
                        files={"file": open("static/input.jpg", "rb")}
                    )
                    if res.status_code == 200:
                        st.success("✅ Processing complete!")
                        st.image("static/output.jpg", caption="Processed Output", use_column_width=True)

                        if os.path.exists("logs/log.txt"):
                            with open("logs/log.txt", "r") as log_file:
                                st.text_area("📄 Logs", log_file.read(), height=150)
                    else:
                        st.error("❌ Failed to process image.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

    # ------------------------------
    # ✅ VIDEO PROCESSING
    # ------------------------------
    elif "video" in file_type:
        with open("static/input.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.video("static/input.mp4")

        if st.button("Process Video"):
            with st.spinner("Processing video..."):
                try:
                    res = requests.post(
                        "http://127.0.0.1:8000/process-video/",
                        files={"file": open("static/input.mp4", "rb")}
                    )
                    if res.status_code == 200:
                        time.sleep(1)  # Ensure file write is done
                        st.success("✅ Processing complete!")
                        st.video("static/output.mp4")

                        if os.path.exists("logs/log.txt"):
                            with open("logs/log.txt", "r") as log_file:
                                st.text_area("📄 Logs", log_file.read(), height=150)
                    else:
                        st.error("❌ Failed to process video.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)
