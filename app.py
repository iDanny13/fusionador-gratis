import streamlit as st
import random

# Configuración básica de la página
st.set_page_config(page_title="Fusionador Infinito GRATIS", page_icon="♾️")

st.title("🧬 Fusionador Infinito (Gratis)")
st.write("Mezcla dos personajes sin pagar ni un centavo.")

# Entradas de texto
col1, col2 = st.columns(2)
with col1:
    p1 = st.text_input("Personaje 1 (ej. Batman)", "")
with col2:
    p2 = st.text_input("Personaje 2 (ej. Elsa Frozen)", "")

# Botón para fusionar
if st.button("¡FUSIONAR AHORA!"):
    if not p1 or not p2:
        st.warning("Escribe los dos personajes primero.")
    else:
        # Generamos un número aleatorio para que la imagen cambie siempre
        seed = random.randint(0, 100000)
        
        # Creamos el prompt (la instrucción para la IA)
        # Pedimos "fusion", "hybrid", "cinematic lighting" para que se vea bien
        prompt = f"Full body shot, hyperrealistic fusion hybrid of {p1} and {p2}, combining features of both, cinematic lighting, 8k, detailed texture"
        
        # Truco: Usamos Pollinations.ai que genera imágenes gratis via URL
        # Convertimos los espacios en %20 para que funcione el enlace
        prompt_url = prompt.replace(" ", "%20")
        
        # Construimos la dirección de la imagen
        url_imagen = f"https://image.pollinations.ai/prompt/{prompt_url}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"

        st.success(f"Fusión: {p1} + {p2}")
        
        # Mostramos la imagen directamente desde esa URL
        st.image(url_imagen, caption="Imagen generada gratuitamente por Pollinations AI")
        st.caption("Si sale borroso o tarda, dale al botón otra vez.")
