from tkinter import *
import main

# codes = ["005930", "000660", "030200", "001040", "051910", "006400", "035720", "035420", "005380", "000150"]

root = Tk()
root.title('Stock')
root.geometry('800x700')

def showStock(code):
    stock = Label(root, text = main.codes[code])
    stock.place(x = 0, y = 50)
    main.get_stock(main.codes[code])

for i in range(len(main.codes)):
    button = Button(root, text = main.codes[i], overrelief = 'solid', command = lambda j = i:showStock(j))
    button.grid(row = 1, column = i)


root.mainloop()