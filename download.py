import tkinter as tk
import os
from tkinter import filedialog
from pytube import YouTube

# Khởi tạo giao diện
root = tk.Tk()
root.withdraw()

# Hiển thị hộp thoại để chọn đường dẫn lưu file
file_path = filedialog.asksaveasfilename(defaultextension=".mp4")

# Hiển thị hộp thoại để nhập URL video
url = tk.simpledialog.askstring(title="URL", prompt="Nhập URL video:")

# Tải video xuống với định dạng mp4
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download(output_path=file_path)

# Chuyển đổi video sang định dạng mp3
mp4_file = stream.default_filename
mp3_file = mp4_file.replace(".mp4", ".mp3")
command = f"ffmpeg -i \"{file_path}\\{mp4_file}\" \"{file_path}\\{mp3_file}\""
os.system(command)
