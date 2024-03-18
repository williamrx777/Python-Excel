import requests
import streamlit as st

# Set Streamlit theme
st.set_page_config(
    page_title="Departamentos e Funcionários",
    layout="wide",  # Wide layout for better use of space
    initial_sidebar_state="collapsed"  # Collapsed sidebar for wider display
)

# Fetch data from API
departamento = requests.get('http://suporte/api/departamento-lista/')
exibir_departamento = departamento.json()
funcionario = requests.get('http://suporte/api/funcionario-lista/')
exibir_funcionario = funcionario.json()

# Group employees by department
departamento_funcionarios = {}
for dept in exibir_departamento:
    dept_id = dept['id']
    dept_name = dept['nome']
    departamento_funcionarios[dept_name] = []
    for func in exibir_funcionario:
        if func['departamentoId'] == dept_id:
            departamento_funcionarios[dept_name].append(func)

# Display data
st.title("Departamentos e Funcionários")

for dept_name, funcionarios in departamento_funcionarios.items():
    st.header(f"Departamento: {dept_name}")
    if funcionarios:
        st.table(funcionarios)
    else:
        st.write("Não há funcionários neste departamento.")
