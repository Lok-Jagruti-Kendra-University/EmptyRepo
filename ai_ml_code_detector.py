import os
import re

# AI/ML-related keywords
ai_ml_keywords = [
    "train", "predict", "infer", "classify", "regress", "neural", "deep learning", "machine learning",
    "ai", "ml", "dataset", "feature extraction", "nlp", "image processing", "model", "transformer",
    "lstm", "cnn", "rnn", "gradient", "hyperparameter", "fine-tune", "tokenizer"
]

# AI/ML-related libraries
ai_ml_libraries = [
    "tensorflow", "torch", "scikit-learn", "keras", "nltk", "xgboost", "pandas", "numpy",
    "scipy", "matplotlib", "opencv", "cv2", "transformers", "huggingface", "tflite",
    "pytorch", "onnx", "mlflow"
]

# Scan files for AI/ML-related keywords
def scan_code_files():
    ai_ml_detected = {}

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".js", ".java")):  # Check only Python, Java, JS
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().lower()

                        # Check for AI/ML-related function/class names
                        matches = [kw for kw in ai_ml_keywords if kw in content]
                        lib_matches = [lib for lib in ai_ml_libraries if lib in content]

                        if matches or lib_matches:
                            ai_ml_detected[file_path] = {"functions": matches, "libraries": lib_matches}

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return ai_ml_detected

# Run the scanner
detected_code = scan_code_files()

# Print findings
if detected_code:
    print("\n🔍 AI/ML-related code detected:")
    for file, details in detected_code.items():
        print(f"📂 {file}")
        if details["functions"]:
            print(f"  🔹 Functions/Keywords: {', '.join(details['functions'])}")
        if details["libraries"]:
            print(f"  📦 Libraries: {', '.join(details['libraries'])}")
    exit(1)  # Fail the job if AI/ML code is detected
else:
    print("✅ No AI/ML-related code detected.")
