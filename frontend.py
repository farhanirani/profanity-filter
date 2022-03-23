from tkinter import *
from backend import *


def printInput():

    input_from_textfield = inputtxt.get()

    if input_from_textfield:

        profane_percent, profane_true_or_false_all_words, filtered_text = backend(
            input_from_textfield)

        # red and green bar that represents profanity severity level
        root.create_rectangle(150, 340, 650, 360, fill='lightgreen')
        root.create_rectangle(150, 340, 150 + 500 *
                              profane_percent / 100, 360, fill='red')

        # updating the text that shows profanity level
        result_txt = str(profane_percent) + '% Profane'
        result.config(text=result_txt)

        # printing filtered text
        result_text.config(text=filtered_text)


root = Tk()

root.title('Profanity Filter')
root.geometry("800x600")
root = Canvas(root, width=800, height=600)
root.pack()

# Title text
title = Label(text='Profanity Filter',
              font='Times 30 italic bold', fg='darkblue')
title.place(relx=0.5, rely=0.1, anchor='center')

# Input box
inputtxt = Entry(root, width=40, font='Times 16 italic bold', justify='center')
inputtxt.place(relx=0.5, rely=0.3, anchor='center')

# Submit button
submitButton = Button(root, text="Check Profanity",
                      font='Times 16 italic bold', fg='darkblue', command=printInput)
submitButton.place(relx=0.5, rely=0.45, anchor='center')

# Result text
result = Label(root, font='Times 18 italic bold', fg='darkblue')
result.place(relx=0.5, rely=0.7, anchor='center')

# Filtered text
result_text = Label(root, font='Times 18 italic bold', fg='darkblue')
result_text.place(relx=0.5, rely=0.85, anchor='center')


mainloop()
