import os

folder = r"D:\ComfyUI_windows_portable\Images\ComfyUI\output\CommonCovers"

files = sorted([
    f for f in os.listdir(folder)
    if os.path.isfile(os.path.join(folder, f))
])

for i, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"Cover_{i:02d}{ext}"

    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)

    os.rename(src, dst)

print("Done")