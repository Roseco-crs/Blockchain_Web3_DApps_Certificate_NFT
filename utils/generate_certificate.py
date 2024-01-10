from openai import OpenAI
from dotenv import load_dotenv
import os

def load_openai_client():
    load_dotenv()                                 # load environment from .env
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Get the openai key from .env
    if not openai_api_key:                        # check if API key is available
        raise ValueError("OpenAI API key is not found. Please, set it in .env file")
    client = OpenAI(api_key=openai_api_key)       # Initialize openai client with api key
    return client

def generate_image_caption(client, prompt):
    try:                                     # Make API Key request to generate an image caption
        response = client.images.generate(
            model = "dall-e-3",              
            prompt = str(prompt), 
            size = "1024x1024",
            quality = "standard",                  # quality = "hd"
            n = 1,
        )
        image_url = response.data[0].url
        return image_url
    
    except Exception as e: 
        print(f"API Key error :{e}")
        return None

def main():
    openai_client = load_openai_client()                  # Initialize OpenAI Key
    prompt = "Simple Nice red certificate with white background and with no image or design",  # Your prompt
    image_url = generate_image_caption(openai_client, prompt)     # Generate image url
    if image_url:
        print(f"Successfully Generated Image URL: {image_url}")
    else:
        print("Image URL generation failled")
    

if __name__ == "__main__":
    main()
        
    
    
