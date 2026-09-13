import tkinter as tk
import random
import time
import threading
import playsound as playsound

kopf_zaehler = 0
zahl_zaehler = 0
wurf_anzahl = 0
wurf_aktiv = False

root = tk.Tk()
root.title("Münzenwurf By Memo")
root.geometry("400x400")
root.config(bg="#1e1e1e")

ergebnis_label = tk.Label(root, text="Bereit zum Werfen?!", font=("Arial", 18, "bold"), fg="white", bg="#1e1e1e")
ergebnis_label.pack(pady=20)

anim_label = tk.Label(root, text="", font=("Arial", 40), fg="gold", bg="#1e1e1e")
anim_label.pack(pady=20)

statistik_label = tk.Label(root, text="", font=("Arial", 12), fg="lightgray", bg="#1e1e1e")
statistik_label.pack(pady=20)

def animation_spin():
    frames = ["🪙", "⚙️", "💫", "🔄", "🌀", "💫", "🪙"]
    for f in frames:
        anim_label.config(text=f)
        root.update()
        time.sleep(0.1)

def play_sound():
    try:
        playsound.playsound("coin.mp3", block=False)
    except:
        pass

def muenzenwurf():
    global kopf_zaehler, zahl_zaehler, wurf_anzahl, wurf_aktiv
    
    if wurf_aktiv:
        return
    
    wurf_aktiv = True
    
    threading.Thread(target=play_sound).start() 
    animation_spin()
    
    ergebnis = random.choice(["Kopf", "Zahl"])
    ergebnis_label.config(text=f"Die Münze zeigt {ergebnis}")
    
    wurf_anzahl += 1
    if ergebnis == "Kopf":
        kopf_zaehler += 1
    else:
        zahl_zaehler += 1
        
    statistik_label.config(
        text=f"Würfe: {wurf_anzahl}\nKopf: {kopf_zaehler} | Zahl: {zahl_zaehler}"
    )           
    
    wurf_aktiv = False

def reset_statistik():
    global kopf_zaehler, zahl_zaehler, wurf_anzahl
    kopf_zaehler = 0
    zahl_zaehler = 0
    wurf_anzahl = 0
    ergebnis_label.config(text="Bereit für einen neuen Start!")
    statistik_label.config(text="")
    anim_label.config(text="♻️")    

wurf_button = tk.Button(root, text="Werfen", command=muenzenwurf, font=("Arial", 14), bg="#4caf50", fg="white", width=12)
wurf_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Statistik", command=reset_statistik, font=("Arial", 12), bg="#ff9800", fg="white", width=15)
reset_button.pack(pady=5)

exit_button = tk.Button(root, text="Beenden", command=root.destroy, font=("Arial", 12), bg="#f44336", fg="white", width=12)
exit_button.pack(pady=10)

root.mainloop()