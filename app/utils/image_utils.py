import cv2
import numpy as np
from PIL import Image


class ImageUtils:

    @staticmethod
    def read_image(image_path):
        """
        Read image using OpenCV
        """
        image = cv2.imread(image_path)

        if image is None:
            raise ValueError("Unable to read image.")

        return image

    @staticmethod
    def resize_image(image, width=224, height=224):
        """
        Resize image for EfficientNet
        """
        return cv2.resize(image, (width, height))

    @staticmethod
    def convert_bgr_to_rgb(image):
        """
        Convert OpenCV image to RGB
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    @staticmethod
    def normalize_image(image):
        """
        Normalize image between 0 and 1
        """
        image = image.astype(np.float32)
        image = image / 255.0
        return image

    @staticmethod
    def prepare_for_efficientnet(image_path):
        """
        Complete preprocessing pipeline
        """
        image = ImageUtils.read_image(image_path)

        image = ImageUtils.resize_image(image)

        image = ImageUtils.convert_bgr_to_rgb(image)

        image = ImageUtils.normalize_image(image)

        image = np.expand_dims(image, axis=0)

        return image

    @staticmethod
    def save_processed_image(image, output_path):
        """
        Save processed image
        """
        cv2.imwrite(output_path, image)