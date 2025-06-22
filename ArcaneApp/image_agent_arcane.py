from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import requests
import shutil
import os
import base64

app = FastAPI()

# Allow frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Local Stable Diffusion API endpoint (e.g., AUTOMATIC1111's WebUI)
IMAGE_GEN_API_URL = "http://localhost:7860/sdapi/v1/img2img"

@app.post("/generate-image")
async def generate_image(
    file: UploadFile = File(...),
    style: str = Form(...)
):
    # Save uploaded image temporarily
    temp_image_path = f"temp_{file.filename}"
    with open(temp_image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Prepare prompt based on style
    prompt = f"Create a {style} style portrait based on the uploaded photo."

    # Read and encode image to base64
    with open(temp_image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode()

    # Construct payload for local Stable Diffusion API
    json_data = {
        "init_images": [base64_image],
        "prompt": prompt,
        "strength": 0.75,
        "denoising_strength": 0.7,
        "sampler_name": "Euler a",
        "cfg_scale": 7,
        "steps": 30
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(IMAGE_GEN_API_URL, headers=headers, json=json_data)
        response.raise_for_status()
        result = response.json()

        # Save generated image to a file if available
        if "images" in result:
            output_base64 = result["images"][0]
            output_bytes = base64.b64decode(output_base64)
            output_path = f"generated_{file.filename}"
            with open(output_path, "wb") as out_file:
                out_file.write(output_bytes)
            return JSONResponse(content={"status": "success", "output_path": output_path})
        else:
            return JSONResponse(content={"status": "error", "message": "No image returned"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"status": "error", "message": str(e)}, status_code=500)
    finally:
        os.remove(temp_image_path)

# To run:
# uvicorn image_agent_arcane:app --reload
