# import barcode 
# from barcode.writer import ImageWriter

# number = input("Enter the code to generate barcode: ")

# barcode_format = barcode.get_barcode_class("upc")

# my_barcode = barcode_format(number, writer= ImageWriter())

# my_barcode.save("generated Barcode")

# import barcode
# from barcode.writer import ImageWriter
# number = input("Enter the code to generate barcode: ")
# EAN = barcode.get_barcode_class('upc')
# code_number= EAN(number, writer=ImageWriter())
# fullname = code_number.save('Mybarcode')

from barcode import EAN13
  
# Make sure to pass the number as string
number = input("Enter number to generate barcode(13): ")
  
# Now, let's create an object of EAN13
# class and pass the number
my_code = EAN13(number)
  
# Our barcode is ready. Let's save it.
my_code.save("new_code")