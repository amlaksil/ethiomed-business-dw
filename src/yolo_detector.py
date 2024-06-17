#!/usr/bin/python3
"""
This module contains a class called 'YOLODetector' which performs
object detection using a pre-trained YOLO model.
"""
import torch
from PIL import Image
from pathlib import Path
import pandas as pd
from tqdm.notebook import tqdm


class YOLODetector:
    """
    A class to perform object detection using a pre-trained YOLO model.

    Attributes:
        model_name (str): Name of the YOLO model to be used.
        images_dir (str): Directory containing images for object detection.
        results_file (str): Path to the file where detection results will
        be saved.
        model (torch.nn.Module): The YOLO model loaded with pre-trained
        weights.
        results (list): List to store detection results.
    """

    def __init__(
            self, model_name='yolov5s', images_dir=None,
            results_file='detection_results.csv'):
        """
        Initializes the YOLODetector with the specified model, image
        directory, and results file.

        Args:
            model_name (str): The name of the YOLO model to be used.
        Default is 'yolov5s'.
            images_dir (str): The directory containing images for object
        detection. Default is None.
            results_file (str): The path to the file where detection
        results will be saved. Default is 'detection_results.csv'.
        """
        self.model_name = model_name
        self.images_dir = images_dir
        self.results_file = results_file
        self.model = self.load_model()
        self.results = []

    def load_model(self):
        """
        Loads the specified YOLO model with pre-trained weights.

        Returns:
            torch.nn.Module: The YOLO model loaded with pre-trained weights.
        """
        print(f"Loading {self.model_name} model...")
        model = torch.hub.load(
            'ultralytics/yolov5', self.model_name, pretrained=True)
        model.eval()
        return model

    def detect_objects(self, img_path):
        """
        Performs object detection on a single image.

        Parameters:
            img_path (str): The path to the image file.

        Returns:
            numpy.ndarray: Array containing detection results with
        bounding box coordinates, confidence scores, and class labels.
        """
        img = Image.open(img_path)
        detections = self.model(img)
        return detections.xyxy[0].numpy()  # store bounding box info

    def process_images(self):
        """
        Processes all images in the specified directory
        for object detection.
        """
        image_paths = list(Path(self.images_dir).glob('*.jpg'))
        for img_path in tqdm(image_paths, desc="Processing images"):
            detection = self.detect_objects(img_path)
            self.results.append((str(img_path), detection))

    def save_results(self):
        """
        Saves the detection results to a CSV file.
        """
        df_list = []
        for img_path, detection in self.results:
            for det in detection:
                row = {
                    'image_path': img_path,
                    'class': int(det[5]),  # Assuming class is at index 5
                    'confidence': float(det[4]),  # confidence is at index 4
                    'bbox': det[:4].tolist()
                }
                df_list.append(row)

        df = pd.DataFrame(df_list)
        print("Saving results to CSV...")
        df.to_csv(self.results_file, index=False)
        print(f"Results saved to {self.results_file}")

    def run(self):
        """
        Runs the complete workflow of loading
        images, detecting objects, and saving results.
        """
        self.process_images()
        self.save_results()
