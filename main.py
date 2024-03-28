import os
from openai import OpenAI
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
from draw import generate_pdf
from dotenv import load_dotenv

load_dotenv(".env")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

client = OpenAI(
    api_key=OPENAI_KEY,
)

# Oputput template file for the AI
with open("template_math.txt", "r") as file:
    template = file.read()

# Generate response from AI
def generate_response(chapter, topic):
    prompt = "Exti cel mai bun profesor de matematica, analizeaza capitolul si tema data. Creeaza un material din care elevii pot invata folosind aces template:\n"+template
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": "Acesta este capitolul: "
                + chapter
                + " si aceasta este tema: "
                + topic,
            },
        ],
        stream=True,
    )
    res = ""
    for chunk in completion:
        if chunk.choices[0].delta.content != None:
            res+=str(chunk.choices[0].delta.content)
    print(res)
    # exit()
    return res



def main():
    #get all the subject plans from the json 
    with open("subjects_plans/math-old.json", "r") as file:
        math_data = json.load(file)


    #loop through all the chapters and topics and generate the theory    
    for chapter_data in math_data["chapters"]:
        chapter_title = chapter_data["title"]

        #used for logs
        print(f"Chapter: {chapter_title}") 
        
        for topic_data in chapter_data["topics"]:
            topic_number = topic_data["number"]
            topic_content = topic_data["content"]

            #used for logs
            print(f"Topic {topic_number}: {topic_content}\n")
            print("Generating theory...")

            #generate the theory with the AI
            response = generate_response(chapter_title, topic_content)

            #used for logs
            print("Saving to PDF...")
            
            #save the theory to a pdf file
            pdf_filename = f"output/{chapter_title}_Topic{topic_number}_theory.pdf"
            generate_pdf(chapter_title,topic_content,pdf_filename ,str(response))
            print(f"File saved to {pdf_filename}")


if __name__ == "__main__":
    main()
