# PhishGuard
Machine learning–based phishing URL detection system using Python, Scikit-learn, and Flask. Detects malicious websites with 95% accuracy.
🧠 PhishGuard AI — Intelligent Phishing URL Detection System

PhishGuard AI is a machine learning–based web application that detects phishing URLs with high accuracy using advanced feature engineering and predictive modeling.
It helps identify malicious websites designed to steal sensitive user data such as passwords, credit card details, and personal information.

🚀 Key Features

🧩 ML-Based Classification — Trained on 11,430 URLs with 87 extracted features from the Mendeley Phishing Dataset
.

⚙️ Real-Time URL Analysis — Classifies a given URL as Legitimate or Phishing in seconds.

🌐 Interactive Flask Web App — User-friendly interface to input and test URLs.

🔒 Security-Oriented Design — Helps raise awareness about phishing risks and safe browsing practices.

📊 Explainable Predictions — Analyzes features like URL length, domain structure, special characters, and HTTPS presence.

🛠️ Tech Stack

Python, Flask, Scikit-learn, Pandas, NumPy, Google Colab

HTML, CSS for frontend

Joblib for model deployment

📂 Dataset

Dataset Source:
📊 Hannousse, Abdelhakim; Yahiouche, Salima (2021), “Web page phishing detection”, Mendeley Data, V3, doi: 10.17632/c2gw7fy2j4.3

11,430 URLs (50% legitimate, 50% phishing)

87 engineered features including:

URL-based

HTML/DOM-based

External service-based

🧪 Model Performance

Achieved ~95% accuracy using Random Forest Classifier

Balanced precision and recall for phishing vs legitimate URLs

Optimized feature selection for high interpretability

📸 Demo

(Add screenshots of your Flask app here once you run it)
Example:

Enter a URL → Model analyzes its structure → Displays Phishing / Legitimate with confidence score

🧾 How to Run Locally
git clone https://github.com/<your-username>/PhishGuard-AI.git
cd PhishGuard-AI
pip install -r requirements.txt
python app.py


Then open: http://127.0.0.1:5000/

👩‍💻 Author

Vaishnavi Srivastava
Cybersecurity Intern @ NIELIT | AI & ML Enthusiast
📧 [vaishnavi.srivastava.tech@gmail.com
]
🌐 [[LinkedIn/GitHub profile link](https://www.linkedin.com/in/vaishnavi-srivastava-7b005b250/)]
