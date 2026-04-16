import streamlit as st
import base64
from PIL import Image
import sys
import os
from io import BytesIO
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.app.main import run_model
from backend.app.main import run_model_cinematic
from backend.app.main import run_model_neon

# Set Page Configuration
st.set_page_config(
    page_title="AnimeGen",
    layout="wide",
    page_icon="camera.png"
)

# Hide Streamlit default layout
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}  
        .block-container {
            padding: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Inject custom CSS
st.markdown("""
<style>
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px 10px;
    border-radius: 10px;
}

.header-content {
    display: flex;
    align-items: center;
    gap: 20px;
}

.header-text {
    text-align: left;
}

.header-title {
    font-size: 32px;
    font-weight: 700;
    color: #000000;
    margin: 0;
}

.header-subtitle {
    font-size: 14px;
    color: #666666;
}

.header-icon {
    width: 60px;
}
</style>
""", unsafe_allow_html=True)

# Custom CSS
st.markdown("""
<style>
/* Remove extra padding from image */
div[data-testid="stImage"] {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Header text styling */
.header-title {
    font-size: 40px;
    font-weight: 700;
}

.header-subtitle {
    font-size: 22px;
    color: #555;
    align: center;
    padding: 0;
}
.center-text {
    width: 100%;
    text-align: center;
}

.header-select{
    font-size: 22px;
    margin-top: 20px;
    align: center;
    font-weight: 700;
}
.header-icon {
    width: 200px;
    margin-left:50px;
}

    /* Card Container */
    .style-card {
        border: 2px solid #000000;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
        background-color: white;
        transition: transform 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .style-card:hover {
        transform: translateY(-5px);
        border-color: #d1d1d1;
    }

    /* Titles and Text */
    .card-title {
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 5px;
    }
    .card-subtitle {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }

    /* Buttons */
    .button {
        border-radius: 25px;
        background-color: #1a1a1a;
        color: white;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        margin-top:20px;
    }
    
    .card-icon{
        border-radius: 10px;
    }
            

/* Align column content vertically */
[data-testid="column"] {
    display: flex;
    align-items: center;
    padding: 0 !important;
}
            
div[data-testid="stFileUploader"] {
            border: 2px dashed #6C63FF;
            border-radius: 15px;
            padding: 10px;
            align:center;
            text-align: center;    
        }
        
        .preview-box {
            width: 300px;
            height: 300px;
            border-radius: 15px;
            overflow: hidden;
            border: 1px solid #ddd;
            padding:5px;
        }

    .stButton>button {
        border-radius: 25px;
        background-color: #1a1a1a;
        color: white;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        margin-top:20px;
        display: flex;
        justify-content: center;
        width: 100%;
    }
div.stButton > button {
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 20px 18px;
    border-radius: 12px;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ee0979, #ff6a00);
}

div[data-testid="stSelectbox"] {
            border: 2px solid #000000;
            border-radius: 15px;
            padding: 10px;
            align:center;
            text-align: center;
            display:flex;
            justify-content: center;
            margin-top: 20px; 
        }

div.stDownloadButton > button {
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 20px 18px;
    border-radius: 12px;
    border: none;
    transition: 0.3s;
}

div.stDownloadButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #ee0979, #ff6a00);
}
                     
</style>
""", unsafe_allow_html=True)
   
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "camera.png")

with open(image_path, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode()

st.markdown(f"""
    <div class="main-header" style="display: flex; align-items: center; gap: 20px; height:100px; margin-top:20px;">
    
    <img src="data:image/png;base64,{img_base64}" class="header-icon"/>
    
    <div class="center-text">
        <div class="header-subtitle">
            IMAGE TO ANIME CONVERTOR
        </div>
        <div class="header-title">
            TRANSFORM YOUR PHOTOS INTO STUNNING CARTOONS!
        </div>
        <div class="header-subtitle">
            Upload your image and choose from 3 unique cartoon styles below!
        </div>
        <div class="header-select" style="margin-left:350px">
            <br>CHOOSE YOUR CARTOON STYLE
        </div>
    </div>
    
    </div>
""", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

with st.container():
        col1, col2, col3, col4 = st.columns([2,1,1,1], gap="small")

with col1:
     st.markdown("""
        <div style="font-size:30px; font-weight:700; text-align:center; margin-top:10px;">
            AnimeGen - AI Anime Style Generator
        </div>
        <div style="font-size:16px;color: #555; margin:10px;">
            AnimeGen is an AI-powered web application that transforms real images into stylized anime artwork using different visual styles like Dreamy, Neon, and Cinematic. Users can upload an image, choose a preferred style, and instantly generate high-quality anime-inspired visuals, making it a simple and creative tool for exploring AI-based image transformation.
        </div>
""", unsafe_allow_html=True)
     
     with st.container():
            one, left, right,two = st.columns([0.01,1,1,0.01])

            BASE_DIR = os.path.dirname(os.path.abspath(__file__))

            with left:
                    image_path = os.path.join(BASE_DIR, "original_girl.png")
                    image = Image.open(image_path)
                    image = image.resize((300,300))

                    st.image(image, width=300)

            with right:
                    image_path = os.path.join(BASE_DIR, "original_girl.png")
                    image = Image.open(image_path)
                    image = image.resize((300,300))

                    st.image(image, width=300)  

with col2:
    st.markdown("""
        <div class="style-card">
            <div class="card-title">1. DREAMY ANIME STYLE</div>
            <div class="card-subtitle">(Soft Dreamy Magic)</div>
            <img src="data:image/png;base64,{}" class="card-icon"/>
            <div class="button">CONVERT TO DREAMY 🌿</div>
        </div>
    """.format(
    __import__("base64").b64encode(open("dreamy.jpg", "rb").read()).decode()
), unsafe_allow_html=True)


with col3:
    st.markdown("""
        <div class="style-card">
            <div class="card-title">2. NEON FANTASY STYLE</div>
            <div class="card-subtitle">(Vibrant Surreal Colors)</div>
            <img src="data:image/png;base64,{}" class="card-icon"/>
            <div class="button">CONVERT TO NEON 🌈</div>
        </div>
    """.format(
    __import__("base64").b64encode(open("neon.jpg", "rb").read()).decode()
), unsafe_allow_html=True)  
    
    
    _, center_col, _ = st.columns([0.5,2,0.5])

    with center_col:
    # st.button("UPLOAD YOUR PHOTO")

       # Initialize session state
        if "input_image" not in st.session_state:
            st.session_state.input_image = "Roshani.jpeg"

        if "output_image" not in st.session_state:
            st.session_state.output_image = "roshani_output.jpg"

        if "converted" not in st.session_state:
            st.session_state.converted = False

        if "option" not in st.session_state:
            st.session_state.option = "DREAMY ANIME"


        @st.dialog("ANIME CONVERTOR", width="medium")
        def vote(item):

            uploaded_file = st.file_uploader(
                "Upload Image",
                type=["jpg", "jpeg", "png"],
                label_visibility="collapsed"
            )

            # Update input image if user uploads
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                image.save("temp_input.jpg")
                st.session_state.input_image = "temp_input.jpg"

            # UI Layout
            one, left, right, second = st.columns([0.2, 2, 2, 0.1])

            # LEFT → Input Image
            with left:
                img = Image.open(st.session_state.input_image)
                img = img.resize((300, 300))
                st.image(img, caption="Input Image")

            # RIGHT → Output Image
            with right:
                if st.session_state.get("converted", False):
                    img = Image.open(st.session_state.output_image)
                else:
                    img = Image.open("roshani_output.jpg")  # default image

                img = img.resize((300, 300))
                st.image(img, caption="Output Image")

                if st.session_state.get("converted", False):

                    def get_image_bytes(image_path):
                        img = Image.open(image_path)
                        buf = BytesIO()
                        img.save(buf, format="JPEG")
                        return buf.getvalue()

                    image_bytes = get_image_bytes(st.session_state.output_image)

                    st.download_button(
                        label="DOWNLOAD IMAGE",
                        data=image_bytes,
                        file_name=f"anime_output_{uuid.uuid4().hex[:6]}.jpg",
                        mime="image/jpeg"
                    )

            # BUTTON FUNCTION
            def my_function():
                input_path = st.session_state.input_image

                # Create unique output file
                output_path = f"output_{uuid.uuid4().hex}.jpg"

                selected_style = st.session_state.get("option", "DREAMY ANIME")

                with st.spinner(f"✨ Applying {selected_style} style... Please wait..."):

                    if selected_style == "DREAMY ANIME":
                        run_model(input_path, output_path)

                    elif selected_style == "NEON FANTASY":
                        run_model(input_path, output_path)

                    elif selected_style == "CINEMATIC ANIME":
                        run_model_cinematic(input_path, output_path)

                # Save output
                st.session_state.output_image = output_path
                st.session_state.converted = True

            # Controls
            selectbox, none, button = st.columns([1.5, 0.5, 1])

            with selectbox:
                option = st.selectbox(
                        " ",
                        ("DREAMY ANIME", "NEON FANTASY", "CINEMATIC ANIME"),
                        key="option"
                        )

            with button:
                if st.button("CONVERT IMAGE"):
                    with st.spinner("Converting..."):
                        my_function()

        def reset_state():
                st.session_state.input_image = "Roshani.jpeg"
                st.session_state.output_image = "roshani_output.jpg"
                st.session_state.converted = False
                st.session_state.option = "DREAMY ANIME"
                
                # Open dialog
        if st.button("UPLOAD YOUR PHOTO"):
            reset_state()
            vote("UPLOAD YOUR PHOTO")
        
with col4:
    st.markdown("""
        <div class="style-card">
            <div class="card-title">3. CINEMATIC ANIME STYLE</div>
            <div class="card-subtitle">(Realistic Dramatic Scenes)</div>
            <img src="data:image/png;base64,{}" class="card-icon"/>
            <div class="button">CONVERT TO CINEMATIC 🎬</div>
        </div>
    """.format(
    __import__("base64").b64encode(open("cinematic.jpg", "rb").read()).decode()
), unsafe_allow_html=True)
    


    