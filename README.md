# Human Pose Estimation with OpenCV and Streamlit
This project demonstrates human pose estimation using OpenCV's Deep Neural Network (DNN) module and a pre-trained TensorFlow model. A simple yet interactive web application built with Streamlit allows users to upload images and view real-time pose estimation results.

## Features

Interactive UI: Upload images and visualize pose estimation results with an intuitive interface.

Pre-trained Model: Utilizes a TensorFlow-based model for detecting and visualizing 18 key body landmarks.

Adjustable Threshold: Fine-tune the detection confidence threshold for better results.

Real-Time Processing: Efficiently processes uploaded images to produce pose estimation outputs.
## Installation and Setup

### Prerequisites

Python 3.8 or above
Streamlit
OpenCV
### Steps to Run

Clone this repository:


git clone https://github.com/AdityaSalian/edunet-techsaksham-phase2.git


Install the required dependencies:


Download the pre-trained model file graph_opt.pb and place it in the project directory.
(Ensure the file path matches the one in the code.)

Run the Streamlit app:


streamlit run estimation_app.py
Open the provided URL in your browser to interact with the app.

## Usage

Upload Image: Click on the "Upload an image" button to upload a JPG, JPEG, or PNG image.

Adjust Threshold: Use the slider to set the confidence threshold for key point detection.

View Results: The app displays the original image and the processed image with the estimated pose.
## File Structure


pose-estimation/

├── estimation_app.py     # Main application script

├── graph_opt.pb          # Pre-trained TensorFlow model

├── Images/

│      └── Image_1.jpeg      # Default demo image

└── README.md             # Documentation


## Credits
Developed with ❤️ using OpenCV, Streamlit, and TensorFlow.
Special thanks to the open-source community for providing the tools and resources that made this project possible.

Feel free to contribute or suggest improvements! 😊

## License
This project is licensed under the MIT License. See the LICENSE file for details.
