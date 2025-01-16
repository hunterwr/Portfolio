import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title and Description
st.title("My Streamlit App")
st.write("Welcome to my app!")

# Input and Output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")


# Create a function to process frames
def add_rectangle_to_frame(frame):
    # Convert the frame from BGR to RGB for Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Get frame dimensions
    height, width, _ = frame.shape
    # Define rectangle dimensions (adjust as needed)
    top_left = (int(width * 0.3), int(height * 0.3))
    bottom_right = (int(width * 0.7), int(height * 0.7))
    # Draw a yellow rectangle
    cv2.rectangle(frame_rgb, top_left, bottom_right, (255, 255, 0), 5)  # Yellow color, thickness 5
    return frame_rgb

# OpenCV video capture
cap = cv2.VideoCapture(0)

# Stream video
if cap.isOpened():
    st.write("Streaming from camera...")
    placeholder = st.empty()  # Placeholder for displaying frames
    while True:
        ret, frame = cap.read()
        if not ret:
            st.write("Failed to grab frame.")
            break
        # Process frame to add rectangle
        processed_frame = add_rectangle_to_frame(frame)
        # Convert processed frame to Image and display in Streamlit
        placeholder.image(processed_frame, channels="RGB")
        # Break loop if the app stops running
        if not st.runtime.exists():
            break
else:
    st.write("Unable to access the camera.")

# Release resources
cap.release()

