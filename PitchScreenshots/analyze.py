import sys
import os

dir_path = "/Users/skytek/Documents/Whipty-Do/PitchScreenshots"
html_out = "<html><body style='display:flex; flex-wrap:wrap; gap:10px;'>"
for file in sorted(os.listdir(dir_path)):
    if file.endswith(".PNG"):
        html_out += f"<div style='border:1px solid #ccc; padding:5px;'><img src='file://{dir_path}/{file}' width='200'/><p style='text-align:center;'>{file}</p></div>"
html_out += "</body></html>"

with open("index.html", "w") as f:
    f.write(html_out)
