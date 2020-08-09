#!/usr/bin/env python
# coding: utf-8

# In[3]:


# #installing important libraries uncomment libraries to install them.(works on jupyter notebook only.)

# !pip install clipboard
# !pip install pyshorteners


# In[1]:


from tkinter import *
import pyshorteners
import clipboard


window = Tk()

#set deafault window size
window.geometry("500x250") # width x height

# make window not resizable 
window.resizable(False,False)  # not resizable in x and y 

# app title
window.title("URL Chota Karne Ki Python Technique")

window.configure(bg='#015788')



# url entry
url_input = Entry(window, font=("Helvetica","16"),width=35)
url_input.grid(row=5, column=3,pady=10,padx=10)


#label shortened url
str_url = StringVar(window)

shortened_url = Label(window, textvariable=str_url, font=("Helvetica","16"), fg="#fff", bg="#1abc9c")
shortened_url.grid(row=10, column=3,pady=10)


# copy short url function
def copy_short_url():
  try:
    clipboard.copy(str_url.get())
    print("Url copied successfully !!")
  except:
    str_url.set("Something wrong try again !!")

# Copy short url button
copy_btn = Button(window, text="Copy", bg="#34495e", fg="#fff", font=("Helvetica","12"), command=copy_short_url)
copy_btn.grid(row=3, column=3, pady=10, padx=10)



#short url function
def short_url():
  try:
    s = pyshorteners.Shortener()
    url = url_input.get()
    final_result = s.tinyurl.short(url)
    str_url.set(final_result)
    url_input.delete(0, END) # clear input 
  except:
    str_url.set("Enter url please !! ")


#click button to short url
btn = Button(window, text="Short Url", padx=8, pady=10, bg="#2ecc71", fg="#fff", font=("Helvetica","16"), activebackground="#16a085", command=short_url)
btn.grid(row=9, column=3)

window.mainloop()

