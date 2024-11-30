import requests
import tkinter as tkinter
from datetime import date, timedelta
from tkinter import messagebox,simpledialog


def fetch_total_debt():

    todaybse =date.today() - timedelta(days=3) #i think the api only shows data from 3 days ago
    today = todaybse.strftime("%Y-%m-%d") #format to match api_url requirements
    #print(today)
    api_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?filter=record_date:eq:" + today
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            total_debt = float(data["data"][0]["tot_pub_debt_out_amt"])
            total_debt = f"{total_debt:,.2f}"
            messagebox.showinfo("Total Debt",f"Total Debt:, ${total_debt}")
        else:
            messagebox.showerror("error", f"Failed to get data Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror(f"error: , {e}")
        
        
        
 
 
fetch_total_debt()


#print(today)