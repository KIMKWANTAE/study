import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile

def extract_file(zip_file, password):
    try:
        zip_file.extractall(pwd=bytes(password, 'utf-8'))
        return True
    except:
        return False

def brute_force(zip_file):
    for i in range(1000000):  # 000000부터 999999까지
        password = f"{i:06d}"
        if extract_file(zip_file, password):
            return password
    return None

def show_result(password):
    result_window = tk.Tk()
    result_window.title("Password Result")
    result_window.geometry("400x200")  # 창 크기를 400x200으로 설정
    result_text = f"Password Found: {password}" if password else "Password not found."
    tk.Label(result_window, text=result_text, padx=20, pady=20).pack()
    result_window.mainloop()

def select_zip_file():
    root = tk.Tk()
    root.withdraw()  # 메인 윈도우 숨기기
    file_path = filedialog.askopenfilename(title="Select ZIP File", filetypes=[("Zip files", "*.zip")])
    if file_path:
        zip_file = zipfile.ZipFile(file_path)
        password = brute_force(zip_file)
        show_result(password)
    else:
        messagebox.showinfo("Information", "No file selected.")

select_zip_file()
