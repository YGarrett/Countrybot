# 🏛️ CountryBot: Asistente de Investigación Histórica y Geopolítica

---

## 📋 Descripción del Proyecto

**CountryBot** es un agente inteligente diseñado bajo un estricto enfoque académico-estudiantil. Su propósito principal es automatizar la recopilación y síntesis de información geopolítica e histórica de cualquier nación del globo. 

El sistema implementa una arquitectura híbrida que prioriza la consulta dinámica de fuentes validadas en la web a través de **Wikipedia API** y **Tavily Search**, procesando dichos datos mediante el modelo de lenguaje avanzado **Gemini-2.5-Flash** para estructurar un reporte monográfico riguroso, formal e impersonal (en tercera persona).

---

## 📊 Estructura del Reporte Monográfico

Cada consulta realizada por el agente genera de forma mandatoria un documento estructurado bajo los siguientes estándares de entrega universitaria:

1. **Introducción y Contexto Histórico-Cultural:** Sinopsis de la identidad nacional.
2. **Proceso de Independencia y Fundamentos del Estado:** Hitos de la formación de la nación.
3. **Conflictos Internos y Guerras Civiles:** Análisis de los eventos que reconfiguraron su rumbo político.
4. **Inserción en Conflictos Internacionales:** Rol estratégico en las Guerras Mundiales u otros acontecimientos globales.
5. **Análisis Vexilológico (Significado de la Bandera):** Simbología detallada de los elementos gráficos, colores y escudos.
6. **Paradigma Geopolítico Actual:** Desafíos contemporáneos, economía y estado actual en el siglo XXI.

---

## 🛠️ Requisitos e Instalación

Para replicar el entorno de ejecución de este proyecto en un ámbito local, se deben seguir rigurosamente los siguientes pasos:

### 1. Clonar el repositorio

### 2. Configurar el entorno virtual

### 3. Instalación de dependencias (Requirements.txt)

### 4. Configuracion de .env
Por estrictas políticas de seguridad informática, las credenciales y llaves privadas de acceso a las APIs no han sido incluidas en este repositorio público.

Para poder ejecutar el programa con éxito, el evaluador deberá proveer sus propias llaves. Cree un archivo de texto plano con el nombre exactamente igual a .env en la raíz del proyecto y configure sus credenciales bajo el siguiente formato:

GOOGLE_API_KEY="SU_LLAVE_DE_GEMINI_AQUÍ"
TAVILY_API_KEY="SU_LLAVE_DE_TAVILY_AQUÍ"

### 5. Ejecute el sistema.
Profe, le recomiendo usar el cmd en fullscreen, para que pueda leer todo el resultado, no tuve chance de hacer un deploy en web, lo iba a hacer con banderas y todo pero me agarraron las prisas :(

   git clone [https://github.com/TU_USUARIO/TU_REPO.git](https://github.com/TU_USUARIO/TU_REPO.git)
   cd agente-historiador
