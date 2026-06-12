# FabricCheck — Fabric Defect Detection System

**Course:** Python Programming  
**Senior Project:** Fabric And Defect Detection System Using AI  

## 1. Group Members
- **Baraa Zakarneh** — 202112875 — Responsible for: `image_loader.py`, `create_test_fabric.py`
- **Iyad Kmail** — 202210792 — Responsible for: `defect_detector.py`, `requirements.txt`
- **Mohammad Kmail** — 202210856 — Responsible for: `annotator.py`, `main.py`

**GitHub Repository:** [https://github.com/baraazaka/Zakarneh_Kmail.git](https://github.com/baraazaka/Zakarneh_Kmail.git)

---

## 2. Project Description
FabricCheck is an automated system designed to identify defects in textile materials using classical Computer Vision techniques. The application performs a full pipeline: loading fabric images, pre-processing them to remove noise, applying Otsu's thresholding to isolate defects, and analyzing the contours of these defects. Based on the size and frequency of detected anomalies, it classifies the fabric's quality into categories: Good, Low, Medium, or High severity.

---

## 3. Libraries Used

| Library | Version | How it was used |
|---|---|---|
| **Pillow** | >= 10.2.0 | Loading images and resizing. |
| **opencv-python** | >= 4.9.0 | Grayscale, blurring, thresholding, and contours. |
| **numpy** | >= 1.26.4 | Array operations and area calculations. |
| **matplotlib** | >= 3.8.3 | Side-by-side visualization. |

---

## 4. Module Descriptions

- **`image_loader.py` (Baraa):** Handles image loading and ensures resizing to 512px width while keeping the aspect ratio.
- **`defect_detector.py` (Iyad):** The core engine that applies Gaussian Blur, Otsu's threshold, and filters out small noise.
- **`annotator.py` (Mohammad):** Draws red bounding boxes around defects and generates the JSON report.
- **`main.py` (Mohammad):** The orchestration script that runs the entire pipeline end-to-end.

---

## 5. Test Cases

### Test 1: `threshold()` Logic
- **Input:** Blurred grayscale array.
- **Output:** Binary array (0 and 255 only). 

### Test 2: `classify_severity()`
- **Input:** 8 defects (> 5% area).
- **Output:** "High — Severe defects". 

---

## 6. Screenshots

### Side-by-Side Comparison
![Comparison](screenshots/comparison_view.png)  
*Original vs Annotated*

---

## 7. Individual Contributions

| Student | ID | Files | Commit Count | GitHub Username |
|---|---|---|---|---|
| **Baraa Zakarneh** | 202112875 | `image_loader.py`, `create_test_fabric.py` | 6 | `@baraazaka` |
| **Iyad Kmail** | 202210792 | `defect_detector.py`, `requirements.txt` | 9 | `@eyadki345-lgtm` |
| **Mohammad Kmail** | 202210856 | `annotator.py`, `main.py` | 7 | `@mohammedkmail` |

---

## 8. Challenges & Learning

- **Baraa:** Maintaining aspect ratio during resize using `thumbnail()`.
- **Iyad:** Fine-tuning Otsu's threshold for different fabric textures.
- **Mohammad:** Handling NumPy-to-JSON serialization errors using `int()`.

---

## 9. How to Run
```bash
pip install -r requirements.txt
python create_test_fabric.py
python main.py
