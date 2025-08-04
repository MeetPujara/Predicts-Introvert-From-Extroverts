# 🧠 Personality Prediction App

This project is a Streamlit web application that predicts whether a user is an introvert or extrovert based on their input of behavioral traits. It leverages a pre-trained machine learning model (K-Nearest Neighbors) to classify users based on their responses to a set of questions about their social behavior and preferences. The model and data scaler are trained and saved using a Jupyter Notebook.

🚀 **Key Features**

*   **Interactive User Interface:** Utilizes Streamlit to create an intuitive and user-friendly web interface for inputting behavioral traits.
*   **Pre-trained Machine Learning Model:** Employs a K-Nearest Neighbors (KNN) model trained on a dataset of personality traits.
*   **Data Scaling:** Uses a StandardScaler to preprocess input data, ensuring optimal model performance.
*   **Real-time Prediction:** Provides instant personality predictions based on user input.
*   **Model Persistence:** The trained model and scaler are saved as `.pkl` files for easy loading and reuse.
*   **Categorical Encoding:** Handles categorical features by encoding them into numerical values.

🛠️ **Tech Stack**

*   **Frontend:**
    *   Streamlit: Web application framework
*   **Backend:**
    *   Python: Programming language
    *   NumPy: Numerical computing library
    *   scikit-learn (sklearn): Machine learning library
    *   joblib: Python library to serialize and deserialize Python objects.
*   **Model Training:**
    *   Jupyter Notebook: Interactive development environment
    *   Pandas: Data analysis library
*   **Model:**
    *   K-Nearest Neighbors (KNN)
*   **Other:**
    *   Pickle (.pkl): Serialization format for saving the model and scaler

📦 **Getting Started / Setup Instructions**

**Prerequisites**

*   Python 3.6 or higher
*   pip package installer

**Installation**

1.  Clone the repository:

    ```bash
    git clone https://github.com/MeetPujara/Predicts-Introvert-From-Extroverts
    cd Predicts-Introvert-From-Extroverts
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

1.  Navigate to the directory containing `app.py`.
2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

3.  Open your web browser and go to the address displayed in the terminal (usually `http://localhost:8501`).

📂 **Project Structure**

```
.
├── app.py              # Streamlit web application
├── prediction.ipynb    # Jupyter Notebook for model training
├── knn_model.pkl       # Serialized KNN model
├── scaler.pkl          # Serialized StandardScaler
├── train.csv           # Training data (not explicitly used in app.py but assumed to exist)
├── test.csv            # Testing data (not explicitly used in app.py but assumed to exist)
└── README.md           # This file
```

🤝 **Contributing**

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.


📬 **Contact**
meetpujara02@gmail.com

💖 **Thanks**

Thank you for checking out this project! We hope it's helpful and informative.

This is written by [readme.ai](https://readme-generator-phi.vercel.app/).
