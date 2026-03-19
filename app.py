import gradio as gr
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image
import torch
import os

# Local model path (after running download_model.py)
model_path = "./model"

# Check if model exists
if not os.path.exists(model_path):
    raise FileNotFoundError("Model not found! Run download_model.py first to download the pretrained model.")

# Load model & processor from folder
processor = AutoImageProcessor.from_pretrained(model_path)
model = SiglipForImageClassification.from_pretrained(model_path)

# Label mapping
id2label = {
    "0": "Fake",
    "1": "Real"
}

def classify_image(image):
    # Convert image to RGB
    image = Image.fromarray(image).convert("RGB")

    # Process image
    inputs = processor(images=image, return_tensors="pt")

    # Model inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1).squeeze().tolist()

    # Create results dictionary
    result = {id2label[str(i)]: round(probs[i], 3) for i in range(len(probs))}

    return result

# Gradio UI
iface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="numpy", label="Upload face image"),
    outputs=gr.Label(num_top_classes=2, label="Deepfake Detection"),
    title="AI Deepfake Detection",
    description="Upload an image to detect whether the face is REAL or FAKE."
)

if __name__ == "__main__":
    iface.launch(share=True)
