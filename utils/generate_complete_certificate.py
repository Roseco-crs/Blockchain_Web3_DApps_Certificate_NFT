import cv2
import numpy as np
import os
from datetime import datetime

os.chdir('..')
grade = "Excellent"
certificate_folder = 'certificate'
logo_path = os.path.join(certificate_folder, "10Academy_logo.png") 
certificate_background_path = os.path.join(certificate_folder, "certificate_background.png")


def generate_certificate(full_name, logo_path, certificate_background_path, grade):
    # Load certificate background image
    certificate_bg = cv2.imread(certificate_background_path)
    # Load logo
    logo = cv2.imread(logo_path)
    logo = cv2.resize(logo, (160, 160))       # Resize logo as needed

    # Define text parameters
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (0, 0, 0)     # Black color

    # Put Full name on the certificate
    name_position = (200, 300)
    cv2.putText(certificate_bg, full_name, name_position, font, font_scale, font_color, font_thickness)

    # Put Logo on the certificate
    logo_position = (460, 20)
    certificate_bg[logo_position[1]:logo_position[1]+logo.shape[0], 
                                logo_position[0]:logo_position[0]+logo.shape[1]] = logo
    
    # Put Date on the certificate
    date = datetime.now().strftime('%Y-%m-%d')
    date_position = (400, 450)
    cv2.putText(certificate_bg, f'Date: {date}', date_position, font, font_scale, font_color, font_thickness)

    # Put Grade on the certificate
    grade = grade 
    grade_position = (400, 550)
    cv2.putText(certificate_bg, f"Grade: {grade}", grade_position, font, font_scale, font_color, font_thickness)

    # Put Founder
    ceo = "10Academy Founders"
    ceo_position = (200, 700)
    cv2.putText(certificate_bg, f"Certified by: {ceo}", ceo_position, font, font_scale, font_color, font_thickness)

    # Save the generated certificate
    output_path = "certificate/generated_certificate.png"
    cv2.imwrite(output_path, certificate_bg)

    # Display the generated certificate
    cv2.imshow('Generated Certificate', certificate_bg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
full_name = "Coffi Rodolphe Segbedji"
generate_certificate(full_name, logo_path, certificate_background_path, grade)


