import os
from datetime import datetime
from renter import Rental
from receipt import ReceiptGenerator

#create a rental object from Rental class
renter = Rental('Ms A So', 450, 'Fortnightly')

#generate receipt from ReceiptGenerator class
receipt = ReceiptGenerator.generate_receipt(renter)
print(receipt)


#Create a path to save the receipt
#change relative path to your directory choice
#saving my receipts outside of git folder
relative_path = '../receipts_folder'
path = os.path.abspath(relative_path)
os.makedirs(path, exist_ok=True)

#current time for filename formatting
current_date = datetime.now().strftime("%d-%m-%Y")

file_name = f"receipt_{current_date}"

file_path = os.path.join(path, file_name)
with open(file_path, 'w') as file:
    file.write(receipt)

    
print(f'Receipt successfully saved as {file_path}')
print(f"{path}")
