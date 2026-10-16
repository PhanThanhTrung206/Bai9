
import tkinter as tk

# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("Bai tap Checkbutton va Radiobutton")
cua_so.geometry("400x500")

# HOAT DONG 1: CHECKBUTTON

tk.Label(
    cua_so,
    text="HOAT DONG 1: CHON SO THICH",
    font=("Arial", 12, "bold")
).pack(pady=10)

tk.Label(
    cua_so,
    text="Chon so thich cua ban:"
).pack(pady=5)

# Bien luu so thich
bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

# Tao cac Checkbutton
tk.Checkbutton(
    cua_so,
    text="Doc sach",
    variable=bien_doc_sach
).pack(anchor="w", padx=50)

tk.Checkbutton(
    cua_so,
    text="The thao",
    variable=bien_the_thao
).pack(anchor="w", padx=50)

tk.Checkbutton(
    cua_so,
    text="Am nhac",
    variable=bien_am_nhac
).pack(anchor="w", padx=50)


def xem_lua_chon():
    print("Doc sach:", bien_doc_sach.get())
    print("The thao:", bien_the_thao.get())
    print("Am nhac:", bien_am_nhac.get())


tk.Button(
    cua_so,
    text="Xem lua chon",
    command=xem_lua_chon
).pack(pady=10)


# HOAT DONG 2: RADIOBUTTON

tk.Label(
    cua_so,
    text="HOAT DONG 2: CHON LOAI TAI KHOAN",
    font=("Arial", 12, "bold")
).pack(pady=10)

# Bien luu loai tai khoan
bien_loai_tai_khoan = tk.StringVar(value="ca_nhan")

tk.Label(
    cua_so,
    text="Chon loai tai khoan:"
).pack(pady=5)

# Tao cac Radiobutton
tk.Radiobutton(
    cua_so,
    text="Ca nhan",
    variable=bien_loai_tai_khoan,
    value="ca_nhan"
).pack(anchor="w", padx=50)

tk.Radiobutton(
    cua_so,
    text="Doanh nghiep",
    variable=bien_loai_tai_khoan,
    value="doanh_nghiep"
).pack(anchor="w", padx=50)

# Noi hien thi ket qua
nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack(pady=5)


def xem_loai_tai_khoan():
    nhan_ket_qua.config(
        text=f"Ban da chon: {bien_loai_tai_khoan.get()}"
    )


tk.Button(
    cua_so,
    text="Xac nhan",
    command=xem_loai_tai_khoan
).pack(pady=10)


# Chay chuong trinh
cua_so.mainloop()
