import streamlit as st


home = st.Page(
    page="vistas/home.py",
    title="Inicio",
    icon="🏠",  
    default=True,
)

acerca_de_page = st.Page(
    page="vistas/acerca_de.py",
    title="Acerca de",
    icon=":material/account_circle:",
)

project_1_page = st.Page(
    page="vistas/ventas.py",
    title="Ventas",
    icon="📈",  
)

project_2_page = st.Page(
    page="vistas/chatbot.py",
    title="Chat Bot",
    icon="🤖",  
)


pg = st.navigation(
    {
        "Información:": [home, acerca_de_page],
        "Proyectos:": [project_1_page, project_2_page],
    }
)


st.sidebar.markdown("Elaborado con ❤️ por [Streamlit](https://streamlit.io/gallery)")


pg.run()
