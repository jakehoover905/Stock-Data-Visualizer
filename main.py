#Stock Data Visualizer - main application

import os
from datetime import date

import requests
from dotenv import load_dotenv

from chart_generator import generate_chart

Chart_Types = {"1": "bar", "2": "line"}
Time_Series = {"1": "Intraday", "2": "Daily", "3": "Weekly", "4": "Monthly"}

def get_symbol():
    return

def get_menu_choice(prompt, valid):
    return

def get_date(prompt):
    return

def get_end_date(start_date):
    return

def fetch_stock_data(symbol, function, api_key):
    return

def check_api_errors(data):
    return

def main():
    return
