import streamlit as st

home = st.Page(
    page="vistas/home.py",
    title="Inicio",
    default=True,
)

acerca_de_page = st.Page(
    page="vistas/acerca_de.py",
    title="Acerca de",
)

project_1 = st.Page(
    page="vistas/ventas.py",
    title="Ventas",

)

project_2 = st.Page(
    page="vistas/chatbot.py",
    title="Chatbot",

)

pg = st.navigation(
    {
        "informacion":{home, acerca_de_page,},
        "proyectos":{project_1, project_2}
    }

)

pg.run()