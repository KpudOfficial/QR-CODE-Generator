import qrcode
import sys

def get_data():
    data = input("Enter the text or URL for your QR code: ")
    filename = input("Enter a name for the file (e.g., mycode): ")
    return data, filename

# 2. Generate the QR code
def generate_qr_code(data):
    print(f"Generating QR code for: {data}...")
    img = qrcode.make(data)
    print("Completed")
    return img

# 3. Save the image
# We add .png automatically so you don't have to type it
def save_qr_code(img,filename):
    img.save(f"/storage/emulated/0/QR_CODES/{filename}.png")
    print(f"Success! Saved as {filename}.png")


def qr_code_data(choice,data):
    qr_code = ''
    if choice == 1:
        qr_code = f"https://wa.me/{data}"
    elif choice == 2:
        qr_code = f"https://x.com/{data}"
    elif choice == 3:
        qr_code = f"{data}"
    else:
        print("Invalid option.")
        return
    return qr_code

menu = {1:"whatsapp",2:"x",3:"Other"}
# 1. Ask the user for input


#if __name__ == main():
print("_______QR CODE SYSTEM_______\n\nQR CODE MENU\nChoose a number correspondong to QR code to be generated\n\n")

for key,value in menu.items():
    print(f"{key}. {value.title()}")

valid_choice = True
while valid_choice:
    choice = int(input("Choice: "))
    if choice not in menu:
        print("Invalid option")
    else:
        valid_choice = False
        
data = get_data()
filename = data[1]
qr_code_dat = qr_code_data(choice,data[0])
gen_qr_code = generate_qr_code(qr_code_dat)
save_code = save_qr_code(gen_qr_code,filename)