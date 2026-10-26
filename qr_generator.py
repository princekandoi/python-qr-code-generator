import qrcode

url = input("Enter the url :")
filename= input("Enter the file name you want to save :")
if not (filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)

print(f"QR code saved successfully as {filename}")