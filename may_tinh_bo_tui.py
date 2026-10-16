
import tkinter as tk
from tkinter import messagebox

# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x400")
cua_so.resizable(False, False)

# Bien luu bieu thuc
bieu_thuc = tk.StringVar()

# O hien thi
man_hinh = tk.Entry(
    cua_so,
    textvariable=bieu_thuc,
    font=("Arial", 20),
    justify="right",
    state="readonly"
)
man_hinh.grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=10, sticky="nsew"
)


# Ham xu ly khi bam nut
def bam_nut(ky_tu):
    bieu_thuc.set(bieu_thuc.get() + str(ky_tu))


# Ham xoa man hinh
def xoa():
    bieu_thuc.set("")


# Ham tinh ket qua
def tinh():
    phep_tinh = bieu_thuc.get()

    if phep_tinh == "":
        messagebox.showerror("Loi", "Vui long nhap phep tinh.")
        return

    try:
        # Chi cho phep cac ky tu may tinh co ban
        ky_tu_hop_le = "0123456789+-*/.() "
        if any(k not in ky_tu_hop_le for k in phep_tinh):
            raise ValueError

        ket_qua = eval(phep_tinh, {"__builtins__": {}}, {})
        bieu_thuc.set(str(ket_qua))

    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0.")
    except (ValueError, SyntaxError, TypeError):
        messagebox.showerror("Loi", "Bieu thuc khong hop le.")


# Danh sach cac nut
cac_nut = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Tao cac nut
for ten_nut, hang, cot in cac_nut:
    if ten_nut == "=":
        lenh = tinh
    else:
        lenh = lambda k=ten_nut: bam_nut(k)

    tk.Button(
        cua_so,
        text=ten_nut,
        font=("Arial", 16),
        command=lenh
    ).grid(
        row=hang, column=cot,
        padx=4, pady=4, sticky="nsew"
    )

# Nut xoa
tk.Button(
    cua_so,
    text="x",
    font=("Arial", 16),
    command=xoa
).grid(
    row=5, column=0, columnspan=4,
    padx=4, pady=4, sticky="nsew"
)

# Chinh kich thuoc cac hang va cot
for cot in range(4):
    cua_so.grid_columnconfigure(cot, weight=1)

for hang in range(6):
    cua_so.grid_rowconfigure(hang, weight=1)

cua_so.mainloop()
