import openai
openai.api_key = "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"  # supply your API key however you choose

image_resp = openai.Image.create(prompt="one trendy sunglasses unisex colorful spring", n=4, size="512x512")

print(image_resp)