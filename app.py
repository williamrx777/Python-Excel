import pandas as pd
import streamlit as st

# Setting page configuration
st.set_page_config(
    page_title="Checklist",
    page_icon="⚠️"
)

# Function to load and display data for each checklist
def display_checklist(title, filename, sheet_name):
    st.title(title)
    data = pd.read_excel(filename, sheet_name=sheet_name)
    st.dataframe(data)

# Displaying different checklists
display_checklist('INVENTARIO PC', 'CHECK LIST.xlsm', 'INVENTÁRIO PC')
display_checklist('VOIP', 'CHECK LIST.xlsm', 'VOIP')
display_checklist('NOVOS PONTOS', 'CHECK LIST.xlsm', 'NOVOS PONTOS')
display_checklist('WHATSAPP', 'CHECK LIST.xlsm', 'WHATSAPP')
display_checklist('CELULARES CLARO', 'CHECK LIST.xlsm', 'CELULARES CLARO')
display_checklist('TONER', 'CHECK LIST.xlsm', 'TONER')
display_checklist("IP's", 'CHECK LIST.xlsm', "IP's")
display_checklist("IP's - 2", 'CHECK LIST.xlsm', "IP's - 2")
display_checklist('Planilha4', 'CHECK LIST.xlsm', 'Planilha4')
display_checklist('IMPRESSORAS', 'CHECK LIST.xlsm', 'IMPRESSORAS')
display_checklist('LICENÇAS OFFICE', 'CHECK LIST.xlsm', 'OFFICE LICENÇAS')
display_checklist('E-MAIL', 'CHECK LIST.xlsm', 'E-MAILS')
display_checklist('CHECKLIST TI', 'CHECK LIST.xlsm', 'CHECKLIST TI')
