# UAS_IoT

Bahasa pemrograman yang digunakan yaitu bahasa python, proteus untuk simulasi sensor, dan virtual serial port emulator. 
ALur dari pengambilan nilai dari sensor yaitu sensor.py dijalankan terlebih dahulu kemudian sensor di proteus akan memberikan nilai yang dituliskan sebelumnya. Sensor yang digunakan yaitu sensor suhu. Kemudian nilai yang diberikan oleh proteus akan dikirimkan ke url website yang sudah dituliskan pada file sensor.py. Pada proteus sendiri yang menyambungkan antara sensor dengan website terdapat dalam file.hex nya.

Dalam file sensor.py terdapat library python yang harus ditambahkan agar sensor dapat terkirim yaitu libray request(untuk mengirimkan nilai pada url) dan library serial(untuk koneksi serial port demgan website)

Pada percobaan koneksi sensor dari proteus ke website, board arduino yang digunakan terdapat error port vcc tidak tersedia pada board arduino yang digunakan.
