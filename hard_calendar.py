import tkinter as tk
from tkinter import messagebox
import calendar


def show_month_calendar(year, month):n
    top = tk.Toplevel(root)  
    top.title(f"📅 {calendar.month_name[month]} {year}")
    top.geometry("300x300")

    cal_text = calendar.month(year, month)
    text_box = tk.Text(top, height=12, width=30, font=("Courier", 10))
    text_box.pack(pady=10)
    text_box.insert(tk.END, cal_text)
    text_box.config(state="disabled") 


def show_year_calendar():
    try:
        year = int(year_entry.get())
        if year < 1:
            messagebox.showerror("خطا", "سال معتبر نیست!")
            return

        year_window = tk.Toplevel(root)
        year_window.title(f"📘 تقویم سال {year}")
        year_window.geometry("500x500")

        tk.Label(year_window, text=f"📆 سال {year}", font=("B Nazanin", 16, "bold")).pack(pady=10)

        frame = tk.Frame(year_window)
        frame.pack()

        for i in range(1, 13):
            btn = tk.Button(
                frame,
                text=calendar.month_name[i],
                width=15,
                height=2,
                command=lambda m=i: show_month_calendar(year, m),
                bg="#2196F3",
                fg="white"
            )
            btn.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

    except ValueError:
        messagebox.showerror("خطا", "لطفاً سال را به‌صورت عدد وارد کنید.")

root = tk.Tk()
root.title("📅 تقویم پایتونی حرفه‌ای")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="نمایش تقویم کامل سال", font=("B Nazanin", 18, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="سال:").grid(row=0, column=0, padx=5)
year_entry = tk.Entry(frame, width=10)
year_entry.grid(row=0, column=1, padx=5)

btn = tk.Button(root, text="نمایش تقویم سال", command=show_year_calendar, bg="#4CAF50", fg="white", font=("B Nazanin", 12))
btn.pack(pady=15)

root.mainloop()
