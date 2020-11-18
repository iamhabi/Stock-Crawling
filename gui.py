from tkinter import *
import main

# codes = ["005930", "000660", "030200", "001040", "051910", "006400", "035720", "035420", "005380", "000150"]

root = Tk()
root.title('Stock')
root.geometry('800x700')

infoWindow = Frame(root)
infoWindow.grid(row = 2)

def clear():
    winList = infoWindow.grid_slaves()

    for i in winList:
        i.destory()

# Show Info
def showStock(code):
    l = main.get(main.codes[code])
    stock = Label(root, text = l[0])
    stock.grid(row = 3)

    stock = Label(root, text = l[1])
    stock.grid(row = 4)

    stock = Label(root, text = "10 days")
    stock.grid(row = 6)

    for i in range(len(l[2])):
        for j in range(len(l[2][i])):
            stock = Label(root, text = l[2][i][j])
            stock.grid(row = 7 + i, column = j)

    stock = Label(root, text = "news")
    stock.grid(row = 18)
    
    for i in range(len(l[3])):
        stock = Label(root, text = l[3][i][0])
        stock.grid(row = 19 + i, columnspan = 5, sticky = 'w')

        stock = Label(root, text = l[3][i][1])
        stock.grid(row = 19 + i, column = 6, columnspan = 3, sticky = 'w')


for i in range(len(main.codes)):
    button = Button(root, text = main.codes[i], overrelief = 'solid', command = lambda j = i:showStock(j))
    button.grid(row = 1, column = i)

root.mainloop()