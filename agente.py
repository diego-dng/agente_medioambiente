import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-flash"
    contents = "Evalúa estas coordenadas: 43.569516756567126, -7.286539538796145"
    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        tools=tools,
        system_instruction=SYSTEM_PROMPT,
    )

    print("Conectando con el Agente...")
    
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    print("INFORME AMBIENTAL")
    print("_" * 100)
    print(response.text)

    try:
        with open("respuesta.md", "w", encoding="utf-8") as f_out:
            f_out.write(response.text)
        print("Respuesta guardada en: respuesta.md")
    except Exception as e:
        print(f"Erro al guardar respuesta: {e}")
    
if __name__ == "__main__":
    generate()