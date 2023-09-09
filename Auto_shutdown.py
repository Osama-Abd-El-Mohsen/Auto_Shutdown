import time
import subprocess
import customtkinter as ctk
import subprocess as sub
import os
import tkinter





color_mode_list = ['Dark', 'Light']

state=0
state1=0

def time_func():
    global Time,minutes,seconds,state1
    try :
        Time=int(input_Entry.get())
        input_Entry.delete(0,ctk.END)
        convert_button.configure(text='pause',fg_color='#2DA572',command =pause)
        time_label2.configure(text_color='#2DA572')
        Time*=60
        minutes = Time // 60
        seconds = Time % 60
        sleep_func()
    except :
        input_Entry.delete(0,ctk.END)
        input_Entry.insert(0,'Error Enter Time In Seconds ')

def resume():
            global state1
            state1=0
            convert_button.configure(text='pause',fg_color='#2DA572',command =pause)
            time_label2.configure(text_color='#2DA572')
            sleep_func()

def pause():
    global state1
    state1=1
    convert_button.configure(text='resume',fg_color='#E06C75',command =resume)
    time_label2.configure(text_color='#E06C75')
    
def mode_func():
        global state
        state=radio_var.get()

def sleep_func():
        global Time,minutes,seconds,state,state1
        if Time>=0 and state1 == 0:
            time_label2.configure(text=f' {minutes:02d}:{seconds:02d} ')
            Time-=1
            minutes = Time // 60
            seconds = Time % 60
            app.after(1000,sleep_func)
        elif Time == -1:
            if state == 0:
                os.system("shutdown /s /t 1")
            elif state == 1:
                os.system("shutdown /r /t 1")


def change_apperance_mode(new_appearance_mode: str):
    ctk.AppearanceModeTracker.set_appearance_mode(new_appearance_mode)



if __name__ == '__main__':

    # config my app
    ctk.ThemeManager.load_theme('green')
    ctk.AppearanceModeTracker.set_appearance_mode('system')
    ctk.deactivate_automatic_dpi_awareness()
    app = ctk.CTk()
    icon_path="\icon.ico"
    app.iconbitmap(os.getcwd()+icon_path)
    app.title("Auto Shutdown\n")
    app.geometry('600x390')
    app.resizable(False, False)
    app.grid_columnconfigure(1, weight=1)

    # opp

    titelfram = ctk.CTkFrame(
        app,
        border_width=0
    )

    setting_frame = ctk.CTkFrame(
        app,
        border_width=0
    )

    entry_frame = ctk.CTkFrame(
        app,
        border_width=0
    )
    

    maker_label = ctk.CTkLabel(
        titelfram,
        width=600,
        text="Auto Shudown",
        font=ctk.CTkFont('Arial', 48, weight='bold'),
        text_color="#2DA572"
    )


    apperance_Label = ctk.CTkLabel(
        setting_frame,
        text="Appearance Mode",
        font=ctk.CTkFont('Arial', 18, weight='bold'),
    )

    owner_frame = ctk.CTkFrame(
        app,
        border_width=0
    )
    
    owner_label1 = ctk.CTkLabel(
        owner_frame,
        text="Made with 💖 By",
        font=ctk.CTkFont('Arial', 20, weight='bold'),
    )
    owner_label2 = ctk.CTkLabel(
        owner_frame,
        text="Osama Abd EL Mohsen",
        font=ctk.CTkFont('Arial', 20, weight='bold'),
        text_color="#2DA572"
    )
    time_label = ctk.CTkLabel(
        entry_frame,
        text='Reaminig Time :',
        font=ctk.CTkFont('Arial', 20, weight='bold')
    )
    
    time_label2 = ctk.CTkLabel(
        entry_frame,
        text=' 00:00 ',
        font=ctk.CTkFont('Arial', 28, weight='bold'),
        text_color="#2DA572"
    )


    input_Entry = ctk.CTkEntry(
        entry_frame,
        placeholder_text="Enter Time In Minutes",
        font=ctk.CTkFont('Arial', 20),
        width=400,
        height=48,
        border_width=0)
    



    convert_button = ctk.CTkButton(
        entry_frame,
        text="Start",
        font=ctk.CTkFont('Arial', 20),
        command=time_func,
        height=48)



    apperance_button = ctk.CTkOptionMenu(
        setting_frame,
        font=ctk.CTkFont('Arial', 20,weight='bold'),
        values=['system','dark','light'],
        command=change_apperance_mode,
        height=48)
    


    radio_var = tkinter.IntVar(value=0)
    
    radio_button1 = ctk.CTkRadioButton(
        entry_frame,
        text='Shutdown',
        variable= radio_var,
        value=0,
        font=ctk.CTkFont('Arial', 18,weight='bold'),
        height=48,
        command=mode_func
    )

    radio_button2 = ctk.CTkRadioButton(
        entry_frame,
        text='Restart',
        variable= radio_var,
        value=1,
        font=ctk.CTkFont('Arial', 18,weight='bold'),
        height=48,
        command=mode_func
    )

    owner_frame.grid(row=4, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

    titelfram.grid(row=0, column=0, padx=10, pady=10,columnspan=3, sticky="ew")
    entry_frame.grid(row=1, column=0, padx=(10, 10),columnspan=3,  pady=(10, 10), sticky="nsew")
    setting_frame.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")


    maker_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    input_Entry.grid(row=2, column=0, padx=(10,10), pady=(10,10), sticky="nsew")

    time_label.grid(row=3, column=0, padx=(10,10), pady=(10,10), sticky="w")
    time_label2.grid(row=3, column=0, padx=(170,10), pady=(10,10), sticky="w")


    convert_button.grid(row=2, column=4, padx=(10, 10), pady=(10, 10))

    radio_button1.grid(row=3, column=0, padx=(10, 10), pady=(10, 10), sticky="e")
    radio_button2.grid(row=3, column=4, padx=(10, 10), pady=(10, 10), sticky="w")

    apperance_Label.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="we")
    apperance_button.grid(row=5, column=0, padx=(10, 10),pady=(10, 10), sticky="we")

    owner_label1.grid(row=4, column=1, padx=(60, 10), pady=(30, 0), sticky="nsew")
    owner_label2.grid(row=5, column=1, padx=(60, 10), pady=(0, 10), sticky="nsew")

    

    app.mainloop()
