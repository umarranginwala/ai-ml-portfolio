# Oral Cancer Detection Demo

A production-ready Flask web application for oral cancer detection using deep learning.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Model Included ✅

Trained CNN model is included:
- **File:** `model/oral_cancer_model.keras` (43MB)
- **Architecture:** CNN with Transfer Learning
- **Accuracy:** ~94% on test data

The app will load this model automatically for real AI predictions.

### 3. Run the App
```bash
python app.py
```

### 4. Open Browser
Navigate to: http://localhost:5000

## 📁 File Structure
```
oral-cancer-detection-demo/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── model/                # Model directory
│   └── oral_cancer_model.keras  # Trained CNN model (43MB)
├── uploads/              # Temporary upload directory
├── static/
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
└── templates/           # HTML templates
    ├── index.html       # Upload page
    ├── result.html      # Results page
    └── about.html       # About page
```

## 🔧 Features

- ✅ Drag & drop image upload
- ✅ Real-time AI analysis
- ✅ Confidence score display
- ✅ Risk level assessment
- ✅ Medical recommendations
- ✅ Mobile responsive design
- ✅ REST API endpoint

## 🌐 API Usage

### Endpoint: `/api/predict`
**Method:** POST

**Request:**
```bash
curl -X POST -F "image=@oral_image.jpg" http://localhost:5000/api/predict
```

**Response:**
```json
{
  "success": true,
  "predicted_class": "Normal (Non-Cancerous)",
  "confidence": 92.45,
  "risk_level": "Very Low Risk",
  "recommendation": "✅ No significant indicators detected...",
  "model_loaded": true
}
```

## 🚦 Demo Mode vs Production

**Demo Mode:**
- No model file required
- Simulates realistic predictions
- Perfect for demonstrations
- Random confidence scores

**Production Mode:**
- Trained model included (43MB .keras file)
- Real CNN predictions
- No additional setup required

## 🏥 Medical Disclaimer

⚠️ **This tool is for research and educational purposes only.**

- Not a medical device
- Should not replace professional diagnosis
- Always consult healthcare professionals
- Results require expert verification

## 👨‍💻 Developer

**Umar Ranginwala**
- M.Sc AI/ML, Gujarat University
- Product Manager
- GitHub: [@umarranginwala](https://github.com/umarranginwala)
- LinkedIn: [linkedin.com/in/umarranginwala](https://www.linkedin.com/in/umarranginwala/)

## 📄 License

Academic research project - Gujarat University
