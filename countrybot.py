import os
from dotenv import load_dotenv
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities.tavily_search import TavilySearchAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# 1. Cargar llaves y configurar variables de entorno
load_dotenv()

# 2. Inicializar las herramientas
# Wikipedia en español
wiki_api = WikipediaAPIWrapper(lang="es")
# Tavily Search para el contexto actual
tavily_api = TavilySearchAPIWrapper()

# 3. Configurar el LLM (Gemini)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

def investigar_pais(pais: str) -> str:
    print(f"\n[CountryBot]: Consultando fuentes históricas (Wikipedia)...")
    # Intentamos extraer el grueso de la historia de Wikipedia
    try:
        datos_wikipedia = wiki_api.run(f"Historia de {pais}")
    except Exception:
        datos_wikipedia = "No se encontraron registros densos en Wikipedia."

    print(f"[CountryBot]: Consultando panorama geopolítico contemporáneo (Tavily Search)...")
    # Buscamos debates actuales o paradigma del siglo XXI en Tavily
    try:
        datos_tavily = tavily_api.run(f"paradigma actual geopolitica economia {pais} 2026")
    except Exception:
        datos_tavily = "No se pudieron recuperar datos web recientes."


   # 4. Prompt de Sistema Optimizado (Identidad Académica con Respaldo de Conocimiento)
    system_instruction = (
        "Eres 'CountryBot', un Asistente de Investigación Histórica y Geopolítica avanzada "
        "con un enfoque riguroso, formal y de carácter estudiantil-académico. "
        "Tu objetivo es proporcionar reportes monográficos detallados, objetivos y con un lenguaje "
        "técnico pero claro sobre el país solicitado.\n\n"
        "Para construir el reporte, analiza y prioriza el contexto provisto de Wikipedia y Tavily. "
        "CRÍTICO: Si el contexto provisto viene incompleto, carece de detalles sobre alguna sección (como la bandera) "
        "o se encuentra completamente vacío, DEBES utilizar tu propio y amplio conocimiento de fondo "
        "para redactar y completar exhaustivamente cada uno de los puntos requeridos. Bajo ninguna circunstancia "
        "dejes el reporte en blanco o te niegues a responder.\n\n"
        "Bajo ninguna circunstancia utilices lenguaje coloquial. El reporte final SIEMPRE debe seguir "
        "la siguiente estructura formal mediante títulos limpios en Markdown:\n\n"
        "1. **Introducción y Contexto Histórico-Cultural:** Sinopsis de la identidad nacional.\n"
        "2. **Proceso de Independencia y Fundamentos del Estado:** Hitos de la formación de la nación.\n"
        "3. **Conflictos Internos y Guerras Civiles:** Análisis de los eventos que reconfiguraron su rumbo político.\n"
        "4. **Inserción en Conflictos Internacionales:** Rol estratégico en las Guerras Mundiales u otros acontecimientos globales.\n"
        "5. **Análisis Vexilológico (Significado de la Bandera):** Simbología detallada de los elementos gráficos, colores y escudos.\n"
        "6. **Paradigma Geopolítico Actual:** Desafíos contemporáneos, economía y estado actual en el siglo XXI.\n\n"
        "Mantén una redacción impersonal (en tercera persona), formal, fluida y con un estándar apto para una entrega universitaria."
    )
    

    # Combinamos el conocimiento obtenido por las herramientas
    contexto_herramientas = (
        f"CONTEXTO DE WIKIPEDIA:\n{datos_wikipedia}\n\n"
        f"CONTEXTO DE TAVILY SEARCH (RECIENTE):\n{datos_tavily}"
    )

    prompt_usuario = (
        f"Genera el reporte monográfico para el siguiente país: {pais}.\n"
        f"Utiliza los siguientes datos extraídos de las herramientas para construirlo:\n\n{contexto_herramientas}"
    )

    # Mandamos los mensajes estructurados a Gemini
    mensajes = [
        SystemMessage(content=system_instruction),
        HumanMessage(content=prompt_usuario)
    ]

    respuesta = llm.invoke(mensajes)
    return respuesta.content

# 5. Ejecución en Terminal
if __name__ == "__main__":
    pais_usuario = input("Introduzca el nombre del país que desea investigar: ")
    print(f"\n[CountryBot]: Iniciando investigación académica sobre {pais_usuario}. Por favor, espere...")
    
    try:
        reporte_final = investigar_pais(pais_usuario)
        print("\n======================================================================")
        print(f"       REPORTE MONOGRÁFICO DE INVESTIGACIÓN: {pais_usuario.upper()}          ")
        print("======================================================================\n")
        print(reporte_final)
        
    except Exception as e:
        print(f"Se ha producido un error durante la investigación académica: {e}")