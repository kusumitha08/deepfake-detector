from transformers import AutoModelForImageClassification, AutoImageProcessor
import os

model_name = "prithivMLmods/deepfake-detector-model-v1"
save_dir = "./model"

os.makedirs(save_dir, exist_ok=True)

print("Downloading model with classifier weights...")

processor = AutoImageProcessor.from_pretrained(model_name)
processor.save_pretrained(save_dir)

model = AutoModelForImageClassification.from_pretrained(model_name)
model.save_pretrained(save_dir)

print("Model downloaded & saved in ./model")
