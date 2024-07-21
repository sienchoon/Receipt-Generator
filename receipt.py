from datetime import datetime, timedelta

# converting time to string
now = datetime.now()
date_formatted = now.strftime("%d-%m-%Y")
date_str = str(date_formatted)
date = date_str[0:10]

#Initial payment date (constant variable)
initial_payment_date = now

# Next Payment date (fortnightly)
next_payment_date = initial_payment_date + timedelta(days=14)
str_formatted_date = next_payment_date.strftime("%d-%m-%Y")
formatted_date = str(str_formatted_date) 
next_date = formatted_date[0:10]

# function to format dates to dd-mm-yyyy
def format_date(date):
    return date.strftime("%Y-%m-%d")

# using the function to convert date to the new format


class ReceiptGenerator:
    @staticmethod
    def generate_receipt(rental):
        receipt = f"Payment Receipt\n"
        receipt += f"----------------------------\n"
        receipt += f"Tenant: {rental.name}\n"
        receipt += f"Payment Amount: ${rental.payment_amount}\n"
        receipt += f"Payment Period: {rental.frequency}\n"
        receipt += f"Payment Dates: {date}\n"
        receipt += f"Next Schedule Payment Date: {next_date}"
        receipt += f"\n"
        receipt += f"Thank you for your payment!\n"
        receipt += f"----------------------------\n"
        
        return receipt