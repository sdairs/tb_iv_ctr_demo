import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('CTRs')

st.header('CTR Thresholds')

col1,col2 = st.columns(2)
col1.empty()
col2.empty()
table = st.empty()

def get_ctr_thresh(lt = None, gt = None):
    params = {
        'token': 'p.eyJ1IjogIjc5ZTZiYTQyLTJkMmItNDZjMi1hZjRlLTUxNmNhNTkxYjY3OSIsICJpZCI6ICJhMTlmMjM1Mi02N2RiLTQ1ZTYtYTNjYy01NzQzNjEzYmM0YTcifQ.Fnq_KKu2xGn4VKRPakiVsHSGNbd1KcOhNnaa5iMjRWc'
    }
    if lt:
        params['lt'] = lt
    if gt:
        params['gt'] = gt

    url = f'https://api.tinybird.co/v0/pipes/vehicle_ctr_by_threshold.json'
    response = requests.get(url, params=params)
    return response.json()['data']

lt = col1.number_input('Less than', min_value=0, step=1, value=1)
gt = col2.number_input('Greater than', min_value=0, step=1, value=10)
table.table(get_ctr_thresh(lt=lt,gt=gt))

st.header('All CTRs')

def get_ctr():
    params = {
        'token': 'p.eyJ1IjogIjc5ZTZiYTQyLTJkMmItNDZjMi1hZjRlLTUxNmNhNTkxYjY3OSIsICJpZCI6ICI5ZDEzMzZiYy02MzM3LTRjNjMtYTcxOC1lZmNiNjFjMzBlNGYifQ.t3ueNMqH6d023upJEW7OGm2fdU_HIzOIFF8zJ3mx7eM'
    }

    url = f'https://api.tinybird.co/v0/pipes/vehicle_clicks.json'
    response = requests.get(url, params=params)
    return response.json()['data']

st.table(get_ctr())