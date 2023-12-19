import pytesseract
from PIL import Image


def extract_business_card_data(image_path):
    try:
        # Load the image using PIL (Python Imaging Library)
        image = Image.open(image_path)

        # Use Tesseract to perform OCR on the image
        ocr_text = pytesseract.image_to_string(image)

        # Process the extracted text to identify different fields
        business_card_data = {}
        lines = ocr_text.split('\n')

        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                business_card_data[key.strip()] = value.strip()

        return business_card_data

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    image_path = "path_to_your_business_card_image.jpg"

    extracted_data = extract_business_card_data(image_path)

    if extracted_data:
        print("Extracted Business Card Data:")
        for key, value in extracted_data.items():
            print(f"{key}: {value}")
    else:
        print("Business card data extraction failed.")
