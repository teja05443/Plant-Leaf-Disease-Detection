# README.md

"""
# Plant Leaf Disease Detection using AWS Rekognition

This project demonstrates how to use AWS Rekognition Custom Labels for detecting plant leaf diseases. The model is trained using a dataset of 5000+ images from Roboflow and is integrated with a Python application leveraging the Boto3 library and AWS Cloud9.

## Dataset
- **Total Images**: 1608
- **Annotations**: COCO format
- **Pre-processing Applied**:
  - Auto-orientation of pixel data (with EXIF-orientation stripping)
  - Resize to 640x640 (Stretch)

- **Augmentation Applied**:
  - 90-degree rotations: none, clockwise, counter-clockwise
  - Random rotation between -15 and +15 degrees
  - Random shear between -10° and +10° horizontally and -10° and +10° vertically
  - Random brightness adjustment between -20% and +20%

The Dataset can be downloaded from https://universe.roboflow.com/plant-disease-n10iv/plant-disease-detection-ryzqa/dataset/6
### Dataset Setup

1. **Download the Dataset**

   Download the dataset from Roboflow or the provided source.

2. **Place the Dataset in the Project**

   Create a directory named `data` in the project root and place the dataset in it:

   ```bash
   mkdir -p data/sample_images
   cp /path/to/downloaded/images/* data/sample_images/

## Features
- **Start the Model**: Start the AWS Rekognition Custom Labels model for inference.
- **Detect Disease**: Detect plant leaf diseases by analyzing images stored in an S3 bucket.
- **Stop the Model**: Stop the AWS Rekognition model to save resources.

## Getting Started

### Prerequisites
- **Python 3.7+**
- **AWS Account**: Set up AWS credentials with permissions for Rekognition, S3, etc.
- **Boto3**: AWS SDK for Python.
- **Pillow**: Python Imaging Library for image processing.

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/plant-leaf-disease-detection.git
   cd plant-leaf-disease-detection

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set Up AWS Credentials**
Ensure that your AWS credentials are configured properly in a credentials.py file that is excluded from version control via .gitignore.

**Acknowledgments**
Thanks to Roboflow for the dataset.
AWS Rekognition for providing powerful image recognition capabilities.

You can copy the entire content into a Python file (e.g., `project.py`). The `README.md` is embedded as a multi-line string at the top, and all the Python scripts are included within the same file.

"""

