

import requests
from datetime import date, timedelta
from tkinter import Tk, Button, messagebox, Label,Text,Menu
from tkcalendar import DateEntry


def fetch_total_debt():

    text_box.delete("1.0", "end")
    todaybse =date.today() - timedelta(days=7) #i think the api only shows data from 3 days ago
    today = todaybse.strftime("%Y-%m-%d") #format to match api_url requirements
    #print(today)
    api_url = f"https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny?filter=record_date:gt:" + today
    try:
        response = requests.get(api_url)
        if response.status_code == 200:

            data = response.json()["data"]
            message = ""

            for i,  record in enumerate(data):
                if i < len(text_boxes):
                    record_date = record["record_date"]
                    total_debt = float(record["tot_pub_debt_out_amt"])
                    text_boxes[i].delete(1.0,"end")
                    text_boxes[i].insert("1.0",f"{record_date}")
                    debt_boxes[i].delete(1.0,"end")
                    debt_boxes[i].insert("1.0",f"${total_debt:,.2f}")

            #messagebox.showinfo("Debt Data", "Data Pulled from API") #probablyl don't need this
        else:
            messagebox.showerror("error", f"Failed to get data Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("error!",f"error: , {e}")


root = Tk()
root.title("debt app")
root.geometry("650x150")

menubar = Menu(root)
file_menu =Menu(menubar, tearoff=0)
file_menu.add_command(label="Quit", command=lambda: exit())
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

dateLabel = []
for i in range(3):
        label1 = Label(text=f"Date {i + 1}")
        label1.grid(row=i,column=0)
        dateLabel.append(label1)

debtLabel = []
for i in range(3):
        label1 = Label(text="Debt:")
        label1.grid(row=i,column=2)
        debtLabel.append(label1)

text_boxes = []
for i in range(3):
        text_box = Text(root, width=12, height=1)
        text_box.grid(row=i , column=1)
        text_boxes.append(text_box)

get_data_button = Button(root, text="Get Data", command=fetch_total_debt)
get_data_button.grid(column=1,row=3,pady=10)

debt_boxes = []
for i in range(3):
        text_box = Text(root, width=23, height=1)
        text_box.grid(row=i , column=3)
        debt_boxes.append(text_box)

date_label = Label(text="Date Range: ", width=10,height=1)
date_label.grid(row=1,column=4)


#Manual Date Entry
date_boxes = []
for i in range(2):
        date_box = DateEntry(root, width=12, height=1)
        date_box.grid(row=1,column=5+ i)
        date_boxes.append(date_box)





get_data_button = Button(root, text="Get Data", command=fetch_total_debt)
get_data_button.grid(column=1,row=3,pady=10)


 
root.mainloop()
        
 
 
#fetch_total_debt()


#print(today)