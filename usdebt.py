

import requests
from datetime import date, timedelta
from tkinter import Tk, Button, messagebox, Label,Text


def fetch_total_debt():

    text_box.delete("1.0", "end")
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
            
            for i,  record in enumerate(data):
                if i < len(text_boxes):
                    record_date = record["record_date"]
                    total_debt = float(record["tot_pub_debt_out_amt"])
                    text_boxes[i].delete(1.0,"end")
                    text_boxes[i].insert("1.0",f"Date: {record_date}\nTotal Debt: ${total_debt:,.2f}")



                
            #messagebox.showinfo("Debt Data", "Data Pulled from API") #probablyl don't need this
        else:
            messagebox.showerror("error", f"Failed to get data Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("error!",f"error: , {e}")
        
 
root = Tk()
root.title("debt app")
root.geometry("600x150")

text_boxes = []
for i in range(3):
        text_box = Text(root, width=40, height=2)
        text_box.grid(row=i, column=0)
        text_boxes.append(text_box)

get_data_button = Button(root, text="Get Data", command=fetch_total_debt)
get_data_button.grid(column=1,row=3,pady=10)
 
root.mainloop()
        
 
 
#fetch_total_debt()


#print(today)