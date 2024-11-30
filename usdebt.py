import requests
import tkinter as tkinter
from tkinter import messagebox,simpledialog


def fetch_total_debt():
    api_url = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?filter=record_date:eq:2024-11-27"
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

username = simpledialog.askstring("Input", "Enter your username:")
apikey = simpledialog.askstring("Input", "Enter your API Key:")

print(username + ' ' + apikey)