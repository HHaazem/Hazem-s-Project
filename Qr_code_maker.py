import qrcode
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def generate_custom_qr_code_with_draw(data, box_size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")

    # Use Pillow (PIL) to draw on the QR code
    draw = ImageDraw.Draw(qr_code)
    draw.text((10, 10), "Custom Text", fill="red")

    return qr_code

def generate_qr_code_button_click():
    data = data_entry.get()
    if data:
        qr_code = generate_custom_qr_code_with_draw(data)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_code.save(file_path)
            messagebox.showinfo("Success", "QR code saved successfully.")
    else:
        messagebox.showerror("Error", "Please enter data for the QR code.")

# Create the GUI window
window = tk.Tk()
window.title("Custom QR Code Generator")

# Create and configure widgets
data_label = tk.Label(window, text="Data:")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code_button_click)
generate_button.pack()

# Start the GUI event loop
window.mainloop()
