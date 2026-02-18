import streamlit as st
import urllib.parse
import random

# Configuración de la página
st.set_page_config(page_title="Fusionador V2", page_icon="🧪")

st.title("🧪 Fusionador de Personajes V2")
st.write("Versión corregida: Ahora soporta mejor los nombres complejos.")

# Entradas
col1, col2 = st.columns(2)
with col1:
    p1 = st.text_input("Personaje 1", "Shrek")
with col2:
    p2 = st.text_input("Personaje 2", "Cristiano Ronaldo")

# Botón
if st.button("¡FUSIONAR AHORA!"):
    if not p1 or not p2:
        st.warning("Escribe ambos nombres.")
    else:
        st.info("Generando fusión... espera unos segundos.")
        
        # 1. Crear el prompt (descripción para la IA)
        prompt = f"Hyperrealistic fusion character combining features of {p1} and {p2}, cinematic lighting, 8k, detailed texture, full body shot"
        
        # 2. LIMPIEZA DE TEXTO (Aquí estaba el fallo antes)
        # Esto convierte "Shrek y Cristiano" en "Shrek%20y%20Cristiano" de forma segura
        prompt_seguro = urllib.parse.quote(prompt)
        
        # 3. Número aleatorio para que la imagen cambie siempre
        semilla = random.randint(0, 999999)
        
        # 4. Crear la URL final
        url_imagen = f"https://image.pollinations.ai/prompt/{prompt_seguro}?width=1024&height=1024&seed={semilla}&nologo=true&model=flux"
        
        # 5. Mostrar resultado
        st.success(f"¡Fusión completada!")
        
        # Mostramos la imagen
        st.image(url_imagen, caption=f"Fusión de {p1} + {p2}")
        
        # ENLACE DE EMERGENCIA
        # Si la imagen sigue sin salir, este enlace te dejará verla en otra pestaña
        st.markdown(f"**¿No ves la imagen?** [Haz clic aquí para abrirla manualmente]({url_imagen})")
