import json
import requests  # pip install requests
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
# https://lottiefiles.com/

# Función Lottie abrir un archivo
def get(path: str):
    with open(path, "r") as p:
        return json.load(p)

# Función Lottie desde URL
def get_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Bienvenida
with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA 👋")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tecnologías y la innovación, especializados en el sector de la "
        "digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y "
        "mejorar procesos."
    )
    st.write("[Saber más >](https://streamlit.io/)")

# Sobre nosotros
with st.container():
    st.write("---")
    I_columna, R_columna = st.columns(2)
    with I_columna:
        st.header("Sobre nosotros 🔍")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudándoles a ahorrar tiempo y dinero a
            través de la implantación de nuevas tecnologías como la inteligencia artificial, análisis de datos o
            implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:
            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor
              añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y
              bolígrafo
            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que
            encontrarás al final de la página***
            """
        )
        st.write("[Más sobre nosotros >](https://streamlit.io/)")

    with R_columna:
        path = get("./animacion/ani.json")
        st_lottie(path)  # Lottie desde archivo
        url = get_url("https://lottie.host/8611e424-5454-46ef-acc1-dbe8a675c7ed/GenBO7VdIL.json")
        st_lottie(url)  # Lottie desde URL

# Servicios
with st.container():
    st.write("---")
    st.header("Servicios")

    imagen_columna, texto_columna = st.columns((1, 2))
    with imagen_columna:
        st.image("img/acerca_de.png")
    with texto_columna:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o
            bien tienes que trabajar con documentación en papel, es hora de pensar en implementar una
            aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarios.
            """
        )
        st.write("[Ver servicios > ](https://streamlit.io/)")

    with st.container():
        st.write("---")
        imagen_columna, texto_columna = st.columns((1, 2))
        with imagen_columna:
            st.image("img/diseno.jpg")
        with texto_columna:
            st.subheader("Automatización de procesos")
            st.write(
                """
                Si realizas cualquier tipo de tarea repetitiva como por ejemplo introducir datos en excel u otras
                aplicaciones, gestión de facturas, envío de emails a proveedores etc Lo que quizás necesitas es una
                automatización de tareas para poder liberar recursos de esas actividades y poder emplearlos en otras
                tareas más productivas.
                """
            )
            st.write("[Ver servicios > ](https://streamlit.io/)")

    with st.container():
        st.write("---")
        imagen_columna, texto_columna = st.columns((1, 2))
        with imagen_columna:
            st.image("img/datos.jpg")
        with texto_columna:
            st.subheader("Visualización de datos")
            st.write(
                """
                Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una
                aplicación en la que puedas tener toda la información de interés de tu empresa.
                """
            )
            st.write("[Ver servicios >](https://streamlit.io/)")

# Contactos
with st.container():
    st.write("---")
    c_columna, inf_columna = st.columns((1, 2))
    with c_columna:
        st.subheader("📧 Contactos")
        # Formulario de contacto
        contacto_form = """
        <form action="https://formsubmit.co/manzanaresdionicio@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Escriba su nombre" required>
        <input type="email" name="email" placeholder="nombre@email.com" required>
        <textarea name="message" placeholder="Su mensaje"></textarea>
        <button type="submit">Enviar...</button>
        </form>
        """
        st.markdown(contacto_form, unsafe_allow_html=True)

# Archivo CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}", unsafe_allow_html=True)

local_css("css/style.css")  # Cargar CSS

# Footer
with st.container():
    st.write("---")
    p_1, p_2, p_3 = st.columns((3))
    with p_1:
        st.subheader("Contacto")
        st.write("***Dirección:*** Juigalpa, Chontales, Nicaragua")
        st.write("***Teléfono:*** +(505) 0000-0000")
    with p_2:
        st.subheader("Servicios")
        st.write("Diseño de aplicaciones")
        st.write("Automatización de procesos")
        st.write("Visualización de datos")
    with p_3:
        st.subheader("Redes")
        st.markdown("[YOUTUBE](https://www.youtube.com/)")
        st.markdown("[Facebook](https://www.markdownguide.org/cheat-sheet/)")
        st.markdown("[Instagram](https://www.markdownguide.org/cheat-sheet/)")
