import cv2
import easyocr
from recognizer.plate_utils import extract_possible_plates
from app.db import get_all_plates
import sqlite3

def is_plate_authorized(plate):
    conn = sqlite3.connect("plates.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM authorized_plates WHERE plate = ?", (plate,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def run_plate_scanner():
    cap = cv2.VideoCapture(0)
    reader = easyocr.Reader(['en'])

    print("Press 's' to scan, 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow("License Plate Scanner", frame)

        key = cv2.waitKey(1)
        if key == ord('s'):
            results = reader.readtext(frame)
            plates = extract_possible_plates(results)
            for plate, confidence in plates:
                status = "✅ AUTHORIZED" if is_plate_authorized(plate) else "❌ UNAUTHORIZED"
                print(f"{plate} ({confidence:.2f}) => {status}")
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
