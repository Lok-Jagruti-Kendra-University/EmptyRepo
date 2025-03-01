import json
import re

# Define AI/ML-related libraries and function calls
AI_LIBRARIES = ["tensorflow", "pytorch", "scikit-learn", "keras", "xgboost", "torch", "fastai", "cv2", "nltk"]
AI_FUNCTIONS = ["fit", "predict", "train", "evaluate", "transform", "generate", "preprocess"]

# Define AI-related file paths
AI_PATHS = ["models/", "ml/", "training/", "ai/", "deep_learning/"]

def load_sonar_report(report_file):
    """ Load the SonarCloud JSON report """
    with open(report_file, "r") as file:
        return json.load(file)

def detect_ai_in_code(code):
    """ Scan for AI-related libraries and function calls in code """
    found_libs = [lib for lib in AI_LIBRARIES if lib in code.lower()]
    found_funcs = [func for func in AI_FUNCTIONS if re.search(rf"\b{func}\b", code)]
    return found_libs, found_funcs

def analyze_sonar_data(sonar_data):
    """ Analyze SonarCloud report for AI/ML usage """
    ai_detected_files = []
    total_files = len(sonar_data.get("issues", []))

    for issue in sonar_data.get("issues", []):
        file_path = issue.get("component", "")
        code = issue.get("message", "")

        # Check if the file is in an AI-related directory
        is_ai_file = any(ai_dir in file_path for ai_dir in AI_PATHS)

        # Check for AI-related libraries and function calls
        found_libs, found_funcs = detect_ai_in_code(code)

        if is_ai_file or found_libs or found_funcs:
            ai_detected_files.append({
                "file": file_path,
                "ai_libraries": found_libs,
                "ai_functions": found_funcs,
                "is_ai_related_path": is_ai_file
            })

    return ai_detected_files, total_files

def generate_report(ai_files, total_files):
    """ Generate a summary report """
    print("\n🔍 AI/ML Detection Report from SonarCloud Analysis 🔍")
    print("=" * 50)
    print(f"📂 Total Files Scanned: {total_files}")
    print(f"🤖 AI/ML-Related Files Detected: {len(ai_files)}\n")

    if ai_files:
        for file in ai_files:
            print(f"📄 File: {file['file']}")
            print(f"  🔹 AI Libraries Found: {', '.join(file['ai_libraries']) if file['ai_libraries'] else 'None'}")
            print(f"  🔹 AI Functions Found: {', '.join(file['ai_functions']) if file['ai_functions'] else 'None'}")
            print(f"  🔹 AI-Related Path: {'✅ Yes' if file['is_ai_related_path'] else '❌ No'}\n")
    else:
        print("✅ No AI/ML-related code detected.")

# Run the analysis
sonar_data = load_sonar_report("sonar-report.json")
ai_detected_files, total_files = analyze_sonar_data(sonar_data)
generate_report(ai_detected_files, total_files)