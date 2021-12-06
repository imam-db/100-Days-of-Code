"""
Interactive Coding Exercise : Data Types
"""

# simpan inputan ke dalam variable
two_digit_number = input('Type a two digit numbers\n')

# ubah type data dari int ke str
str_two_digit_number = str(two_digit_number)

# dari str bisa kita subscript untuk mendapatkan digit pertama dan digit kedua
str_first_digit = str_two_digit_number[0]
str_second_digit = str_two_digit_number[1]

# dilakukan operasi penjumlahan antara kedua digit tersebut, akan tetapi dilakukan casting(ubah tipe data) terlebih dahulu dari str ke int
print(int(str_first_digit) + int(str_second_digit))