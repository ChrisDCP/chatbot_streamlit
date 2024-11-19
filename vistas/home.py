import streamlit as  st
import json
import requests #pip install requests
from streamlit_lottie import st_lottie # pip install streamlit-lottie
from PIL import Image
#https://lottiefiles.com/

def get(path:str):
    with open(path, "r") as p:
        return json.load(p)


#Inicio de pagina
with st.container():
    st.subheader("Bienvenidos, Somos SOFTIA👋🏻🥰🦾")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de las tenologías y la innovación, especialización en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos. "
    )
    st.write("[Saber más>]((https://github.com/ChrisDCP))"
    )

#Sobre nosostros
with st.container():
    st.write("---")

    texto_columna, imagen_columna = st.columns((1,2))
    with texto_columna:
        st.subheader("Sobre nosotros🧐❓🤖")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.

Seguramente te vamos a poder ayudar si:

-Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido

para tu negocio

No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos

-Quieres mejorar la experiencia de tus clientes

Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y boligrafo

***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página***

            """
    )
        st.write("[Más sobre nosotros >](https://streamlit.io/)")
        
        with imagen_columna:
            image_path = get("img/acerca_de.png")
            lottie_path= ".Animacion/ani.json"
            try:
                image = Image.open(image_path)
                st.image(image, "imagen cargada correctamente")
                animation = get(lottie_path)
                st_lottie(animation)
            except Exception as e:
                st.error(f"No se puede cargar la imagen: {e}") 

    

#Servicios

with st.container():
    st.write("---")
    st.header("Servicios📱💻🤩")


    texto_columna, imagen_columna = st.columns((1,2))


with texto_columna:
    st.subheader("Diseño de aplicaciones")

    st.write(
        """
        Si en tus procesos diarios tienes que introducir información en diferentes fuentes de datos o bien tienes que 
        trabajar con documentación en papel, es hora de pensar en implementar una aplicación en tu negocio para potenciar y optimizar el funcionamiento de los procesos diarias
        """
    )
    st.write("[Ver servicios >](https://share.streamlit.io/galery)")
    
    with imagen_columna: st.image("img/diseno.png")
    with st.container():
        st.write("---")
        #st.write("##")
        imagen_columna, texto_columna = st.columns((1,2))
        with imagen_columna:
            st.image("img/proceso.jpg")

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
                #st.write("##")
                imagen_columna, texto_columna = st.columns((1,2))
                with imagen_columna:
                    st.image("img/datos.jpg")

            with texto_columna:
                st.subheader("Visualización de datos")
                st.write(
                """
            Si sientes que no tienes una visión clara de datos de tu negocio lo que necesitas es una
aplicación en la que puedas tener toda la información de interes de tu empresa.
                """
                )
                st.write("[Ver servicios >](https://streamlit.io/)")

#contactos
st.subheader("Contacto")

form = st.form(key="home", clear_on_submit=True)

with form:
    input_nombre = st. text_input("Nombre:", placeholder="Escriba su nombre")
    input_email = st. text_input("correo electrónico:", placeholder="Escriba su correo electrónico")
    input_area = st. text_input("Comentario:", placeholder="Comentario:")
    button_submit = form.form_submit_button("Enviar")

# footer
with st.container():
    st.write("---")
    p1, p2,  p3 = st.columns((3))
    with p1:
        st.subheader("Contacto:")
        st.write("***Dirección***: Juigalpa, Chontales-Nicaragua")
        st.write("***Telefon***: +505 0000-0000")
    with p2:
        st.subheader("Servicios")
        st.write("Diseño de Aplicaciones")
        st.write("Automatización de procesos")
        st.write("Visualización de datos")
    with p3:
        st.subheader("Redes Sociales")
        st.markdown("[Yootube](https://www.yourube.com)")
        st.markdown("[Instagram](https://www.instagram.com)")
        st.markdown("[Facebook](https://www.facebook.com)")