import sys
import json
import requests
from google import genai
from google.genai import types

GOOGLE_API_KEY = "AIzaSyAGTgandeECziJqABnG3uznVCTlVltSaUc"

MODELS = {
    "nb2":   "gemini-3.1-flash-image-preview",  # Nano Banana 2
    "nbpro": "gemini-3-pro-image-preview",       # Nano Banana Pro
}

def run():
    if len(sys.argv) < 3:
        print("Usage: python generate_image.py <prompt_json_file> <output_file> [aspect_ratio] [model]")
        print("  aspect_ratio: 1:1 (default), 16:9, 9:16, 4:5, 4:3, 3:4, 21:9, etc.")
        print("  model:        nb2 (Nano Banana 2, default) | nbpro (Nano Banana Pro) | full model ID")
        sys.exit(1)

    prompt_file  = sys.argv[1]
    output_file  = sys.argv[2]
    aspect_ratio = sys.argv[3] if len(sys.argv) > 3 else "1:1"
    model_arg    = sys.argv[4] if len(sys.argv) > 4 else "nb2"
    model        = MODELS.get(model_arg, model_arg)

    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt_json = json.load(f)

    # Build prompt text — embed negative prompt as an instruction
    prompt_text     = prompt_json.get("prompt", "")
    negative_prompt = prompt_json.get("negative_prompt", "")
    if negative_prompt:
        prompt_text += f"\n\nDo NOT include any of the following: {negative_prompt}"

    api_parameters    = prompt_json.get("api_parameters", {})
    ar                = api_parameters.get("aspect_ratio", aspect_ratio)
    resolution        = api_parameters.get("resolution", "1K")
    use_google_search = api_parameters.get("google_search", False)

    # Build content parts (text first, then any reference images)
    parts = [prompt_text]

    image_input = prompt_json.get("image_input", [])
    for img_url in image_input:
        print(f"Fetching reference image: {img_url}")
        try:
            img_resp = requests.get(img_url, timeout=30)
            img_resp.raise_for_status()
        except Exception as e:
            print(f"ERROR fetching reference image: {e}")
            sys.exit(1)

        url_clean = img_url.lower().split('?')[0]
        if url_clean.endswith('.png'):
            mime = 'image/png'
        elif url_clean.endswith('.webp'):
            mime = 'image/webp'
        else:
            mime = 'image/jpeg'

        parts.append(types.Part.from_bytes(data=img_resp.content, mime_type=mime))

    client = genai.Client(api_key=GOOGLE_API_KEY)

    config_kwargs = {
        "image_config": types.ImageConfig(
            aspect_ratio=ar,
            image_size=resolution,
        )
    }
    if use_google_search:
        config_kwargs["tools"] = [types.Tool(google_search=types.GoogleSearch())]

    print(f"Generating image: model={model}  aspect_ratio={ar}  resolution={resolution}")

    try:
        response = client.models.generate_content(
            model=model,
            contents=parts,
            config=types.GenerateContentConfig(**config_kwargs),
        )
    except Exception as e:
        print(f"ERROR generating image: {e}")
        sys.exit(1)

    for part in response.parts:
        if part.text:
            print(f"Model: {part.text}")
        if part.inline_data is not None:
            with open(output_file, 'wb') as f:
                f.write(part.inline_data.data)
            print(f"Successfully saved to {output_file}")
            sys.exit(0)

    print("ERROR: No image returned in response.")
    sys.exit(1)

if __name__ == "__main__":
    run()
