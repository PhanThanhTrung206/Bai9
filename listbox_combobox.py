import tkinter as tk
from tkinter import ttk

# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("Vi du Listbox va Combobox")
cua_so.geometry("350x430")

# ==============================
# BAI TAP 3.1 - LISTBOX
# ==============================

tk.Label(
    cua_so,
    text="Bai tap 3.1 - Listbox",
    font=("Arial", 12, "bold")
).pack(pady=(12, 5))

tk.Label(cua_so, text="Chon mon hoc:").pack(pady=3)

listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=5, width=25)

for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)

listbox_mon_hoc.pack(pady=5)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        mon = listbox_mon_hoc.get(lua_chon[0])
        nhan_listbox.config(text=f"Ban da chon mon: {mon}")
    else:
        nhan_listbox.config(text="Ban chua chon mon hoc!")


tk.Button(
    cua_so,
    text="Xem mon da chon",
    command=xem_mon_da_chon
).pack(pady=4)

nhan_listbox = tk.Label(cua_so, text="")
nhan_listbox.pack(pady=3)

# ==============================
# BAI TAP 3.2 - COMBOBOX
# ==============================

tk.Label(
    cua_so,
    text="Bai tap 3.2 - Combobox",
    font=("Arial", 12, "bold")
).pack(pady=(18, 5))

tk.Label(cua_so, text="Chon lop hoc:").pack(pady=3)

combobox_lop = ttk.Combobox(
    cua_so,
    values=["CNTT1", "CNTT2", "CNTT3", "CNTT4"],
    state="readonly",
    width=22
)
combobox_lop.current(0)
combobox_lop.pack(pady=5)


def xem_lop_da_chon():
    nhan_combobox.config(text=f"Ban da chon lop: {combobox_lop.get()}")


tk.Button(
    cua_so,
    text="Xac nhan lop",
    command=xem_lop_da_chon
).pack(pady=4)

nhan_combobox = tk.Label(cua_so, text="")
nhan_combobox.pack(pady=3)

# Chay chuong trinh
cua_so.mainloop()