from PIL import Image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from io import BytesIO
import os
import base64

# Load .env from a custom location
load_dotenv(dotenv_path="/Users/andik/Downloads/.env")

def encode_image(image_path):
    """Encodes an image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def encode_pil_image(pil_image):
    """Encodes a PIL image to base64."""
    im_file = BytesIO()
    pil_image.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64.decode("utf-8")

def generate_pil_image_caption(model, pil_image, prompt="What is in this image?"):
    try:
        base64_image = encode_pil_image(pil_image)
        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
            ]
        )
        response = model.invoke([message])
        return response.content
    except Exception as e:
        print(f"Error generating caption: {e}")
        return None

def generate_answer_to_prompt(model, prompt):
    try:
        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
            ]
        )
        response = model.invoke([message])
        return response.content
    except Exception as e:
        print(f"Error generating caption: {e}")
        return None

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")

llm_model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.0,
    max_tokens=None,
    timeout=None,
    max_retries=1,
    google_api_key=api_key,
)

"""
from google.colab import drive
drive.mount('/content/drive')
import os
os.listdir('/content/drive/MyDrive/content')
"""

import os

# List the categories in your local content folder
content_path = os.path.join(os.path.dirname(__file__), "content")
if os.path.exists(content_path):
    print("Categories in content folder:", os.listdir(content_path))
else:
    print("Content folder not found:", content_path)

#from google.colab import drive
#drive.mount('https://drive.google.com/drive/folders/15PpjM4NFRuCRSrnXWhvZwSm9spVBoTLm')
#import os
#os.listdir('/content/drive/MyDrive')

#https://drive.google.com/drive/folders/15PpjM4NFRuCRSrnXWhvZwSm9spVBoTLm

#pictures = os.listdir('/content/drive/MyDrive/content/fire/sample_0')
#print(pictures)
import os
#from skimage import io
#import cv2 as cv
from PIL import Image
from google.colab.patches import cv2_imshow

# Convert FIRE samples
#IMAGE_TYPE = 'fire'
#IMAGE_TYPE = 'smoke'
#IMAGE_TYPE = 'default'
IMAGE_TYPE = '' # To not run sth by mistake

the_path = '/content/drive/MyDrive/content/' + IMAGE_TYPE + '/'
samples = os.listdir(the_path)
samples.sort()
total_samples = len(samples)
print(samples)

ii = 0
for sample in samples:
  sample_path = the_path + '/' + sample
  imgs = os.listdir(sample_path)
  imgs.sort()
  print(sample, imgs)

  img0_path = sample_path + '/' + imgs[0]
  img1_path = sample_path + '/' + imgs[1]
  img2_path = sample_path + '/' + imgs[2]
  img3_path = sample_path + '/' + imgs[3]
  img4_path = sample_path + '/' + imgs[4]

  img0 = Image.open(img0_path)
  img1 = Image.open(img1_path)
  img2 = Image.open(img2_path)
  img3 = Image.open(img3_path)
  img4 = Image.open(img4_path)

  #final_frame = cv.hconcat((img0, img1, img2, img3, img4))
  #cv2_imshow(final_frame)
  #cv2_imshow(new_img)

  width, height = img0.size

  total_width = 5*width

  new_img = Image.new('RGB', (total_width, height))
  new_img.paste(img0, (0*width,0))
  new_img.paste(img1, (1*width,0))
  new_img.paste(img2, (2*width,0))
  new_img.paste(img3, (3*width,0))
  new_img.paste(img4, (4*width,0))

  total_width = int(total_width/2)
  height = int(height/2)
  new_img = new_img.resize((total_width, height))

  #display(new_img)

  if ii/total_samples < 0.75:
    new_img.save('/content/drive/MyDrive/content/attached_imgs_dataset/train/'+IMAGE_TYPE+'/sample_'+str(ii)+'.jpg',quality=20)   #image.save(b.image.path,,optimize=True)
  else:
    new_img.save('/content/drive/MyDrive/content/attached_imgs_dataset/test/'+IMAGE_TYPE+'/sample_'+str(ii)+'.jpg',quality=20)
    print('here')

  ii = ii + 1


from datasets import load_dataset

#dataset = load_dataset("imagefolder", data_dir="/content/drive/MyDrive/content/attached_imgs_dataset")
train_ds, test_ds = load_dataset("imagefolder", data_dir="/content/drive/MyDrive/content/attached_imgs_dataset/", split=['train', 'test'])


#for ii in [15,24]:#range(0, len(train_ds)):
for ii in range(0, len(train_ds)):
  curr_img = train_ds[ii]['image']
  curr_lbl = train_ds[ii]['label']
  #display(curr_img)
  width, height = curr_img.size
  new_width = int(width/5)
  #print(width, height)

  img_0 = Image.new('RGB', (new_width, height))
  img_1 = Image.new('RGB', (new_width, height))
  img_2 = Image.new('RGB', (new_width, height))
  img_3 = Image.new('RGB', (new_width, height))
  img_4 = Image.new('RGB', (new_width, height))

  img_0.paste(curr_img.crop((0*new_width, 0, new_width, height)), (0,0))
  img_1.paste(curr_img.crop((1*new_width, 0, 2*new_width, height)), (0,0))
  img_2.paste(curr_img.crop((2*new_width, 0, 3*new_width, height)), (0,0))
  img_3.paste(curr_img.crop((3*new_width, 0, 4*new_width, height)), (0,0))
  img_4.paste(curr_img.crop((4*new_width, 0, 5*new_width, height)), (0,0))

  #caption = generate_pil_image_caption(llm_model, img_0,"What is in this image that is a fire emergency?")
  #print(curr_lbl, caption)
  #diff1 = generate_pil_image_diff_caption(llm_model, img_0, img_1, "What changes from the first image to the second that is a fire emergency?")
  #diff2 = generate_pil_image_diff_caption(llm_model, img_1, img_2, "What changes from the second image to the second that is a fire emergency?")
  #diff3 = generate_pil_image_diff_caption(llm_model, img_2, img_3, "What changes from the first image to the second that is a fire emergency?")
  #diff4 = generate_pil_image_diff_caption(llm_model, img_3, img_4, "What changes from the first image to the second that is a fire emergency?")
  #print(diff1, diff2, diff3, diff4)
  #prolog_input = caption + ' ' + diff1 + ' ' + diff2 + ' ' + diff3 + ' ' + diff4
  #prolog_output = generate_prolog_code(llm_model, prolog_input, prompt="Generate a prolog program without comments based on the prompt that queries at the end whether there is a fire emergency.")



  #prolog_output = generate_pil_sequence_diffs(llm_model, img_0, img_1, img_2, img_3, img_4, "Relevant to a fire emergengy, describe the first image, then describe the differences between the first and the second image, then the differences between the second and the third image, then the differences between the third and the fourth image, then the differences between the fourth and the fifth image. Generate a prolog program without comments based on the descriptions that queries at the end whether there is a fire emergency in the image sequence. Return only one yes or no.")
  prolog_output = generate_pil_sequence_diffs(llm_model, img_0, img_1, img_2, img_3, img_4, "Relevant to a fire emergengy, describe what is going on. Then, based on the description, generate a prolog program without comments that queries whether there is a fire emergency in the image sequence. Return only one yes or no.")


  prolog_result = generate_prolog_code(llm_model, prolog_output, prompt="Run this prolog code and show me the result concisely without any reasoning, just yes or no.")
  #print(curr_lbl, '--------------------------------')
  #print(prolog_output)
  #print(prolog_result)
  print(ii, curr_lbl, prolog_result)
  print('================================')
  time.sleep(30)

for ii in [15,24]:#range(0, len(train_ds)):
#for ii in range(0, len(train_ds)):
  curr_img = train_ds[ii]['image']
  curr_lbl = train_ds[ii]['label']
  display(curr_img)
  width, height = curr_img.size
  new_width = int(width/5)
  #print(width, height)

  img_0 = Image.new('RGB', (new_width, height))
  img_1 = Image.new('RGB', (new_width, height))
  img_2 = Image.new('RGB', (new_width, height))
  img_3 = Image.new('RGB', (new_width, height))
  img_4 = Image.new('RGB', (new_width, height))

  img_0.paste(curr_img.crop((0*new_width, 0, new_width, height)), (0,0))
  img_1.paste(curr_img.crop((1*new_width, 0, 2*new_width, height)), (0,0))
  img_2.paste(curr_img.crop((2*new_width, 0, 3*new_width, height)), (0,0))
  img_3.paste(curr_img.crop((3*new_width, 0, 4*new_width, height)), (0,0))
  img_4.paste(curr_img.crop((4*new_width, 0, 5*new_width, height)), (0,0))

  caption = generate_pil_sequence_caption(llm_model, img_0, img_1, img_2, img_3, img_4, "Is there a fire emergency in this image sequence? Answer concisely without any reasoning, just yes or no. Aftter that, give a reasoning for the answer.")
  #print(curr_lbl, caption)

  print(ii, curr_lbl, caption)
  print('================================')
  time.sleep(1)

answer = generate_answer_to_prompt(llm_model, "What prompt to use for you to detect fire in consecutive images?")
print(answer)

import dspy

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY","xxx")

llm_model = ChatGoogleGenerativeAI(
    model= "gemini-2.0-flash",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=api_key,
)
dspy.configure(lm=llm_model)


instructions = "Is there an ongoing fire emergency?"
signature = dspy.Signature("claim -> titles: list[str]", instructions)
react = dspy.ReAct(signature, tools=[search_wikipedia, lookup_wikipedia], max_iters=20)

# Create a huggingface dataset

qa_pair = dspy.Example(question="What is in this image that is a burning fire emergency?", answer="This is an answer.")


