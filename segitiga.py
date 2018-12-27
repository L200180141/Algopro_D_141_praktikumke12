def hitung_luas():
    "fungsi menghitung luas dari segitiga"
    s = a * t / 2
    return s

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Menghitung Luas Bangun Geometri</title></head>
<body>"""
a = 5
t = 8
print """<table>
<tr>
<td rowspan="7"><img src="face.jpg" width="100"></td>
<th align="left">Bangun Geometri</th>
</tr>
<tr>
<td>Nama bangun : Segitiga</td>
</tr>
<tr>
<td>Dimensi (2D/3D): 2D</td>
</tr>
<tr>
<td>Rumus luas : Alas x Tinggi / 2</td>
</tr>
<tr>
<td>Parameter 1 : {}</td>
</tr>
<tr>
<td>Parameter 2 : {}</td>
</tr
<tr>
<td>Luas : """.format(a, t)
print hitung_luas(), """</td>
</tr></table></body>"""
print "</html>"
