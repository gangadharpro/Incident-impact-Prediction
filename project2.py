import pandas as pd
import numpy as np
import streamlit as st
import pickle as p
import requests

p_in = open("model_ent.pkl", "rb")
model = p.load(p_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(number, resolved_by, assigned_to, assignment_group, 
		 priority, urgency, u_symptom, subcategory, category, sys_updated_by, location, 
		 closed_at, sys_mod_count, opened_by, resolved_at):
    """Let's Authenticate the Impact of Incidents
    This is using docstrings for specifications.
    ---
    parameters:
      - name: number
        in: query
        type: number
        required: true
      - name: resolved_by
        in: query
        type: number
        required: true
      - name: assigned_to
        in: query
        type: number
        required: true
      - name: assignment_group
        in: query
        type: number
        required: true
      - name: priority
        in: query
        type: number
        required: true
      - name: urgency
        in: query
        type: number
        required: true
      - name: u_symptom
        in: query
        type: number
        required: true
      - name: subcategory
        in: query
        type: number
        required: true
      - name: category
        in: query
        type: number
        required: true
      - name: sys_updated_by
        in: query
        type: number
        required: true
      - name: location
        in: query
        type: number
        required: true
      - name: closed_at
        in: query
        type: number
        required: true
      - name: sys_mod_count
        in: query
        type: number
        required: true
      - name: opened_by
        in: query
        type: number
        required: true
      - name: resolved_at
        in: query
        type: number
        required: true
    responses:
        200:
            descriptions: The output values
    """

    prediction = model.predict([[number, resolved_by, assigned_to, assignment_group, 
		 priority, urgency, u_symptom, subcategory, category, sys_updated_by, location, 
		 closed_at, sys_mod_count, opened_by, resolved_at]])
    print(prediction)
    return prediction




def main():
    st.title("Impact of Incidents")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center">Streamlit Incidents Impact ML App </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    number = st.sidebar.text_input('Number', )
    resolved_by = st.sidebar.text_input('Resolved_by', )
    assigned_to = st.sidebar.text_input('Assigned_to', )
    assignment_group = st.sidebar.text_input('Assignment_group',)
    priority = st.sidebar.text_input('Priority', )
    urgency = st.sidebar.text_input('Urgency', )
    u_symptom = st.sidebar.text_input('U_symptom', )
    subcategory = st.sidebar.text_input('Subcategory',)
    category = st.sidebar.text_input('Category', )
    sys_updated_by = st.sidebar.text_input('Sys_updated_by', )
    location = st.sidebar.text_input('Location', )
    closed_at = st.sidebar.text_input('Closed_at', )
    sys_mod_count = st.sidebar.text_input('Sys_mod_count', )
    opened_by = st.sidebar.text_input('opened_by', )
    resolved_at = st.sidebar.text_input('Resolved_at', )
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(number, resolved_by, assigned_to, assignment_group, 
		 priority, urgency, u_symptom, subcategory, category, sys_updated_by, location, 
		 closed_at, sys_mod_count, opened_by, resolved_at)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()