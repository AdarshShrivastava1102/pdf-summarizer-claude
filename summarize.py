import sys
import anthropic
from pypdf import PdfReader
from dotenv import load_dotenv

#load the API key from the .env file
load_dotenv()


#Get filename from command line
if len(sys.argv) < 2:
    print("Usage: python summarize.py mckinsey_auto_report.pdf")
    sys.exit(1) 

filename = sys.argv[1]

#Extract text from PDF
reader = PdfReader(filename)
text = ""
for page in reader.pages:
    text += page.extract_text()

#Send to Claude for summarization
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=300,
    system="You are an expert summarizer.",
    messages=[
        {
            "role": "user",
            "content": f"Summarize this document in exactly 5 bullet points:\n\n{text}"
        }
    ]
)

#Print the summary
print("\n === Summary === \n")
print(response.content[0].text)