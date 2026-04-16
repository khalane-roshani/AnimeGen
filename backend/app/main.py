import onnxruntime as ort
import cv2
import numpy as np
import sys
import os


class AnimeGAN:
    def __init__(self, model_path):
        # Load ONNX model
        self.session = ort.InferenceSession(model_path)
        self.input_name = self.session.get_inputs()[0].name

        # Print model input shape (for debugging)
        print("Model input shape:", self.session.get_inputs()[0].shape)

    def stylize(self, input_path, output_path):

        # Read image
        img = cv2.imread(input_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize to multiple of 32
        h, w, _ = img.shape
        h = (h // 32) * 32
        w = (w // 32) * 32
        img = cv2.resize(img, (w, h))

        # Normalize to [-1, 1]
        img = img.astype(np.float32) / 127.5 - 1.0

        # Add batch dimension (NHWC format)
        input_tensor = np.expand_dims(img, axis=0)

        # Run model
        output = self.session.run(None, {self.input_name: input_tensor})[0]

        # Remove batch dimension
        output = output[0]

        # Convert back to image
        output = (output + 1.0) * 127.5
        output = np.clip(output, 0, 255).astype(np.uint8)

        output = cv2.cvtColor(output, cv2.COLOR_RGB2BGR)
        cv2.imwrite(output_path, output)

        print("Anime image generated successfully!")
        print("Saved at:", output_path)

def run_model(input_path, output_path):
    # Get current file directory (backend/app/)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Go to backend/models/
    model_path = os.path.join(BASE_DIR, "..", "models", "AnimeGANv2_Hayao.onnx")
    model_path = os.path.abspath(model_path)

    # Debug (optional)
    print("Model path:", model_path)
    print("Exists:", os.path.exists(model_path))

    model = AnimeGAN(model_path)

    model.stylize(input_path, output_path)


def run_model_neon(input_path, output_path):
    # Get current file directory (backend/app/)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Go to backend/models/
    model_path = os.path.join(BASE_DIR, "..", "models", "AnimeGANv2_Paprika.onnx")
    model_path = os.path.abspath(model_path)

    # Debug (optional)
    print("Model path:", model_path)
    print("Exists:", os.path.exists(model_path))

    model = AnimeGAN(model_path)

    model.stylize(input_path, output_path)


def run_model_cinematic(input_path, output_path):
    # Get current file directory (backend/app/)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # Go to backend/models/
    model_path = os.path.join(BASE_DIR, "..", "models", "AnimeGANv2_Shinkai.onnx")
    model_path = os.path.abspath(model_path)

    # Debug (optional)
    print("Model path:", model_path)
    print("Exists:", os.path.exists(model_path))

    model = AnimeGAN(model_path)

    model.stylize(input_path, output_path)