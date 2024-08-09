import customtkinter
import qrcode

def createQR():
    text = entry.get()
    img = qrcode.make(text)
    img.save("qrcode.png")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("someshiet")

title = customtkinter.CTkLabel(app, text="QRcode generator", font=("Roboto", 44))
title.pack(padx=10, pady=10)

entry = customtkinter.CTkEntry(app, width=350, height=40, placeholder_text="Text/URL")
entry.pack(padx=10, pady=10)

create = customtkinter.CTkButton(app, text="Create", command=createQR)
create.pack(padx=10, pady=10)

app.mainloop()

