from image_loader import ImageLoader
from defect_detector import DefectDetector
from annotator import Annotator

def main():
    INPUT_IMAGE  = "fabric_sample.png"
    OUTPUT_IMAGE = "fabric_annotated.png"
    REPORT_FILE  = "defect_report.json"

    loader   = ImageLoader()
    detector = DefectDetector()
    ann      = Annotator()

    # Step 1: Load image
    print("[1/5] Loading image...")
    image       = loader.load_image(INPUT_IMAGE)
    image       = loader.resize_image(image)
    img_array   = loader.to_numpy(image)
    image_area  = img_array.shape[0] * img_array.shape[1]

    # Step 2: Detect defects
    print("[2/5] Detecting defects...")
    gray        = detector.to_grayscale(img_array)
    blurred     = detector.reduce_noise(gray)
    binary      = detector.threshold(blurred)
    contours    = detector.find_contours(binary)
    defects     = detector.filter_contours(contours)
    severity    = detector.classify_severity(defects, image_area)
    boxes       = detector.get_bounding_boxes(defects)

    print(f"      Defects found : {len(defects)}")
    print(f"      Severity      : {severity}")

    # Step 3: Annotate
    print("[3/5] Annotating image...")
    annotated = ann.draw_boxes(img_array, boxes, severity)

    # Step 4: Save outputs
    print("[4/5] Saving outputs...")
    ann.save_annotated(annotated, OUTPUT_IMAGE)
    ann.save_report(REPORT_FILE, INPUT_IMAGE, boxes, severity)

    # Step 5: Display
    print("[5/5] Displaying comparison...")
    ann.show_comparison(img_array, annotated, severity)

    print("\nDone!")

if __name__ == "__main__":
    main()