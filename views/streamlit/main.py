import streamlit as st
import requests
import base64

st.title("HR Self Service Tool")

col1, _ = st.beta_columns(2)

with col1:
    document_name = st.selectbox(
        "Select the document you need",
        ["verification_letter"],
        format_func=lambda x: x.replace("_", " ").title(),
    )
    include_salary = st.checkbox(
        "Include my salary",
    )
    include_allowance = False
    if include_salary:
        include_allowance = st.checkbox(
            "Include my non-salary allowance",
        )
    addressee = st.text_input(
        "Who should the document be addressed to?", value="A QUIEN CORRESPONDA"
    )
    gen_document = st.button("Generate download link")

info_dict = {
    "name": "Carlos Andrés Ardila Palomino",
    "id_number": "1020798773",
    "id_city": "Bogotá",
    "start_date": "2021-06-01",
    "position": "Machine Learning Engineer III",
    "salary": None,
    "bonus": None,
    "addressee": addressee,
}


def create_download_link(val, filename):
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'


if gen_document:
    res = requests.post("http://localhost:8000/verification", json={
        "email": "carlos.ardila@factored.ai",
        "addressee": addressee,
        "include_salary": include_salary,
        "include_allowance": include_allowance,
    })
    html = create_download_link(res.json()["file"].encode("latin-1"), "VerificationLetter")
    st.markdown(html, unsafe_allow_html=True)
