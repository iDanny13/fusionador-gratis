import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import io

# Configuración
st.set_page_config(page_title="Fusionador PRO", page_icon="🧬")

st.title("🧬 Fusionador PRO (Hugging Face)")
st.write("Usando el modelo Stable Diffusion XL (Gratis)")

# Verificar el Token
if "HF_TOKEN" not in st.secrets:
    st.error("⚠️ FALTA EL TOKEN. Configúralo en los 'Secrets' de Streamlit.")
    st.stop()

# Conexión con la IA
client = InferenceClient(token=st.secrets["HF_TOKEN"])

# Entradas
col1, col2 = st.columns(2)
with col1:
    p1 = st.text_input("Personaje 1", "Iron Man")
with col2:
    p2 = st.text_input("Personaje 2", "Pikachu")

# Botón
if st.button("¡FUSIONAR AHORA!"):
    if not p1 or not p2:
        st.warning("Escribe los dos nombres.")
    else:
        try:
            with st.spinner('🎨 La IA está pintando... (tarda unos 10-15 seg)'):
                
                # Creamos el prompt en inglés automáticamente
                prompt = f"Hybrid fusion character of {p1} and {p2}, full body, cinematic lighting, 8k, highly detailed, fantasy style, masterpiece."
                
                # Pedimos la imagen al modelo 'stabilityai/stable-diffusion-xl-base-1.0'
                # Este es uno de los mejores modelos gratuitos del mundo
                image = client.text_to_image(
                    prompt, 
                    model="stabilityai/stable-diffusion-xl-base-1.0"
                )
                
                # Mostrar resultado
                st.success("¡Imagen generada!")
                st.image(image, caption=f"Fusión: {p1} + {p2}")
                
        except Exception as e:
            st.error(f"Hubo un error: {e}")
            st.info("Si dice 'Rate limit', espera 2 minutos y prueba otra vez.")
