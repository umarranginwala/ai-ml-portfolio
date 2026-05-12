# oral-cancer-ai

> AI-powered oral cancer detection from medical images using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13-orange.svg)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/Flask-2.3-black.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Production-ready web application for oral cancer detection using CNN and Transfer Learning.

## 🚀 Live Demo

Try it now: [Launch Demo](https://github.com/umarranginwala/ai-ml-portfolio/tree/main/demo/oral-cancer-detection-demo)

![Demo Screenshot](https://via.placeholder.com/800x400?text=Oral+Cancer+AI+Demo)

## Features

- 🖼️ **Image Upload** - Drag & drop interface
- 🧠 **AI Analysis** - Real-time CNN prediction
- 📊 **Confidence Score** - Probability visualization
- 🏥 **Medical Report** - Risk assessment & recommendations
- 🌐 **Web Interface** - Flask-based responsive design
- 🔌 **REST API** - Programmatic access

## Quick Start

```bash
# Clone and setup
git clone https://github.com/umarranginwala/oral-cancer-ai.git
cd oral-cancer-ai
pip install -r requirements.txt

# Run web app
python app.py
# Open http://localhost:5000
```

## Model Architecture

```
Input (224×224 RGB)
    ↓
ResNet50 (Transfer Learning)
    ↓
GlobalAveragePooling2D
    ↓
Dense(1024) → Dropout(0.5)
    ↓
Dense(512) → Dropout(0.3)
    ↓
Dense(1, sigmoid)
    ↓
Cancer Probability
```

## API Usage

```bash
curl -X POST -F "image=@oral_image.jpg" http://localhost:5000/api/predict
```

**Response:**
```json
{
  "predicted_class": "Normal (Non-Cancerous)",
  "confidence": 92.45,
  "risk_level": "Very Low Risk"
}
```

## Dataset

- **Type:** Oral cavity images
- **Classes:** Cancerous / Non-Cancerous
- **Preprocessing:** 224×224 resize, normalization
- **Augmentation:** Rotation, zoom, flip

## Performance

- **Accuracy:** ~94%
- **F1 Score:** 0.92
- **Inference Time:** < 2 seconds

## Tech Stack

- Python 3.9
- TensorFlow / Keras
- Flask
- OpenCV
- Pillow
- HTML5 / CSS3 / JavaScript

## Medical Disclaimer

⚠️ **For research and educational purposes only.** Not for clinical diagnosis.

## Research Paper

📄 [Oral Cancer Detection Report](https://github.com/umarranginwala/ai-ml-portfolio/blob/main/Final-Papers/Umar_Oral_Cancer_Report.pdf)

## License

MIT License

---

Built for healthcare innovation | M.Sc AI/ML, Gujarat University
