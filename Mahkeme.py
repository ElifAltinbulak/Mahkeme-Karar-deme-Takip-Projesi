import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3
window=tk.Tk()
window.title("Dava Takip")
window.geometry("830x680")
def faizfunction():
    try:
        a,b,c,d=entry17.get(),entry18.get(),entry22.get(),entry14.get()
        gun1,ay1,yıl1=a.split(".")
        gun2,ay2,yıl2=b.split(".")
        tarih1=datetime(int(yıl1),int(ay1),int(gun1))
        tarih2=datetime(int(yıl2),int(ay2),int(gun2))
        fark=abs(tarih2-tarih1)
        apf=int(c)*9
        gf=apf*fark.days
        ft=gf/36000
        ofm=ft+int(c)
        otm=int(d)+ofm
        print(fark.days)
        print(otm)
        labelyen.configure(text=otm)
        label21e.configure(text=fark.days)
    except ValueError:
        message_box=messagebox.askretrycancel(title="Dikkat",message="Bir sayı eksik, hatalı ya da tarih arasına yanlış bir işaret girdiniz tekrar deneyiniz (tarih arası giriş için nokta kullanınız.)")
    
def checkButtonFunction1():
    if save_var1.get()==1:
        print("ödeme işlemi kayıt edilir")
    else:
        print("ödeme işlemi kayıt edilmez")
def buttonFunction():
    value=entry.get()
    label4.configure(text = value,font="Times 20")
def checkButtonFunction():
    if save_var.get()==1:
        print("Çalışır")
        faizfunction()
    else:
        print("Çalışmaz")
        print(entry12.get())
def KayıtButtonFunction():
    conn=sqlite3.connect("Mahkemekayıt.db")
    c=conn.cursor()
    evraktakıpno=entry.get()
    gun=entry1.get()
    ay=entry2.get()
    yıl=entry3.get()
    gelenevraktarıh=entry5.get()
    sayı=entry6.get()
    ıcerık=comboBox.get()
    konu=text8.get("1.0",'end-1c')
    mahkemeadı=comboBox1.get()
    mahkemekararıno=entry10.get()
    mahkemesasno=entry11.get()
    vekaletucretı=entry12.get()
    yargılamagıderı=entry13.get()
    tazmınantmıktarı=entry14.get()
    nott=text15.get("1.0",'end-1c')
    buton1=save_var.get()
    mahkemekarartarıhı=entry16.get()
    tarıh1=entry17.get()
    tarıh2=entry18.get()
    gunsayısı=label21e.cget("text")
    anapara=entry22.get()
    faıztutarı=labelyen.cget("text")
    odemeyapıldımı=save_var1.get()
    davacıvekil1=entry26.get()
    davacıvekil2=entry27.get()
    davacıadısoyadı=comboBox2.get()
    davalıvekıl1=entry29.get()
    mudahıl=entry30.get()
    baroadı=entry31.get()
    vergıno=entry32.get()
    odemeacıklama=text32.get("1.0",'end-1c')
    davalıadısoyadı=comboBox3.get()
    paraf=comboBox4.get()
    unvan1=comboBox5.get()
    unvan2=comboBox6.get()
    kayıtyapan=comboBox7.get()
    c.execute("""CREATE TABLE IF NOT EXISTS mahkemekayıt (evraktakıpno TEXT, gun INT, ay INT, yıl INT, gelenevraktarıh DATE, sayı INT, ıcerık TEXT, konu TEXT, mahkemeadı TEXT,mahkemekararıno INT, mahkemesasno INT, vekaletucretı INT, yargılamagıderı INT,tazmınantmıktarı INT, nott TEXT,buton1 TEXT,mahkemekarartarıhı DATE, tarıh1 DATE,tarıh2 DATE,gunsayısı INT,anapara INT,faıztutarı INT,odemeyapıldımı TEXT,davacıvekil1 TEXT,davacıvekil2 TEXT,davacıadısoyadı TEXT,davalıvekıl1 TEXT,mudahıl TEXT,baroadı TEXT,vergıno INT,odemeacıklama TEXT,davalıadısoyadı TEXT,paraf TEXT,unvan1 TEXT,unvan2 TEXT,kayıtyapan TEXT)""")
    c.execute("INSERT INTO mahkemekayıt VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(evraktakıpno,gun,ay,yıl,gelenevraktarıh,sayı,ıcerık,konu,mahkemeadı,mahkemekararıno,mahkemesasno,vekaletucretı,yargılamagıderı,tazmınantmıktarı,nott,buton1,mahkemekarartarıhı,tarıh1,tarıh2,gunsayısı,anapara,faıztutarı,odemeyapıldımı,davacıvekil1,davacıvekil2,davacıadısoyadı,davalıvekıl1,mudahıl,baroadı,vergıno,odemeacıklama,davalıadısoyadı,paraf,unvan1,unvan2,kayıtyapan))
    conn.commit()
    conn.close()
        
    entry.delete(0,tk.END)
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)
    entry5.delete(0,tk.END)
    entry6.delete(0,tk.END)
    comboBox.set("")
    text8.delete("1.0",tk.END)
    comboBox1.set("")
    entry10.delete(0,tk.END)
    entry11.delete(0,tk.END)
    entry12.delete(0,tk.END)
    entry13.delete(0,tk.END)
    entry14.delete(0,tk.END)
    text15.delete("1.0",tk.END)
    save_var.set(0)
    entry16.delete(0,tk.END)
    entry17.delete(0,tk.END)
    entry18.delete(0,tk.END)
    label21e.destroy()
    entry22.delete(0,tk.END)
    labelyen.destroy()
    save_var1.set(0)
    entry26.delete(0,tk.END)
    entry27.delete(0,tk.END)
    comboBox2.set("")
    entry29.delete(0,tk.END)
    entry30.delete(0,tk.END)
    entry31.delete(0,tk.END)
    entry32.delete(0,tk.END)
    text32.delete("1.0",tk.END)
    comboBox3.set("")
    comboBox4.set("")
    comboBox5.set("")
    comboBox6.set("")
    comboBox7.set("")
def SilButtonFunction():
    global kayıtentry
    kayıtsıl=tk.Label(window,text="Evrak Takip No Giriniz:")
    kayıtentry=tk.Entry(window)
    kayıtsılbuton=tk.Button(window,text="Sil",command=delete)
    kayıtsıl.place(x=270,y=620)
    kayıtentry.place(x=392,y=620)
    kayıtsılbuton.place(x=350,y=638)
def delete():
    try:
        entry=kayıtentry
        conn=sqlite3.connect("Mahkemekayıt.db")
        c=conn.cursor()
        c.execute("DELETE from mahkemekayıt WHERE evraktakıpno =" + kayıtentry.get() )
        conn.commit()
        conn.close()
        kayıtentry.delete(0,tk.END)
    except sqlite3.OperationalError:
        message_box2=messagebox.askretrycancel(title= "Dikkat",message="Geçersiz bir değer girdiniz.")
def uyarı():
    message_box3=messagebox.showinfo(title="Lütfen Dikkat!",message="Lütfen 'Evrak Takip No' kısmına '-_?/*+&%' ifadeler kullanmayınız! Ayrıca başlarken bir 15 saniye gecikme olabilir")
def show():
    root=tk.Tk()
    root.title("Kayıt Listesi")
    root.geometry("900x200")
    conn=sqlite3.connect("Mahkemekayıt.db")
    c=conn.cursor()
    c.execute("SELECT * FROM mahkemekayıt")
    result=c.fetchall()
    liste=["evraktakıpno","gun","ay","yıl","gelenevraktarıh","sayı","içerik","konu","Mahkeme Adı","Mahkeme Karar No","Mahkeme Esas No","Vekalet Ucreti","Yargılama Gideri","Not",
           "Buton1","Mahkeme Karar Tarıhı","Tarih1","Tarih2","Gun Sayısı","Anapara","Faiz Tutarı","Ödeme Yapıldı mı?","Davacı Vekili1","Davalı Vekili2","Davacı Adı Soyadı","Davalı vekili",
           "Mudahil","Baro adı","Vergi No","Ödeme Açıklama","Davalı Adı Soyadı","Paraf","Unvan1","Unvan2","Kayıt Yapan"]
    y=""
    for j in liste:
        y +=str(j)+"\t"
    labels1=tk.Label(root,text=y,bg="red")
    labels1.place(x=0,y=0)
    p=""
    for i in result:
        p += str(i) + "\t" +"\n"
    #str(i[1])+ "\t" +str(i[2])+str(i[3])+str(i[4])+str(i[5])+str(i[6])+str(i[7])+str(i[8])+str(i[9])+str(i[10])+str(i[11])+str(i[12])+str(i[13])+str(i[14])+str(i[15])+str(i[16])+str(i[17])+str(i[18])+str(i[19])+str(i[20])+str(i[21])+str(i[22])+str(i[23])+str(i[24])+str(i[25])+str(i[26])+str(i[27])+str(i[28])+str(i[29])+str(i[30])+str(i[31])+str(i[32])+str(i[33])+str(i[34])
    labels=tk.Label(root,text=p)
    labels.place(x=0,y=28)
    conn.commit()
    conn.close()
uyarı()
label=tk.Label(window,text="....... GENEL MÜDÜRLÜĞÜ",font="Times 16",fg="red")
label.pack()
label1=tk.Label(window,text="Evrak Takip No: ",font="Times 10")
label1.place(x=15,y=40)
entry=tk.Entry(window)
entry.place(x=110,y=40)
buton=tk.Button(window, text="Evrak Takip No Kayıt",command= buttonFunction)
buton.place(x=300,y=50)
frame=tk.LabelFrame(window,text="Kayıt Tarihi",width=250,height=80)
entry1=tk.Entry(frame,width=3)
entry1.place(x=100,y=20)
label2=tk.Label(frame,text="/")
label2.place(x=125,y=20)
entry2=tk.Entry(frame,width=3)
entry2.place(x=139,y=20)
label3=tk.Label(frame,text="/")
label3.place(x=161,y=20)
entry3=tk.Entry(frame,width=6)
entry3.place(x=172,y=20)
frame.place(x=15,y=70)
label4=tk.Label(window,fg="red")
label4.place(x=300,y=100)
label5=tk.Label(window,text="Gelen Evrak Tarih")
label5.place(x=15,y=165)
entry5=tk.Entry(window)
entry5.place(x=115,y=165)
label6=tk.Label(window,text="Sayı")
label6.place(x=270,y=165)
entry6=tk.Entry(window)
entry6.place(x=300,y=165)
label7=tk.Label(window,text="İçerik")
label7.place(x=15,y=195)
problem=tk.StringVar()
comboBox=ttk.Combobox(window, textvariable=problem, values=("Vekalet Ücreti","Yargılama Gideri","İcra","Tazminat","Yargılama Gideri ve Vekalet Ücreti","Mahkeme Harcı","Nisbi Hizmet Harcı","Tazminat Yargılama Gideri ve Vekalet Ücreti"),state="readonly")
comboBox.place(x=114,y=195)
label8=tk.Label(window,text="Konusu")
label8.place(x=15,y=220)
text8=tk.Text(window,height=6,width=38,bd=2)
text8.place(x=114,y=220)
label9=tk.Label(window,text="Mahkeme Adı")
label9.place(x=15,y=330)
problem1=tk.StringVar()
comboBox1=ttk.Combobox(window,textvariable=problem1,values=("Ankara 18.İdare Mahkemesi","İstanbul Ağır Ceza Mahkemesi"))
comboBox1.place(x=114,y=330)
label10=tk.Label(window,text="Mahk. Karar No")
label10.place(x=15,y=374)
entry10=tk.Entry(window)
entry10.place(x=114,y=374)
label11=tk.Label(window,text="Mahk. Esas No")
label11.place(x=15,y=394)
entry11=tk.Entry(window)
entry11.place(x=114,y=394)
label12=tk.Label(window,text="Vekalet Ücreti")
label12.place(x=15,y=414)
entry12=tk.Entry(window)
entry12.place(x=114,y=414)
label13=tk.Label(window,text="Yargılama Gideri")
label13.place(x=15,y=434)
entry13=tk.Entry(window)
entry13.place(x=114,y=434)
label14=tk.Label(window,text="Tazminat Miktarı")
label14.place(x=15,y=455)
entry14=tk.Entry(window,bg="DarkSeaGreen4")
entry14.place(x=114,y=455)
label15=tk.Label(window,text="Not")
label15.place(x=15,y=480)
text15=tk.Text(window,height=6,width=34,bd=2)
text15.place(x=17,y=500)
save_var=tk.IntVar()
save_var.set(0)
c_button=tk.Checkbutton(window,text="Faiz Var Mı?",variable=save_var,font="Times 10",command = checkButtonFunction)
c_button.place(x=272,y=322)
label16=tk.Label(window,text="""Mahk.Karar Tarihi""")
label16.place(x=15,y=353)
entry16=tk.Entry(window)
entry16.place(x=114,y=353)

frame1=tk.LabelFrame(window,text="Faiz Hesaplama",width=163,height=152,)
frame1.place(x=260,y=343)
label17=tk.Label(frame1,text="Tarihi1")
label17.place(x=1,y=1)
entry17=tk.Entry(frame1,width=7)
entry17.place(x=41,y=1)
label18=tk.Label(frame1,text="Tarihi2")
label18.place(x=1,y=22)
entry18=tk.Entry(frame1,width=7)
entry18.place(x=41,y=22)
label19=tk.Label(frame1,text="Faiz Oranı",font="Time 7")
label19.place(x=87,y=0)
label20=tk.Label(frame1,text="9",font="Time 7")
label20.place(x=135,y=0)
label21=tk.Label(frame1,text="Gün Sayı",font="Time 7")
label21.place(x=87,y=33)
label21e=tk.Label(frame1,fg="red")
label21e.place(x=129,y=33)
buttonyenı=tk.Button(frame1,text="faizhesabı",command=faizfunction)
buttonyenı.place(x=-1,y=108)
label22=tk.Label(frame1,text="Ana Para",font="Time 7")
label22.place(x=41,y=54)
entry22=tk.Entry(frame1,width=7,bg="DarkSeaGreen4")
entry22.place(x=87,y=54)
label23=tk.Label(frame1,text="/3600+Anapara",font="Time 8")
label23.place(x=78,y=73)
label24=tk.Label(frame1,text="Faiz Tutarı",font=("Time 7"))
label24.place(x=39,y=88)
labelyen=tk.Label(frame1,fg="red")
labelyen.place(x=85,y=90)


save_var1=tk.IntVar()
save_var1.set(0)
c_button1=tk.Checkbutton(window,text="Ödeme Yapıldı mı?",variable=save_var1,font="Times 10",command=checkButtonFunction1)
c_button1.place(x=300,y=500)

frame2=tk.LabelFrame(window,text="Davacı",width=300,height=129)
label25=tk.Label(frame2,text="Davacı")
label25.place(x=20,y=16)
problem2=tk.StringVar()
comboBox2=ttk.Combobox(frame2, textvariable=problem2, values=("Adalet Bakanlığı","Türkiye Barolar Birliği","Ankara Barosu","İstanbul Barosu"))
comboBox2.place(x=100,y=15)
label26=tk.Label(frame2, text="1.Davacı Vekili")
label26.place(x=19,y=42)
entry26=tk.Entry(frame2)
entry26.place(x=100,y=42)
label27=tk.Label(frame2, text="2.Davacı Vekili")
label27.place(x=19,y=67)
entry27=tk.Entry(frame2)
entry27.place(x=100,y=67)
frame2.place(x=460,y=41)

frame3=tk.LabelFrame(window,text="Davalı", width=300,height=129)
label28=tk.Label(frame3, text="Davalı")
label28.place(x=20,y=16)
problem3=tk.StringVar()
comboBox3=ttk.Combobox(frame3,textvariable=problem3,values=("Adalet Bakanlığı","Türkiye Barolar Birliği","Ankara Barosu","İstanbul Barosu"))
comboBox3.place(x=100,y=15)
label29=tk.Label(frame3,text="1.Davalı Vekili")
label29.place(x=19,y=42)
entry29=tk.Entry(frame3)
entry29.place(x=100,y=42)
label30=tk.Label(frame3,text="Müdahil")
label30.place(x=19,y=67)
entry30=tk.Entry(frame3)
entry30.place(x=100,y=67)
frame3.place(x=460,y=170)

frame4=tk.LabelFrame(window,text="Ödeme Yapılan Baro",width=300,height=100)
label31=tk.Label(frame4,text="Baro Adı")
label31.place(x=20,y=16)
entry31=tk.Entry(frame4)
entry31.place(x=100,y=15)
label32=tk.Label(frame4,text="Vergi No")
label32.place(x=20,y=42)
entry32=tk.Entry(frame4)
entry32.place(x=100,y=42)
frame4.place(x=460,y=300)

label32=tk.Label(window,text="Ödeme Açıklama")
label32.place(x=461,y=401)
text32=tk.Text(width=37,height=4,bd=2)
text32.place(x=460,y=422)

frame5=tk.LabelFrame(window,text="Paraf",width=300,height=88)
problem4=tk.StringVar()
comboBox4=ttk.Combobox(frame5,textvariable=problem4,values=("1.amir","2.amir","3.amir"))
comboBox4.place(x=130,y=-2)
problem5=tk.StringVar()
comboBox5=ttk.Combobox(frame5,textvariable=problem5,values=("Hakim","Tetkik Hakim"))
comboBox5.place(x=130,y=20)
problem6=tk.StringVar()
comboBox6=ttk.Combobox(frame5,textvariable=problem6,values=("Daire Başkanı","Genel Müdür Yardımcısı"))
comboBox6.place(x=130,y=42)
frame5.place(x=460,y=497)

label33=tk.Label(window,text="Kayıt Yapan Personel")
label33.place(x=460,y=590)
problem6=tk.StringVar()
comboBox7=ttk.Combobox(window,textvariable=problem6,values=("Personel 1","Personel 2","Personel 3","Personel 4","Personel 5"))
comboBox7.place(x=592,y=590)

button=tk.Button(window,text="Kayıt Ekle",command=KayıtButtonFunction)
button.place(x=140,y=620)

button1=tk.Button(window,text=" Kayıt Sil ",command=SilButtonFunction)
button1.place(x=210,y=620)
button2=tk.Button(window,text="Kayıt Göster",command=show)
button2.place(x=60,y=620)
window.mainloop()
