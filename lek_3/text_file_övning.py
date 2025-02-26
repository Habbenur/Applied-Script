with open ("test_file_exempel.txt", "w") as file:
    file.write("Asrin\nHabbe\nAbdullah\nElif\nMehtap\nHuseyin")

with open ("test_file_exempel.txt", "r") as file:
    for rad in file:
        print(rad.strip())