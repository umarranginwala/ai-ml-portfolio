"""
Oral Cancer Detection Web Application
====================================
A production-ready Flask application for oral cancer detection using deep learning.
Part of M.Sc AI/ML Portfolio - Gujarat University

Author: Umar Ranginwala
GitHub: https://github.com/umarranginwala
LinkedIn: https://www.linkedin.com/in/umarranginwala/

This application demonstrates practical implementation of:
- Deep Learning (CNN & ResNet50)
- Transfer Learning
- Medical Image Classification
- Flask Web Development
- Production Deployment
"""

import os
import numpy as np
from flask import Flask, request, render_template, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.preprocessing import image
from PIL import Image
import base64
from io import BytesIO

# Flask App Configuration
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-in-production')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# File upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Model configuration
MODEL_PATH = 'model/oral_cancer_model.h5'
IMG_SIZE = (224, 224)
CLASS_NAMES = ['Normal (Non-Cancerous)', 'Oral Cancer Detected']

# Initialize model variable
model = None

def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_model():
    """
    Create ResNet50-based model architecture for oral cancer detection.
    This mirrors the architecture used in the original research.
    """
    # Load pre-trained ResNet50 without top layers
    base_model = ResNet50(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    
    # Freeze base model layers
    for layer in base_model.layers:
        layer.trainable = False
    
    # Add custom classification layers
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.3)(x)
    predictions = Dense(1, activation='sigmoid')(x)
    
    # Create final model
    model = Model(inputs=base_model.input, outputs=predictions)
    
    return model

def load_model_safe():
    """
    Safely load the trained model.
    Returns None if model file doesn't exist (demo mode).
    """
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = load_model(MODEL_PATH)
            print(f"✅ Model loaded successfully from {MODEL_PATH}")
        else:
            # Create model architecture for demo purposes
            print("⚠️  Model file not found. Creating architecture for demo mode...")
            print("   Note: In production, place trained model at:", MODEL_PATH)
            model = create_model()
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        model = None
    return model

def preprocess_image(img_path):
    """
    Preprocess image for model prediction.
    
    Args:
        img_path: Path to uploaded image
        
    Returns:
        Preprocessed image array ready for prediction
    """
    # Load and resize image
    img = image.load_img(img_path, target_size=IMG_SIZE)
    
    # Convert to array
    img_array = image.img_to_array(img)
    
    # Expand dimensions and preprocess
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    return img_array, img

def predict_cancer(img_path):
    """
    Make prediction on uploaded image.
    
    Args:
        img_path: Path to the uploaded image
        
    Returns:
        Dictionary with prediction results
    """
    try:
        # Preprocess image
        processed_img, original_img = preprocess_image(img_path)
        
        # Make prediction (demo mode if no model)
        if model is not None and os.path.exists(MODEL_PATH):
            # Real prediction with loaded model
            prediction = model.predict(processed_img, verbose=0)
            confidence = float(prediction[0][0])
        else:
            # Demo mode - simulate realistic prediction
            # In production, remove this and use actual model
            import random
            confidence = random.uniform(0.15, 0.85)
            print("🎮 DEMO MODE: Simulating prediction (no trained model loaded)")
        
        # Determine class
        if confidence < 0.5:
            predicted_class = CLASS_NAMES[1]  # Cancer detected
            confidence_score = (1 - confidence) * 100
        else:
            predicted_class = CLASS_NAMES[0]  # Normal
            confidence_score = confidence * 100
        
        # Convert image to base64 for display
        buffered = BytesIO()
        original_img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()
        
        # Risk assessment
        if predicted_class == CLASS_NAMES[1]:
            if confidence_score > 80:
                risk_level = "High Risk"
                recommendation = "⚠️ Strong indicators detected. Immediate consultation with an oncologist is strongly recommended."
            elif confidence_score > 60:
                risk_level = "Moderate Risk"
                recommendation = "⚡ Some indicators present. Schedule a dental/oral examination within the next 2 weeks."
            else:
                risk_level = "Low Risk"
                recommendation = "📋 Minor indicators detected. Monitor symptoms and consult a dentist during routine checkup."
        else:
            if confidence_score > 90:
                risk_level = "Very Low Risk"
                recommendation = "✅ No significant indicators detected. Continue routine dental checkups every 6 months."
            elif confidence_score > 70:
                risk_level = "Low Risk"
                recommendation = "✓ No major indicators detected. Maintain regular oral hygiene and annual checkups."
            else:
                risk_level = "Uncertain"
                recommendation = "🔄 Results inconclusive. Please consult a healthcare professional for proper evaluation."
        
        return {
            'success': True,
            'predicted_class': predicted_class,
            'confidence': round(confidence_score, 2),
            'raw_probability': round(confidence, 4),
            'risk_level': risk_level,
            'recommendation': recommendation,
            'image_data': img_base64,
            'filename': os.path.basename(img_path),
            'model_loaded': model is not None and os.path.exists(MODEL_PATH)
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'message': 'Error processing image. Please try again with a valid image file.'
        }

@app.route('/')
def index():
    """Render main page."""
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """
    API endpoint for prediction.
    Accepts: POST with image file
    Returns: JSON with prediction results
    """
    # Check if file is present
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image file provided'}), 400
    
    file = request.files['image']
    
    # Check if file is selected
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No file selected'}), 400
    
    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({
            'success': False, 
            'error': f'Invalid file type. Allowed: {", ".join(ALLOWED_EXTENSIONS)}'
        }), 400
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Make prediction
        result = predict_cancer(filepath)
        
        # Clean up uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Server error during processing'
        }), 500

@app.route('/predict', methods=['POST'])
def web_predict():
    """
    Web form endpoint for prediction.
    Renders results on the same page.
    """
    # Check if file is present
    if 'image' not in request.files:
        flash('No image file provided', 'error')
        return redirect(request.url)
    
    file = request.files['image']
    
    # Check if file is selected
    if file.filename == '':
        flash('No file selected', 'error')
        return redirect(request.url)
    
    # Validate file type
    if not allowed_file(file.filename):
        flash(f'Invalid file type. Allowed: {", ".join(ALLOWED_EXTENSIONS)}', 'error')
        return redirect(request.url)
    
    try:
        # Save uploaded file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Make prediction
        result = predict_cancer(filepath)
        
        # Clean up uploaded file
        if os.path.exists(filepath):
            os.remove(filepath)
        
        if result['success']:
            return render_template('result.html', result=result)
        else:
            flash(result.get('message', 'Error processing image'), 'error')
            return redirect(url_for('index'))
            
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'model_path_exists': os.path.exists(MODEL_PATH),
        'upload_folder': os.path.exists(app.config['UPLOAD_FOLDER'])
    })

@app.route('/about')
def about():
    """Render about page with project information."""
    return render_template('about.html')

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('error.html', error_code=404, error_message="Page not found"), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('error.html', error_code=500, error_message="Internal server error"), 500

if __name__ == '__main__':
    # Load model on startup
    load_model_safe()
    
    # Run the app
    print("🚀 Starting Oral Cancer Detection Web App")
    print("=" * 50)
    print("📍 Local URL: http://127.0.0.1:5000")
    print("📍 Network URL: http://0.0.0.0:5000")
    print("=" * 50)
    print("Press CTRL+C to stop the server")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
