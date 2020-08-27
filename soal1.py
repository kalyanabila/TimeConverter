# Soal 1

def timeConverter(seconds):
    
    # Condition sesuai soal hanya menerima angka bulat, dengan nilai maksimal 359999,
    # jika user memasukkan nilai lebih dari 359999, bilangan desimal , bilangan negatif, 
    # maupun memasukkan string akan keluar notifikasi. Invalid Input 
    if seconds >= 0 and type(seconds) == int and seconds < 359999:
        hours = seconds // (60*60)      # hour = 60*60 seconds
        seconds %= (60*60)              # modulo 3600 second, agar setiap 3600s akan di translate = hours 1
        minutes = seconds // 60         # minute = 60 seconds
        seconds %= 60                   # modulo 3600 second, agar setiap 60s akan di translate = hours 1
        return "%02i:%02i:%02i" % (hours, minutes, seconds)  # return value ke misal "01:01:05" jika menginput '3665'
   
    

minutes = 60
hours = 60*60
seconds = int(input('Masukan detik : '))  # Untuk input detik yg diinginkan
print(timeConverter(seconds))             # menampilkan hasil dari function