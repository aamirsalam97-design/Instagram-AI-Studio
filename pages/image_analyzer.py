import streamlit as st
from PIL import Image
from ultralytics import YOLO
import tempfile

from utils.gemini_api import (
    generate_image_description,
    predict_engagement
)

# Load YOLO Model
model = YOLO("yolov8n.pt")


def image_analyzer():

    st.title("🖼️ AI Image Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("🔍 Analyze Image"):

            with st.spinner("Analyzing Image..."):

                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:

                    image.save(tmp.name)

                    results = model(tmp.name)

                    result = results[0]

                    plotted = result.plot()

                    st.image(
                        plotted,
                        caption="Detected Objects",
                        use_container_width=True
                    )

                    st.subheader("📋 Objects Found")

                    names = result.names
                    detected_objects = []

                    for box in result.boxes:

                        cls = int(box.cls[0])
                        conf = float(box.conf[0])

                        detected_objects.append(names[cls])

                        st.write(f"✅ {names[cls]} ({conf:.2f})")

                    if detected_objects:

                        # AI Description
                        description = generate_image_description(
                            ", ".join(detected_objects)
                        )

                        st.subheader("🤖 AI Description")
                        st.write(description)

                        # Engagement Prediction
                        engagement = predict_engagement(description)

                        st.subheader("📈 AI Engagement Prediction")
                        st.markdown(engagement)

                    else:

                        st.warning("No objects detected.")