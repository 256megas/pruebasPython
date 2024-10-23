# Read Only ('r’): This mode opens the text files for reading only. The start of the file is where the handle is located. It raises the I/O error if the file does not exist. This is the default mode for opening files as well.
# Read and Write ('r+’): This method opens the file for both reading and writing. The start of the file is where the handle is located. If the file does not exist, an I/O error gets raised.
# Write Only ('w’): This mode opens the file for writing only. The data in existing files are modified and overwritten. The start of the file is where the handle is located. If the file does not already exist in the folder, a new one gets created.
# Write and Read ('w+’): This mode opens the file for both reading and writing. The text is overwritten and deleted from an existing file. The start of the file is where the handle is located.
# Append Only ('a’): This mode allows the file to be opened for writing. If the file doesn't yet exist, a new one gets created. The handle is set at the end of the file. The newly written data will be added at the end, following the previously written data.
# Append and Read (‘a+’): Using this method, you can read and write in the file. If the file doesn't already exist, one gets created. The handle is set at the end of the file. The newly written text will be added at the end, following the previously written data

file1 = open("./manejoArchivos/prueba.txt", "w+")
L = ["Probamos a escribir en un archivo \n",
     "Escribimos una linea más \n",
     "Y ahora un gran final \n"]
file1.write("Escritura simple \n")
file1.writelines(L)
file1.close()

file1 = open("./manejoArchivos/prueba.txt", "r+")
print("Leemos el archivo")
print("******************")
print(file1.read())
print("******************")
file1.seek(0)
print(file1.readline())
print(file1.readline())
file1.close()
