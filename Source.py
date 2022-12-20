# import
import publisher1
import publisher2
import publisher5
import subprocess
import kusur
import serial
ser = serial.Serial('',9600)
# Vnesuvanje na pocetni vrednosti na sharzerot
s1=20;
s2=20;
s5=20;
#ova da se stavi vo while true sto ke mozhe da se prekine so ctrl+q
# Proverka dali nekoj od sarzerite e prazen
if s1<3:
    publisher1.main() #da isprakja deka nema 1
elif s2<3:
    publisher2.main() #da isprakja deka nema 2
elif s3<2:
    publisher5.main() #da isprakja deka nema 3    
# Pravenje na slika
subprocess.call([r'path\slika.bat'])
# Obrabotka na slika
detect.py #treba da se sredi(vrakja cena, [produkti])
# Vnesuvame kolku pari imame
pari = input("Vnesi pari")
k = pari-cena
if k<0:
    #info kon arduino da sveti crven led
    pass
elif k==0:
    promet=promet+cena
    #info kon arduino da sveti zelen led
    publisher.py #da prakja s1,s2,s5, time, promet, [produkti]
    main(s1, s2, s5, time, promet, produkti)
else:
    servo_dvizhenja = kusur.main() #vrakja [x1,x2,x5]
    s1=s1-x1;s2=s2-x2;s5=s5-x3
    #info kon arduino [x1,x2,x5]
    ser.write(x1)
    ser.write(x2)
    ser.write(x3)
    publisher.py #da prakja s1,s2,s5, time, promet, [produkti]

