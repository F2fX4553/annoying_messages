#program tsjile mwadf
from tkinter import *
from tkinter import ttk
from  tkinter import messagebox
from  tkinter import IntVar
#from sendmesag import apps
import pyautogui
import time


frm = Tk()
# hdo l3fayse li ndi mn3ndhom lalwan o lhjm ta3 l5et o bzaf 3fayse
fnt       = 'none 30 bold'
bg        = '#192734' # lonse ta3 lforma
bgtxt     = '#1DA1F2'
fg        = '#1DA1F2'
fw        = 900 #####################################################
fh        = 500                                                     #
x         = (frm.winfo_screenwidth()  - fw ) / 2                    # hdi lhjme ta3 lforma
y         = (frm.winfo_screenheight() - fh ) / 2                    #
pad       = 10 ######################################################
frm.resizable(width=0, height=0)                                                                   #
                                                                    #
frm.geometry('%dx%d+%d+%d' %(fw , fh , x , y))                      # tab3a lhjme lforma
frm.title('Annoying messages')                                     #
frm.iconbitmap('images/ninja.ico')
frm.config(bg = bg)                                                 #
#####################################################################
Label(frm,text = 'Sending a Message',bg = '#192734',fg = 'white',font = fnt).pack(pady = pad)  # hdi text li ybane mlfo9 chro kima welcom
fram = Frame(frm,bg = bg)                                                   # hdi background ta3o
fram.pack(pady = pad)                                                       #
#############################################################################
Label(fram,text = 'The number of times',bg = bg , fg = fg , font = fnt).grid(row = 0 , column = 0)   #
Label(fram,text = 'Text Message',bg = bg , fg = fg , font = fnt).grid(row = 1 , column = 0)   # text li y5rojli 9dam mourba3at ta3 nese
Label(fram,text = 'Time Slip',bg = bg , fg = fg , font = fnt).grid(row = 2 , column = 0)#
########################################################################################
svnumber   = IntVar()                                                                #
svMessage  = StringVar()                                                                #
svTime     = IntVar()                                                                # lmoud5alat ta3 code and name and address
txtcode    = Entry(fram ,bg = "white" , fg = fg , font = fnt , textvariable  = svnumber)    #
txtname    = Entry(fram ,bg = "white" , fg = fg , font = fnt , textvariable  = svMessage)    #
txtaddress = Entry(fram ,bg = "white" , fg = fg , font = fnt , textvariable  = svTime) #
#########################################################################################
txtcode.grid(row = 0 , column = 1 , pady = pad)
txtname.grid(row = 1 , column = 1 , pady = pad)
txtaddress.grid(row = 2 , column = 1 , pady = pad)

def getValue(var):
  try:
    return var.get()
  except:
    return None

def creat():
  numb = getValue(svnumber)
  name = getValue(svMessage)
  tim = getValue(svTime)
  if(numb == None or numb <= 0):
    messagebox.showerror("Error","The number of messages mest be not 0")
  elif(name == ""):
    messagebox.showerror("Error","Please enter message text")
  elif(tim == None or tim <= 0):
    messagebox.showerror("Error","The sleep time must be not 0")
  else:
    for x in range(numb):
      fram.update()
      pyautogui.typewrite(name)
      time.sleep(tim)
      pyautogui.press("enter")

      if numb == x:
          break

      svnumber.set("")
      svMessage.set("")
      svTime.set("")
    messagebox.showinfo("", "operation accomplished successfully 100%")








btnstyle = ttk.Style() ##################################################################
btnstyle.configure('TButton',font = fnt , fg = "white" ,pady = pad , padding = pad)                   #
ttk.Button(frm , text = 'Click Here To Get Started', command = creat).pack(pady = pad)                                  # hdo lbouton li y5dmli file jdide o li y5roj mlbrnamje
ttk.Button(frm , text = 'exit now',command = frm.destroy).pack(pady = pad) #####################################################

frm.mainloop()
