import os
import csv

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

# Counters
ai_ml_files = 0
total_ai_ml_functions = 0
total_ai_ml_libraries = 0

# Scan files for AI/ML-related keywords
def scan_code_files():
    global ai_ml_files, total_ai_ml_functions, total_ai_ml_libraries
    ai_ml_detected = {}

    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".js", ".java")):  # Check only Python, Java, JS files
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read().lower()

                        # Check for AI/ML-related functions and libraries
                        matches = [kw for kw in ai_ml_keywords if kw in content]
                        lib_matches = [lib for lib in ai_ml_libraries if lib in content]

                        if matches or lib_matches:
                            ai_ml_files += 1
                            total_ai_ml_functions += len(matches)
                            total_ai_ml_libraries += len(lib_matches)
                            ai_ml_detected[file_path] = {"functions": matches, "libraries": lib_matches}

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return ai_ml_detected

# Run the scanner
detected_code = scan_code_files()

# Print summary
print("\nAI/ML Code Detection Summary:")
print(f"Total AI/ML-related files: {ai_ml_files}")
print(f"Total AI/ML-related libraries used: {total_ai_ml_libraries}")
print(f"Total AI/ML-related functions used: {total_ai_ml_functions}")

# Print detailed findings
if detected_code:
    print("\nAI/ML-related files:")
    for file, details in detected_code.items():
        print(f"{file}")
        if details["functions"]:
            print(f"Functions/Keywords: {', '.join(details['functions'])}")
        if details["libraries"]:
            print(f"Libraries: {', '.join(details['libraries'])}")
    exit(1)  # Fail the job if AI/ML code is detected
else:
    print("No AI/ML-related code detected.")

csv_file = "AIML_detect.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Project", "Total Files", "Total Libraries", "Total Functions"])
    writer.writerow(["EmptyRepo", ai_ml_files, total_ai_ml_libraries, total_ai_ml_functions])
