import re

def extract_possible_plates(results):
    plates = []
    plate_pattern = r"\b[A-Z]{3}[0-9][0-9A-Z][0-9]{2}\b"
    for _, text, confidence in results:
        text = text.upper().replace(" ", "")
        if re.match(plate_pattern, text):
            plates.append((text, confidence))
    return plates
