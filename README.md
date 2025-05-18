# Employee Feedback Analysis

This repository contains the source code and documentation for the Employee Feedback Analysis project. The project is designed to collect and analyze employee feedback through video uploads, utilizing advanced machine learning techniques to process and classify emotions from both facial expressions and speech content.

## Description

The Employee Feedback Analysis system allows users to upload videos containing their reviews about their workplace. The application employs face recognition to identify employees, speech recognition to extract and transcribe spoken content into text, and a BERT-based model to classify the transcribed text into five emotional categories: **angry**, **happy**, **sadness**, **fear**, and **love**. This system aims to provide insights into employee sentiments, facilitating better understanding and improvement of workplace environments.

## Features

- **Video Upload**: Users can upload video files containing their feedback.
- **Face Recognition**: Identifies employees in the video using face recognition technology.
- **Speech-to-Text**: Extracts spoken content from videos and converts it to text using speech recognition.
- **Emotion Classification**: Analyzes transcribed text using a BERT model to classify emotions into angry, happy, sadness, fear, or love.
- **User-Friendly Interface**: A web-based interface for seamless interaction.

## Directory Structure

- **model/**: Contains machine learning models and scripts.
  - `face_recognition_model`: Pre-trained model for face recognition.
  - `speech_recognition_model`: Model or scripts for speech-to-text conversion.
  - `bert_model`: Pre-trained BERT model for emotion classification.
  - `predict.py`: Script to load models and perform predictions.
- **templates/**: Stores HTML files for the front-end interface.
- **app.py**: Main back-end script integrating the front-end, face recognition, speech recognition, and BERT-based emotion classification.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/employee-feedback-analysis.git
   cd employee-feedback-analysis
   ```

2. **Set Up a Virtual Environment** (Recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   Ensure dependencies include `tensorflow`, `keras`, `flask`, `face_recognition`, and `speechrecognition`.

4. **Set Up Models**:
   - Place pre-trained models (face recognition, speech recognition, and BERT) in the `model/` directory.
   - Configure paths to models in `predict.py` if necessary.

5. **Run the Application**:
   Start the Flask server:
   ```bash
   python app.py
   ```
   Access the application at `http://localhost:5000` in your web browser.

## Usage

1. Open the web application in a browser.
2. Upload a video file containing your workplace feedback.
3. The system will:
   - Perform face recognition to identify the employee.
   - Extract and transcribe speech from the video.
   - Classify the transcribed text into one of five emotions (angry, happy, sadness, fear, love).
4. View the results, including the identified employee and the classified emotion, on the web interface.

## Technologies Used

- **Back-End**: Python, Flask
- **Front-End**: HTML, CSS, JavaScript
- **Machine Learning**:
  - TensorFlow/Keras for model development and predictions
  - Face Recognition library for identifying employees
  - SpeechRecognition library for converting speech to text
  - BERT model for emotion classification
- **Design**: Figma for UI/UX mock-up

#

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or feedback, please contact:
- Widia Fandi: [widiafandi58@gmail.com](mailto:widiafandi58@gmail.com)
- Satria Nur Saputro: [satrianursaputro06@gmail.com](mailto:satrianursaputro06@gmail.com)