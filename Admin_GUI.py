from tkinter import *
from tkinter import messagebox
import boto3
import botocore
from time import sleep
import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from fpdf import FPDF
from botocore.client import Config
from datetime import date
import os
check=0
check_window1=0
# Create an S3 client
s3 = boto3.resource('s3')
x=open('admin_details.txt','r').read().split()
username=x[0]
password=x[1]
global  dn,pn_pdfd,aadhar,spec,depart
dn=''
pn_pdfd=''
aadhar=''
spec=''
depart=''
def reset_memory():
    pass
def forgot():
    def sub_btn():
        new_pwd=password_f.get()
        new_usr=username_f.get()
        if len(new_pwd)<7 or len(new_usr)<5:
            messagebox.showerror('Error','1.Username must contain minimum 5 characters\n2.Password must contain minimum 7 characters')
            window_f.destroy()
            forgot()
        else:
            global username,password
            concat=new_usr+" "+new_pwd
            x=open('admin_details.txt','w').write(concat)
            messagebox.showinfo('Information','Details Successfully updated')
            x=open('admin_details.txt','r').read().split()
            username=x[0]
            password=x[1]
            window_f.destroy()
    window_f=Toplevel()
    window_f.configure(bg='#ff8484')
    window_f.geometry('400x350+200+2')
    window_f.resizable(0,0)
    frame1=Frame(window_f)
    username_l=Label(frame1,text='User Name : ',font=("Ariel",16),bg='#ff8484')
    username_l.pack(side='left')
    username_f=Entry(frame1,width=20,font=("Ariel",16))
    username_f.pack(side='left')
    frame1.pack()
    waste1=Frame(window_f,bg='#ff8484')
    lab_waste=Label(waste1,text=' ',bg='#ff8484',).pack(fill='x')
    waste1.pack(fill='x')
    frame2=Frame(window_f,bg='#ff8484')
    password_l=Label(frame2,text='  Password   : ',font=("Ariel",16),bg='#ff8484')
    password_l.pack(side='left')
    password_f=Entry(frame2,show="*",width=20,font=("Ariel",16))
    password_f.pack(side='left')
    frame2.pack(fill='x')
    waste2=Frame(window_f,bg='#ff8484')
    lab_waste=Label(waste2,text=' ',bg='#ff8484',).pack(fill='x')
    waste2.pack()
    frame1=Frame(window_f,bg='#ff8484')
    #label_w=Label(frame1,text='                             ',bg='#ff8484').pack(side='left')
    button=Button(frame1,text='Submit',font=("Ariel",12),command=sub_btn)
    button.pack()
    frame1.pack()
    window_f.mainloop()
def destroy():
    window.destroy()
def submit(event=0):
    def save():
        global cv2image
        cv2image = cv2.cvtColor(cv2image, cv2.COLOR_RGB2BGR)
        cv2.imwrite('mypic.png',cv2image.copy())
        mypic2=PhotoImage(file='mypic.png')
        photo_click.config(image=mypic2)
        photo_click.photo=mypic2
        window_o.destroy()
    def photo(event=0):
        #Set up GUI
        global window_o,cap
        window_o = Toplevel()  #Makes main window
        window_o.title("Camera")
        window_o.config(background="#FFFFFF")
        #Graphics window
        imageFrame = Frame(window_o, width=600, height=500)
        imageFrame.grid(row=0, column=0, padx=5, pady=2)
        #Capture video frames
        lmain = Label(imageFrame)
        lmain.grid(row=0, column=0)
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        def show_frame():
            global cv2image
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)
        #Slider window (slider controls stage position)
        sliderFrame = Frame(window_o, width=200, height=100)
        sliderFrame.grid(row = 600, column=0, padx=5, pady=2)
        button=Button(window_o,text="save",command=save)
        button.grid(row=601)
        show_frame()  #Display 2
        window_o.mainloop()  #Starts GUI
    def create_f():
        global  dn,pn_pdfd,aadhar,spec,depart
        dn=''
        pn_pdfd=''
        aadhar=''
        spec=''
        depart=''
    def preview_f():
        global s3,d_pn_e,window1,dn_e,aadhar_e,spec_e,depart_e,window_nd
        global dn,pn_pdfd,aadhar,spec,depart
        dn=dn_e.get()
        pn_pdfd=d_pn_e.get()
        aadhar=aadhar_e.get()
        spec=spec_e.get()
        depart=depart_e.get()
        def back_y(event=0):
            global check_window1
            check_window1=0
            window2.destroy()
            newdoctor()
        def window2_clear():
            window2.destroy()
            home_page()
        window_nd.destroy()
        window2=Tk()
        window2.config(bg='#ff8484')
        window2.title('{}\' Details'.format(dn))
        window2.wm_attributes('-fullscreen','true')
        f_back=Frame(window2,bg='#ff8484')
        back_image=PhotoImage(file="Back_Arrow.png")
        back_label=Label(f_back,image=back_image,bg='#ff8484')
        back_label.pack(side='left')
        back_label.bind('<Button-1>',back_y)
        f_back.pack(fill='x')
        frame0=Frame(window2,bg='#ff8484')
        info=Label(frame0,text="Preview - Details",bg='#ff8484',font=('Arial',23)).pack()
        frame0.pack(fill='x')
        frame0_p=Frame(window2,bg='#ff8484')
        doctor_pic_i=PhotoImage(file='Photo_upload_image.png')
        doctor_pic=Label(frame0_p,image=doctor_pic_i)
        doctor_pic.photo=doctor_pic_i
        doctor_pic.pack()
        spaceF=Frame(window2,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame0_p.pack(fill='x')
        frame1=Frame(window2,bg='#ff8484')
        spaceL=Label(frame1,text='\t\t\t\t\t\t\t\t\t\t',bg='#ff8484').pack(side='left')
        doctor_n=Label(frame1,text='Name \t          : {}'.format(dn),font=('Arial',20),bg='#ff8484')
        doctor_n.pack(side='left')
        frame1.pack(fill='x')
        frame2=Frame(window2,bg='#ff8484')
        spaceL=Label(frame2,text='\t\t\t\t\t\t\t\t\t\t',bg='#ff8484').pack(side='left')
        doctor_pn=Label(frame2,text='Phone Number   : {}'.format(pn_pdfd),font=('Arial',20),bg='#ff8484')
        doctor_pn.pack(side='left')
        frame2.pack(fill='x')
        frame3=Frame(window2,bg='#ff8484')
        spaceL=Label(frame3,text='\t\t\t\t\t\t\t\t\t\t',bg='#ff8484').pack(side='left')
        doctor_aadhar=Label(frame3,text='Adhaar Number  : {}'.format(aadhar),font=('Arial',20),bg='#ff8484')
        doctor_aadhar.pack(side='left')
        frame3.pack(fill='x')
        frame4=Frame(window2,bg='#ff8484')
        spaceL=Label(frame4,text='\t\t\t\t\t\t\t\t\t\t',bg='#ff8484').pack(side='left')
        doctor_spec=Label(frame4,text='Specification\'s    : {}'.format(spec),font=('Arial',20),bg='#ff8484')
        doctor_spec.pack(side='left')
        frame4.pack(fill='x')
        frame5=Frame(window2,bg='#ff8484')
        spaceL=Label(frame5,text='\t\t\t\t\t\t\t\t\t\t',bg='#ff8484').pack(side='left')
        doctor_depart=Label(frame5,text='Department        : {}'.format(depart),font=('Arial',20),bg='#ff8484')
        doctor_depart.pack(side='left')
        frame5.pack(fill='x')
        spaceF=Frame(window2,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame7=Frame(window2,bg='#ff8484')
        create=Button(frame7,text="Create Account",font=('Arial',16),command=create_f)
        create.pack()
        frame7.pack(fill='x')
        spaceF=Frame(window2,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame8=Frame(window2,bg='#ff8484')
        close=Button(frame8,text="Close",font=('Arial',16),command=window2_clear)
        close.pack()
        frame8.pack(fill='x')
        window2.mainloop()
        '''cap.release()
        def pdf():
            pdf=FPDF()
            pdf.add_page()
            pdf.set_font('Arial',size=16)
            #pdf.image('mypic.png')
            pdf.cell(200,10,txt="Doctor Name : {}".format(dn),ln=1)
            pdf.cell(200,10,txt="Phone Number : {}".format(pn_pdfd),ln=1)
            pdf.cell(200,10,txt="Adhaar Number : {}".format(aadhar),ln=1)
            pdf.cell(200,10,txt="Specifications : {}".format(spec),ln=1)
            pdf.cell(200,10,txt="Department : {}".format(depart),ln=1)
            pdf.cell(200,10,txt="Joined Date : {}".format(date_t),ln=1)
            pdf.cell(200,10,txt="Doctor Image : ",ln=1)
            pdf.image('mypic.png')
            pdf.output("{}.pdf".format(pn_pdfd))
            acces_key='AKIAI43MM4QUVYVDT5WA'
            access_s_key='llOZ980qQMzZnicwsInsAEhtasL1Vg1iI/OKG5BC'
            bucket='530045admin'
            var=open('{}.pdf'.format(pn_pdfd),'rb')
            print('ok1')
            s3=boto3.resource('s3',aws_access_key_id=acces_key,
                              aws_secret_access_key=access_s_key,
                              config=Config(signature_version='s3v4')
                              )
            #print('ok2')
            s3.Bucket(bucket).put_object(Key='{}.pdf'.format(pn_pdfd),Body=var).Acl().put(ACL='public-read')
            var.close()
            os.remove('{}.pdf'.format(pn_pdfd))
            #print("Done")
        global s3,d_pn_e,window1,dn_e,aadhar_e,spec_e,depart_e
        #print(d_pn_e.get())
        if not(d_pn_e=='' and dn_e=='' and aadhar_e=='' and spec_e=='' and depart_e==''):
            def y():
                def back_y(event=0):
                    window2.destroy()
                    home_page()
                global dn,pn_pdfd,aadhar,spec,depart
                dn=dn_e.get()
                pn_pdfd=d_pn_e.get()
                aadhar=aadhar_e.get()
                spec=spec_e.get()
                depart=depart_e.get()
                s3.create_bucket(Bucket='530045'+d_pn_e.get(),CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
                bucket=s3.Bucket('530045'+d_pn_e.get())
                bucket.Acl().put(ACL='public-read')
                pdf()
                messagebox.showinfo('Information','Account Created Successfully')
                window_nd.destroy()
                window2=Tk()
                window2.config(bg='#ff8484')
                window2.title('{}\' Details'.format(dn))
                window2.wm_attributes('-fullscreen','true')
                f_back=Frame(window2,bg='#ff8484')
                back_image=PhotoImage(file="Back_Arrow.png")
                back_label=Label(f_back,image=back_image,bg='#ff8484')
                back_label.pack(side='left')
                back_label.bind('<Button-1>',back_y)
                f_back.pack(fill='x')
                frame0=Frame(window2,bg='#ff8484')
                info=Label(frame0,text="Account Created Successfully ",bg='#ff8484',font=('Arial',23)).pack(side='left')
                frame0.pack(fill='x')
                frame0_p=Frame(window2,bg='#ff8484')
                doctor_pic_i=PhotoImage(file='mypic.png')
                doctor_pic=Label(frame0_p,image=doctor_pic_i)
                doctor_pic.photo=doctor_pic_i
                doctor_pic.pack(side='left')
                frame0_p.pack(fill='x')
                frame1=Frame(window2,bg='#ff8484')
                doctor_n=Label(frame1,text='Name : {}'.format(dn),font=('Arial',20),bg='#ff8484')
                doctor_n.pack(side='left')
                frame1.pack(fill='x')
                frame2=Frame(window2,bg='#ff8484')
                doctor_pn=Label(frame2,text='Phone Number : {}'.format(pn_pdfd),font=('Arial',20),bg='#ff8484')
                doctor_pn.pack(side='left')
                frame2.pack(fill='x')
                frame3=Frame(window2,bg='#ff8484')
                doctor_aadhar=Label(frame3,text='Adhaar Number : {}'.format(aadhar),font=('Arial',20),bg='#ff8484')
                doctor_aadhar.pack(side='left')
                frame3.pack(fill='x')
                frame4=Frame(window2,bg='#ff8484')
                doctor_spec=Label(frame4,text='Specification\'s : {}'.format(spec),font=('Arial',20),bg='#ff8484')
                doctor_spec.pack(side='left')
                frame4.pack(fill='x')
                frame5=Frame(window2,bg='#ff8484')
                doctor_depart=Label(frame5,text='Department : {}'.format(depart),font=('Arial',20),bg='#ff8484')
                doctor_depart.pack(side='left')
                frame5.pack(fill='x')
                window2.mainloop()
                #s.remove('doctor_details.pdf')
            except
                messagebox.showerror('Information','Account not Created')
            y()
        else:
            messagebox.showinfo('Information','Fill all the Credentials')'''
    def clear(event=0):
        pn_e.delete(0,END)
        pn_e.unbind('<Button-1>')
        pn_e.config(fg='black')
    def get_details():
        pass
    def piechart_g():
        pass
    def olddoctor():
        global entry_old_d
        def back_old(event=0):
            window_old.destroy()
            if check==1:
                os.remove('{}.pdf'.format(remove_d_pdf))
            home_page()
        def get_old():
            global check,remove_d_pdf
            check=1
            print(entry_old_d.get())
            s3 = boto3.client('s3')
            s3.download_file('530045admin', '{}.pdf'.format(entry_old_d.get()), '{}.pdf'.format(entry_old_d.get()))
            remove_d_pdf=entry_old_d.get()
            os.startfile('{}.pdf'.format(entry_old_d.get()))
        def clear(event=0):
            entry_old_d.delete(0,END)
            entry_old_d.unbind('<Button-1>')
            entry_old_d.config(fg='black')
        window1.destroy()
        window_old=Tk()
        window_old.wm_attributes('-fullscreen',True)
        window_old.configure(background='#ff8484')
        f_back=Frame(window_old,bg='#ff8484')
        back_image_old=PhotoImage(file="Back_Arrow.png")
        back_label=Label(f_back,image=back_image_old,bg='#ff8484')
        back_label.pack(side='left')
        back_label.bind('<Button-1>',back_old)
        f_back.pack(fill='x')
        frame=Frame(window_old,bg='#ff8484')
        label=Label(frame,text='Doctor\'s Phone Number : ',font=('Arial',22),bg='#ff8484')
        label.pack(side='left')
        entry_old_d=Entry(frame,fg='#D3D3D3',width=20,font=('Arial',18))
        entry_old_d.pack(side='left')
        entry_old_d.insert(0,'Ex:- 7986410856')
        label_w=Label(frame,text='         ',bg='#ff8484').pack(side='left')
        entry_old_d.bind('<Button-1>',clear)
        button=Button(frame,text='Get Details',font=('Arial',18),command=get_old)
        button.pack(side='left')
        frame.pack(fill='x')
        window_old.mainloop()
    def newdoctor():
        global dn_e,d_pn_e,aadhar_e,spec_e,depart_e,window1,photo_click,window_nd,date_t,check_window1,dn,pn_pdfd,aadhar,spec,depart
        def back_new(event=0):
            window_nd.destroy()
            home_page()
        if check_window1==1:
            window1.destroy()
        window_nd=Tk()
        window_nd.configure(bg='#ff8484')
        window_nd.resizable(0,0)
        window_nd.wm_attributes('-fullscreen','true')
        f_back=Frame(window_nd,bg='#ff8484')
        back_image_new=PhotoImage(file="Back_Arrow.png")
        back_label=Label(f_back,image=back_image_new,bg='#ff8484')
        back_label.pack(side='left')
        back_label.bind('<Button-1>',back_new)
        f_back.pack(fill='x')
        frame_w=Frame(window_nd,bg='#ff8484')
        label_w=Label(frame_w,text=' ',bg='#ff8484').pack()
        frame_w.pack(fill='x')
        frame0=Frame(window_nd,bg='#ff8484')
        dn1=Label(frame0,text="Doctor Name     : ",bg='#ff8484',font=('Arial',18))
        dn1.pack(side='left')
        dn_e=Entry(frame0,width=20,font=('Arial',18))
        dn_e.insert(0,dn)
        dn_e.pack(side='left')
        frame0.pack(fill='x')
        spaceF=Frame(window_nd,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame1=Frame(window_nd,bg='#ff8484')
        d_pn1=Label(frame1,text="Phone Number  : ",bg='#ff8484',font=('Arial',18))
        d_pn1.pack(side='left')
        d_pn_e=Entry(frame1,width=20,font=('Arial',18))
        d_pn_e.insert(0,pn_pdfd)
        d_pn_e.pack(side='left')
        frame1.pack(fill='x')
        spaceF=Frame(window_nd,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame1_1=Frame(window_nd,bg='#ff8484')
        aadhar1=Label(frame1_1,text="Adhaar Number : ",font=('Arial',18),bg='#ff8484')
        aadhar1.pack(side='left')
        aadhar_e=Entry(frame1_1,width=20,font=('Arial',18))
        aadhar_e.insert(0,aadhar)
        aadhar_e.pack(side='left')
        frame1_1.pack(fill='x')
        spaceF=Frame(window_nd,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame2=Frame(window_nd,bg='#ff8484')
        spec1=Label(frame2,text="Specification      : ",bg='#ff8484',font=('Arial',18))
        spec1.pack(side='left')
        spec_e=Entry(frame2,width=20,font=('Arial',18))
        spec_e.insert(0,spec)
        spec_e.pack(side='left')
        frame2.pack(fill='x')
        spaceF=Frame(window_nd,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame3=Frame(window_nd,bg='#ff8484')
        depart1=Label(frame3,text="Department       : ",font=('Arial',18),bg='#ff8484')
        depart1.pack(side='left')
        depart_e=Entry(frame3,width=20,font=('Arial',18))
        depart_e.insert(0,depart)
        depart_e.pack(side='left')
        frame3.pack(fill='x')
        spaceF=Frame(window_nd,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame3_1=Frame(window_nd,bg='#ff8484')
        date_t=str(date.today().day)+'/'+str(date.today().month)+'/'+str(date.today().year)
        date_l=Label(frame3_1,text='Joined Date       : {}'.format(date_t),font=('Arial',18),bg='#ff8484')
        date_l.pack(side='left')
        frame3_1.pack(fill='x')
        spaceF=Frame(window_nd,bg='#ff8484')
        spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
        spaceF.pack()
        frame4=Frame(window_nd,bg='#ff8484')
        photo_d=Label(frame4,text="Photo : ",font=('Arial',18),bg='#ff8484')
        photo_d.pack(side='left')
        frame4_1=Frame(window_nd,bg='#ff8484')
        label_w=Label(frame4_1,text='                 ',bg='#ff8484').pack(side='left')
        image_c=PhotoImage(file='Photo_upload_image.png')
        photo_click=Label(frame4_1,image=image_c)
        photo_click.bind('<Button-1>',photo)
        photo_click.pack(side='left')
        frame4.pack(fill='x')
        frame4_1.pack(fill='x')
        frame5=Frame(window_nd,bg='#ff8484')
        files=Label(frame5,text="Files : ",font=('Arial',18),bg='#ff8484')
        files.pack(side='left')
        frame5.pack(fill='x')
        frame6=Frame(window_nd,bg='#ff8484')
        label_w=Label(frame6,text='                 ',bg='#ff8484').pack(side='left')
        choose=Button(frame6,text="Choose Files",font=('Arial',16))
        choose.pack(side='left')
        frame6.pack(fill='x')
        frame_w1=Frame(window_nd,bg='#ff8484')
        label_w1=Label(frame_w1,text=' ',bg='#ff8484').pack()
        frame_w1.pack(fill='x')
        frame7=Frame(window_nd,bg='#ff8484')
        spaceL=Label(frame7,text='          ',bg='#ff8484').pack(side='right')
        create=Button(frame7,text="Create Account",font=('Arial',16),command=create_f)
        create.pack(side='right')
        spaceL=Label(frame7,text='       ',bg='#ff8484').pack(side='right')
        preview=Button(frame7,text="Preview Account",font=('Arial',16),command=preview_f)
        preview.pack(side='right')
        frame7.pack()
        window_nd.mainloop()
    if username_e.get()==username and password_e.get()==password:
        destroy()
        global home_page
        def home_page():
            global window1,pn_e,check_window1
            def closeall():
                window1.destroy()
            window1=Tk()
            check_window1=1
            window1.configure(bg='#ff8484')
            #window.geometry('700x650+200+2')
            window1.resizable(0,0)
            frame_w=Frame(window1,bg='#ff8484')
            label_w=Label(frame_w,text='Doctor\'s info : ',bg='#ff8484',font=('Arial',23)).pack(side='left')
            frame_w.pack(fill='x')
            frame0=Frame(window1,bg='#ff8484')
            waste=Label(frame0,text='\t\t\t',bg='#ff8484').pack(side='left')
            new_doctor=Button(frame0,text="New Doctor's Registration",command=newdoctor,font=('Arial',15))
            new_doctor.pack(side='left')
            waste=Label(frame0,text='\t\t\t\t\t\t\t\t\t\t\t\t\t\t',bg='#ff8484').pack(side='right')
            old_doctor=Button(frame0,text="Old Doctor's Information",command=olddoctor,font=('Arial',15))
            old_doctor.pack(side='right')
            frame0.pack(fill='x')
            frame1_w=Frame(window1,bg='#ff8484')
            waste=Label(frame1_w,text='',bg='#ff8484').pack(side='left')
            frame1_w.pack(fill='x')
            frame1=Frame(window1,bg='#ff8484')
            piechart=Label(frame1,text="To see the Pie Chart Between Doctor's and various Department's click the button : ",bg='#ff8484',font=('Arial',20))
            waste=Label(frame1,text='\t\t',bg='#ff8484').pack(side='left')
            piechart.pack(side='left')
            #waste=Label(frame1,text='\t\t',bg='#ff8484').pack(side='left')
            piechart_b=Button(frame1,text='Pie Chart',command=piechart_g,font=('Arial',14))
            piechart_b.pack(side='left')
            frame1.pack(fill='x')
            frame1_w=Frame(window1,bg='#ff8484')
            waste=Label(frame1_w,text='',bg='#ff8484').pack(side='left')
            frame1_w.pack(fill='x')
            frame_a=Frame(window1,bg='#ff8484')
            analysis=Label(frame_a,text='Hospital Analysis : ',font=('Arial',23),bg='#ff8484')
            analysis.pack(side='left')
            frame_a.pack(fill='x')
            frame1_w=Frame(window1,bg='#ff8484')
            waste=Label(frame1_w,text='',bg='#ff8484').pack(side='left')
            frame1_w.pack(fill='x')
            frame_w1=Frame(window1,bg='#ff8484')
            label_w1=Label(frame_w1,text='Patients\'s info : ',bg='#ff8484',font=('Arial',23)).pack(side='left')
            frame_w1.pack(fill='x')
            frame_p=Frame(window1,bg='#ff8484')
            waste=Label(frame_p,text='\t\t\t\t',bg='#ff8484').pack(side='left')
            pn=Label(frame_p,text="Patient's Phone Number : ",font=('Arial',18),bg='#ff8484')
            pn.pack(side='left')
            pn_e=Entry(frame_p,width=15,fg='#D3D3D3',font=('Arial',18))
            pn_e.bind('<Button-1>',clear)
            pn_e.insert(0,'Ex: 7986410567')
            pn_e.pack(side='left')
            waste=Label(frame_p,text='\t',bg='#ff8484').pack(side='left')
            get=Button(frame_p,text="Get Details",font=('Arial',14),command=get_details)
            get.pack(side='left')
            frame_p.pack(fill='x')
            spaceF=Frame(window1,bg='#ff8484')
            spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
            spaceF.pack()            
            closeF=Frame(window1,bg='#ff8484')
            closeL=Button(closeF,text='Close',font=("Ariel",14),borderwidth=4,command=closeall)
            closeL.pack()
            closeF.pack(fill='x')
            spaceF=Frame(window1,bg='#ff8484')
            spaceL=Label(spaceF,bg='#ff8484').pack(fill='x')
            spaceF.pack(side='bottom')
            resetF=Frame(window1,bg='#ff8484')
            spaceL=Label(resetF,text=' ',font=("Ariel",20),bg='#ff8484')
            spaceL.pack(side='right')
            resetB=Button(resetF,text='Reset Memory',font=("Ariel",18),borderwidth=4,command=reset_memory)
            resetB.pack(side='right')
            resetF.pack(side='bottom',fill='x')
            window1.wm_attributes('-fullscreen','true')
            window1.mainloop()
        home_page()
    else:
        messagebox.showerror('Error','Entered Credentials are incorrect')
window=Tk()
window.configure(bg='#ff8484')
window.geometry('700x650+200+2')
window.resizable(0,0)
window.wm_attributes('-fullscreen','true')
frame0=Frame(window,bg='#ff8484')
l=Label(frame0,text="ADMIN PAGE",font=("Ariel",19),bg='#ff8484')
l.pack()
frame0.pack()
waste=Frame(window,bg='#ff8484')
lab_waste=Label(waste,bg='#ff8484',).pack(fill='x')
waste.pack()
frame1=Frame(window,bg='#ff8484')
username_l=Label(frame1,text='User Name : ',font=("Ariel",16),bg='#ff8484')
username_l.pack(side='left')
username_e=Entry(frame1,width=20,font=("Ariel",16))
username_e.pack(side='left')
frame1.pack()
waste1=Frame(window,bg='#ff8484')
lab_waste=Label(waste1,bg='#ff8484',).pack(fill='x')
waste1.pack()
frame2=Frame(window,bg='#ff8484')
password_l=Label(frame2,text='Password   : ',font=("Ariel",16),bg='#ff8484')
password_l.pack(side='left')
password_e=Entry(frame2,show="*",width=20,font=("Ariel",16))
password_e.bind('<Return>',submit)
password_e.pack(side='left')
frame2.pack()
waste2=Frame(window,bg='#ff8484')
lab_waste=Label(waste2,bg='#ff8484',).pack(fill='x')
waste2.pack()
frame1=Frame(window,bg='#ff8484')
#label_w=Label(frame1,text='                             ',bg='#ff8484').pack(side='left')
button=Button(frame1,text='Submit',font=("Ariel",14),command=submit)
button.pack()
lab_waste=Label(frame1,text='       ',bg='#ff8484',).pack()
button1=Button(frame1,text='Forgot Password',font=("Ariel",14),command=forgot)
button1.pack()
frame1.pack()
frame1_w=Frame(window,bg='#ff8484')
label1_w2=Label(frame1_w,text=' ',bg='#ff8484').pack()
frame1_w.pack(fill='x')
frame2=Frame(window,bg='#ff8484')
button_destroy=Button(frame2,text='Close',font=("Ariel",14),command=destroy)
button_destroy.pack()
frame2.pack()
window.mainloop()
