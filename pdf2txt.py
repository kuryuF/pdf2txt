import tkinter as tk
from tkinter import filedialog
import os
import re
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="PDFファイルを選択してください")

if not file_path:
    print("ファイルが選択されませんでした。")
    exit()

desktop_path = filedialog.askdirectory(title="保存先ディレクトリを選択してください")

if not desktop_path:
    print("保存先ディレクトリが選択されませんでした。")
    exit()

output_file_name = input("出力ファイルの名前を入力してください（例: output.txt）: ")
output_file_path = os.path.join(desktop_path, output_file_name)

input_file = open(file_path, 'rb')
output_file = open(output_file_path, 'w')

laparams = LAParams(line_overlap=0.5)
resource_manager = PDFResourceManager()
device = TextConverter(resource_manager, output_file, laparams=laparams)
interpreter = PDFPageInterpreter(resource_manager, device)

for page in PDFPage.get_pages(input_file):
    interpreter.process_page(page)

input_file.close()
output_file.close()

with open(output_file_path, 'r') as output_file:
    text = output_file.read()
    cleaned_text = re.sub(r'\n+', '\n', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

with open(output_file_path, 'w') as output_file:
    output_file.write(cleaned_text)

print("テキストを整形して保存しました。")
