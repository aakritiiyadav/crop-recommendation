import os
import urllib.request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
CSV_PATH = os.path.join(DATA_DIR, 'crop_recommendation.csv')
MODEL_PATH = os.path.join(MODELS_DIR, 'crop_recommendation_model.pkl')
ENCODER_PATH = os.path.join(MODELS_DIR, 'label_encoder.pkl')

# URL of the Crop Recommendation dataset
DATASET_URL = "https://raw.githubusercontent.com/Gladiator07/Harvestify/master/Data-processed/crop_recommendation.csv"

def ensure_directories():
    """Ensure that data and models directories exist."""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(MODELS_DIR, exist_ok=True)
    print(f"Directories verified: {DATA_DIR}, {MODELS_DIR}")

def download_dataset():
    """Download the crop recommendation dataset if it doesn't exist."""
    if not os.path.exists(CSV_PATH):
        print(f"Downloading dataset from: {DATASET_URL} ...")
        try:
            urllib.request.urlretrieve(DATASET_URL, CSV_PATH)
            print(f"Dataset successfully downloaded to: {CSV_PATH}")
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            raise
    else:
        print(f"Dataset already exists at: {CSV_PATH}")

def train_and_evaluate():
    """Train Random Forest model and save artifacts."""
    print("Loading dataset...")
    df = pd.read_csv(CSV_PATH)
    
    print("\nDataset columns:", df.columns.tolist())
    print("Dataset shape:", df.shape)
    print("\nCrop distribution:")
    crop_counts = df['label'].value_counts()
    for crop, count in crop_counts.items():
        print(f"  - {crop}: {count}")
    
    # Split features and target
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    
    # Encode target labels
    print("\nEncoding target labels...")
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    
    # Initialize and train Random Forest Classifier
    print("\nTraining Random Forest Classifier...")
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=15)
    rf_model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = rf_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
    
    print("\nClassification Report:")
    target_names = label_encoder.classes_
    print(classification_report(y_test, y_pred, target_names=target_names))
    
    # Save model and label encoder
    print(f"\nSaving model to: {MODEL_PATH}")
    joblib.dump(rf_model, MODEL_PATH)
    
    print(f"Saving label encoder to: {ENCODER_PATH}")
    joblib.dump(label_encoder, ENCODER_PATH)
    
    print("\nModel training workflow completed successfully!")

if __name__ == "__main__":
    ensure_directories()
    download_dataset()
    train_and_evaluate()
