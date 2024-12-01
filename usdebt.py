

import requests
from datetime import date, timedelta
from tkinter import Tk, Button, messagebox


def fetch_total_debt():

    todaybse =date.today() - timedelta(days=7) #i think the api only shows data from 3 days ago
    today = todaybse.strftime("%Y-%m-%d") #format to match api_url requirements
    #print(today)
    api_url = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?filter=record_date:gt:" + today
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            #data = response.json()
            #total_debt = float(data["data"][0]["tot_pub_debt_out_amt"])
            #debt_date = data["data"][0]["record_date"]
            #total_debt = f"{total_debt:,.2f}"
            
            data = response.json()["data"]
            message = ""
            
            for record in data:
                record_date = record["record_date"]
                total_debt = float(record["tot_pub_debt_out_amt"])
                message += f"Date : {record_date}, \nTotal Debt: ${total_debt:,.2f}\n\n"
                
            messagebox.showinfo("Debt Data", message)
        else:
            messagebox.showerror("error", f"Failed to get data Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("error!",f"error: , {e}")
        
 
root = Tk()
root.title("debt app")
root.geometry("400x400")
 
get_data_button = Button(root, text="Get Data", command=fetch_total_debt)
get_data_button.pack(side="bottom", pady=20)
 
root.mainloop()
        
 
 
#fetch_total_debt()


#print(today)