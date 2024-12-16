import pandas as pd
from PIL import Image
import os

# Path to the images folder
image_folder = "cropped_images_train/cropped_images/"

# Read CSV file
data = pd.read_csv("updated_data.csv")

# Define bounding box size (5x5 grid)
bbox_size = 5

# Iterate over rows in the CSV
for index, row in data.iterrows():
    # Get the image file name
    image_filename = f"chart_{row['id']}.png"
    image_path = os.path.join(image_folder, image_filename)

    # Open the image to get its width and height
    with Image.open(image_path) as img:
        image_width, image_height = img.size

    # Extract keypoints (assuming boxes is a 2D array as a string)
    keypoints = eval(row["boxes"])

    # Create YOLO annotation content
    yolo_annotations = []
    for kp in keypoints:
        # Extract the x and y coordinates of the keypoint
        x_center = kp[0]
        y_center = kp[1]

        # Normalize coordinates
        x_center_norm = x_center / image_width
        y_center_norm = y_center / image_height

        # Normalize the bounding box width and height
        bbox_width_norm = bbox_size / image_width
        bbox_height_norm = bbox_size / image_height

        # YOLO syntax: class (0), x_center, y_center, width, height
        yolo_annotations.append(
            f"0 {x_center_norm:.6f} {y_center_norm:.6f} {bbox_width_norm:.6f} {bbox_height_norm:.6f}"
        )

    # Write YOLO annotations to a file
    yolo_annotation_filename = f"chart_{row['id']}.txt"
    yolo_annotation_path = os.path.join(image_folder, yolo_annotation_filename)
    with open(yolo_annotation_path, "w") as f:
        for annotation in yolo_annotations:
            f.write(annotation + "\n")
