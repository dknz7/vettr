---
name: Nano Banana 2 Image Generation Master
description: A formalized skill for generating hyper-realistic, highly-controlled images using the Nano Banana 2 (Gemini 3.1 Flash) model through parameterized JSON prompting.
---

# Nano Banana 2 Image Generation Master

## Goal
The purpose of this skill is to provide a standardized, highly controlled method for generating images using AI model Nano Banana 2 (or any underlying model connected to the `generate_image` tool). By strictly enforcing a structured JSON parameter schema, this skill neutralizes native model biases (like over-smoothing, dataset-averaging, or "plastic" AI styling) and ensures raw, unretouched, hyper-realistic outputs.

## Prerequisites
- Access to the `generate_image` tool.
- A clear understanding of the user's desired Subject, Lighting, and Camera characteristics.

## Core Schema Structure
When constructing a prompt for the `generate_image` tool, you **MUST** use the following JSON schema as the foundation. Fill in the string values with extreme, microscopic detail.

```json
{
  "task": "string - High-level goal (e.g., 'sports_selfie_collage', 'single_macro_portrait')",
  
  "output": {
    "type": "string - e.g., 'single_image', '4-panel_collage'",
    "layout": "string - e.g., '1x1', '2x2_grid', 'side-by-side'",
    "aspect_ratio": "string - e.g., '3:4', '16:9', '4:5'",
    "resolution": "string - e.g., 'ultra_high', 'medium_low'",
    "camera_style": "string - e.g., 'smartphone_front_camera', 'professional_dslr'"
  },

  "image_quality_simulation": {
    "sharpness": "string - e.g., 'tack_sharp', 'slightly_soft_edges'",
    "noise": "string - e.g., 'unfiltered_sensor_grain', 'visible_film_grain', 'clean_digital'",
    "compression_artifacts": "boolean - true if attempting to simulate uploaded UGC",
    "dynamic_range": "string - e.g., 'limited', 'hdr_capable'",
    "white_balance": "string - e.g., 'slightly_warm', 'cool_fluorescent'",
    "lens_imperfections": [
      "array of strings - e.g., 'subtle chromatic aberration', 'minor lens distortion', 'vignetting'"
    ]
  },

  "subject": {
    "type": "string - e.g., 'human_portrait', 'nature_macro', 'infographic_flatlay'",
    "human_details": {
      "//": "Use this block ONLY for human subjects",
      "identity": "string",
      "appearance": "string - Extremely specific (e.g., visible pores, mild redness)",
      "outfit": "string"
    },
    "object_or_nature_details": {
      "//": "Use this block for non-human subjects",
      "material_or_texture": "string - e.g., 'brushed aluminum', 'dew-covered velvety petals'",
      "wear_and_tear": "string - e.g., 'subtle scratches on the anodized finish', 'browning edges on leaves'",
      "typography": "string - e.g., 'clean sans-serif overlaid text, perfectly legible'"
    }
  },

  "multi_panel_layout": {
    "grid_panels": [
      {
        "panel": "string - e.g., 'top_left', 'full_frame' (if not a grid)",
        "pose": "string - e.g., 'slight upward selfie angle, relaxed smile'",
        "action": "string - e.g., 'holding phone with one hand, casual posture'"
      }
    ]
  },

  "environment": {
    "location": "string - e.g., 'gym or outdoor sports area'",
    "background": "string - What is behind the subject (e.g., 'blurred gym equipment')",
    "lighting": {
      "type": "string - e.g., 'natural or overhead gym lighting', 'harsh direct sunlight'",
      "quality": "string - e.g., 'uneven, realistic, non-studio', 'high-contrast dramatic'"
    }
  },

  "embedded_text_and_overlays": {
    "text": "string (optional)",
    "location": "string (optional)"
  },

  "structural_preservation": {
    "preservation_rules": [
      "array of strings - e.g., 'Exact physical proportions must be preserved'"
    ]
  },

  "controlnet": {
    "pose_control": {
      "model_type": "string - e.g., 'DWPose'",
      "purpose": "string",
      "constraints": ["array of strings"],
      "recommended_weight": "number"
    },
    "depth_control": {
      "model_type": "string - e.g., 'ZoeDepth'",
      "purpose": "string",
      "constraints": ["array of strings"],
      "recommended_weight": "number"
    }
  },

  "explicit_restrictions": {
    "no_professional_retouching": "boolean - typically true for realism",
    "no_studio_lighting": "boolean - typically true for candid shots",
    "no_ai_beauty_filters": "boolean - mandatory true to avoid plastic look",
    "no_high_end_camera_look": "boolean - true if simulating smartphones"
  },

  "negative_prompt": {
    "forbidden_elements": [
      "array of strings - Massive list of 'AI style' blockers required for extreme realism. Example stack: 'anatomy normalization', 'body proportion averaging', 'dataset-average anatomy', 'wide-angle distortion not in reference', 'lens compression not in reference', 'cropping that removes volume', 'depth flattening', 'mirror selfies', 'reflections', 'beautification filters', 'skin smoothing', 'plastic skin', 'airbrushed texture', 'stylized realism', 'editorial fashion proportions', 'more realistic reinterpretation'"
    ]
  }
}
```

## Paradigm 2: The Dense Narrative Format (Optimized for the Python Pipeline)
When executing API calls via the Python pipeline, condense the logic above into a dense, flat JSON string containing a massive descriptive text block.

```json
{
  "prompt": "string - A dense, ultra-descriptive narrative. Use specific camera math (85mm lens, f/1.8, ISO 200), explicit flaws (visible pores, mild redness, subtle freckles, light acne marks), lighting behavior (direct on-camera flash creating sharp highlights), and direct negative commands (Do not beautify or alter facial features).",
  "negative_prompt": "string - A comma-separated list of explicit realism blockers (no plastic skin, no CGI).",
  "image_input": [
    "array of strings (URLs) - Optional. Input images to transform or use as reference (up to 14). Formatting: URL to jpeg, png, or webp. Max size: 30MB."
  ],
  "api_parameters": {
    "google_search": "boolean - Optional. Use Google Web Search grounding",
    "resolution": "string - Optional. '1K', '2K', or '4K' (default 1K)",
    "output_format": "string - Optional. 'jpg' or 'png' (default jpg)",
    "aspect_ratio": "string - Optional. Overrides CLI aspect_ratio (e.g., '16:9', '4:5', 'auto')"
  },
  "settings": {
    "resolution": "string",
    "style": "string - e.g., 'documentary realism'",
    "lighting": "string - e.g., 'direct on-camera flash'",
    "camera_angle": "string",
    "depth_of_field": "string - e.g., 'shallow depth of field'",
    "quality": "string - e.g., 'high detail, unretouched skin'"
  }
}
```

## Best Practices & Natural Language Hacks

1.  **Camera Mathematics:** Always define exact focal length, aperture, and ISO (e.g., `85mm lens, f/2.0, ISO 200`). This forces the model to mimic optical physics rather than digital rendering.
2.  **Explicit Imperfections:** Words like "realistic" are not enough. Dictate flaws: `mild redness`, `subtle freckles`, `light acne marks`, `unguided grooming`.
3.  **Direct Commands:** Use imperative negative commands *inside* the positive prompt paragraph: `Do not beautify or alter facial features. No makeup styling.`
4.  **Lighting Behavior:** Don't just name the light, name what it does: `direct flash photography, creating sharp highlights on skin and a slightly shadowed background.`
5.  **Non-Human Materials (Products/Nature):** When generating non-humans, replace skin/outfit logic with extreme material physics. Define surface scoring (e.g., "micro-scratches on anodized aluminum"), light scattering (e.g., "subsurface scattering through dew-covered petals"), or graphic layouts (e.g., "flat-lay composition, clean sans-serif typography").
6.  **Mandatory Negative Stack:** You MUST include the extensive negative prompt block (e.g., forbidding "skin smoothing" and "anatomy normalization").
7.  **Avoid Over-Degradation (The Noise Trap):** While simulating camera flaws (like `compression artifacts`) can help realism, pushing extreme `ISO 3200` or `heavy film grain` in complex, contrast-heavy environments (like neon night streets) actually triggers the model's "digital art/illustration" biases. Keep ISO settings below 800 and rely on *physical subject imperfections* (like peach fuzz or asymmetrical pores) rather than heavy camera noise to sell the realism.

## Master Reference Guide
If you require the absolute full schema breakdown, parameter options, or the complex JSON structing for multi-panel grids, refer to the root project document:
`[Master Prompt Reference Guide](file:///c:/Users/nateh/OneDrive/Desktop/Nano%20Banana%202/master_prompt_reference.md)`

## Execution via Google API (Python Workflow)

When executing Nano Banana prompts, bypass the standard `generate_image` tool and use the dedicated Python pipeline which calls Google's Gemini image generation API directly.

**Prerequisites:**
1. `google-genai` and `requests` packages installed (`pip install google-genai requests`).
2. A JSON prompt file matching the **Dense Narrative Format** saved in `/prompts/`.

**Available Models:**
| Alias  | Model ID                           | Description         |
|--------|------------------------------------|---------------------|
| `nb2`  | `gemini-3.1-flash-image-preview`   | Nano Banana 2       |
| `nbpro`| `gemini-3-pro-image-preview`       | Nano Banana Pro     |

**Execution:**
```powershell
python "C:\Users\dicke\.claude\skills\nano-banana-images\scripts\generate_image.py" .\prompts\your_prompt.json .\images\output_image.jpg "4:5"
```

With an explicit model (defaults to `nb2` if omitted):
```powershell
python "C:\Users\dicke\.claude\skills\nano-banana-images\scripts\generate_image.py" .\prompts\your_prompt.json .\images\output_image.jpg "4:5" nbpro
```

**Parameters:**
1. `<prompt_json_file>` — Path to the Dense Narrative JSON prompt (relative to current project)
2. `<output_file>` — Destination path for the saved image (relative to current project)
3. `[aspect_ratio]` — e.g. `1:1`, `16:9`, `9:16`, `4:5` (defaults to `1:1`)
4. `[model]` — `nb2` or `nbpro` or a full model ID (defaults to `nb2`)

## How to use this skill
When a user asks you to generate a highly detailed, realistic, or complex image:
1. Construct a Dense Narrative JSON prompt (Paradigm 2 format) based on the user's request.
2. Save the JSON file to `.\prompts\` in the current project directory (mirror the image category subdirectory).
3. Run the Python pipeline via Bash, using the absolute script path:
   ```powershell
   python "C:\Users\dicke\.claude\skills\nano-banana-images\scripts\generate_image.py" .\prompts\<name>.json .\images\<category>\<name>.jpg "<aspect_ratio>" <model>
   ```
   - Model defaults to `nb2` (Nano Banana 2). Use `nbpro` if the user requests Nano Banana Pro.
   - Aspect ratio defaults to `1:1` if not specified by the user.
4. Save the output image to the correctly categorized subfolder inside `.\images\`. Use `.\images\miscellaneous\` if no category is clear.
5. When processing multiple images simultaneously, run their generation commands in parallel.
