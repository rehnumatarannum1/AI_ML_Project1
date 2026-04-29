from google import genai
from dotenv import load_dotenv
import os,io #io->for input-output;os->for operating system
from PIL import Image #import pillow package to convert image type for GEMINI-3 API


#load environment variables
load_dotenv()
API_KEY=os.getenv("GEMINI_API_KEY")

#API_Client->handle request and response (User-><-Server)
client=genai.Client(api_key=API_KEY) 

#note generate
def generate_note(images):

    pil_images=[]
    for i in images:
        img=Image.open(i)
        pil_images.append(img)
        
    prompt="""Summarize the images in Note format at max 100 words, add necessary markdown to differentiate sections"""
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images,prompt]
    )
    return response.text

#quiz generate
def generate_quiz(pictures,level):

    pil_images=[]
    for i in pictures:
        img=Image.open(i)
        pil_images.append(img)
        
    prompt=f"""Generate 5 multiple choice questions based on the {level} difficulty with correct answers below, add necessary markdown one by one"""
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[pil_images,prompt]
    )
    return response.text