import streamlit as st
import urllib.parse
import random
import time

# Configuración
st.set_page_config(page_title="Fusionador V3 (Lite)", page_icon="⚡")

st.title("⚡ Fusionador V3 (Modo Rápido)")
st.write("Si los servidores están llenos, esta versión intenta colarse más rápido.")

# Entradas
col1, col2 = st.columns(2)
with col1:
    p1 = st.text_input("Personaje 1", "Shrek")
with col2:
    p2 = st.text_input("Personaje 2", "Batman")

# Botón
if st.button("¡FUSIONAR AHORA!"):
    if not p1 or not p2:
        st.warning("Escribe ambos nombres.")
    else:
        st.info("Contactando con el servidor... (Cruzando los dedos 🤞)")
        
        # 1. Prompt SIMPLIFICADO (Menos texto = Menos error)
        # Quitamos palabras como "8k", "cinematic" que a veces bloquean
        prompt = f"fusion of {p1} and {p2}, hybrid character, visual mix"
        
        # 2. Limpieza segura del texto
        prompt_seguro = urllib.parse.quote(prompt)
        
        # 3. Semilla aleatoria
        semilla = random.randint(0, 999999)
        
        # 4. URL MODIFICADA (EL TRUCO ESTÁ AQUÍ)
        # Quitamos 'model=flux' y 'width/height'. Usamos el modelo por defecto que es más estable.
        url_imagen = f"https://image.pollinations.ai/prompt/{prompt_seguro}?seed={semilla}&nologo=true"
        
        # Pequeña pausa para dar tiempo a procesar
        time.sleep(1)
        
        try:
            # Mostramos la imagen
            st.image(url_imagen, caption=f"Fusión: {p1} + {p2}")
            st.success("¡Éxito!")
        except:
            st.error("El servidor sigue ocupado.")

        # Enlace de respaldo por si la imagen no carga en la web
        st.markdown("---")
        st.markdown(f"👇 **Si la imagen de arriba no carga, toca este enlace azul:**")
        st.markdown(f"[>> ABRIR IMAGEN EN PESTAÑA NUEVA <<]({url_imagen})")
