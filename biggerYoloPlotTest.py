import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from PIL import Image

# Path to the images folder
image_folder = "cropped_images_train/cropped_images/images"

# Load the first image
image_filename = "chart_100.png"
image_path = os.path.join(image_folder, image_filename)
image = Image.open(image_path)

# Load the YOLO annotation for the first image
yolo_annotation_filename = "chart_100.txt"
yolo_annotation_path = os.path.join(image_folder, yolo_annotation_filename)

# Define the bounding box size
bbox_size = 3

# Get image dimensions
image_width, image_height = image.size

# Read the YOLO annotation
with open(yolo_annotation_path, "r") as f:
    yolo_annotations = f.readlines()

# Create a plot to display the image and bounding boxes
plt.imshow(image)
ax = plt.gca()

# Loop over the YOLO annotations and plot each bounding box
for annotation in yolo_annotations:
    # Split the annotation into its components
    parts = annotation.split()

    # Extract the center coordinates and bounding box dimensions
    x_center_norm = float(parts[1])
    y_center_norm = float(parts[2])
    bbox_width_norm = float(parts[3])
    bbox_height_norm = float(parts[4])

    # Convert normalized coordinates to pixel values
    x_center = x_center_norm * image_width
    y_center = y_center_norm * image_height
    bbox_width = bbox_width_norm * image_width
    bbox_height = bbox_height_norm * image_height

    # Calculate the top-left corner of the bounding box
    top_left_x = x_center - bbox_width / 2
    top_left_y = y_center - bbox_height / 2

    # Create a rectangle for the bounding box
    bbox = plt.Rectangle(
        (top_left_x, top_left_y),
        bbox_width,
        bbox_height,
        linewidth=1,
        edgecolor='r',
        facecolor='none'
    )

    # Add the bounding box to the plot
    ax.add_patch(bbox)

# Display the plot
plt.show()