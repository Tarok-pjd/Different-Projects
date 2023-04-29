#import tkinter
import tkinter

#class: controll
class ConWin:
    def __init__(self, name, rowpos, colpos, root=tkinter.Tk()):
        self.name = name #what will be displayed next to the lights
        self.rowposition = rowpos #used to position the labels in the rows correctly
        self.columnpos = colpos #used to position the labels in the columns correctly
        self.rootwin = root #the root window
        self.label() #creates one label with the given data
        self.create_light() #creates the light next to the label

    def label(self):
        lbs = tkinter.Label(self.rootwin, text=self.name)
        lbs["height"] = 5
        lbs["width"] = 20
        lbs["borderwidth"] = 5
        lbs["relief"]= "ridge"
        
        lbs.grid(row=self.rowposition, column=self.columnpos, columnspan=2, sticky="w")
        
    def create_light(self):
        self.light = tkinter.Label(self.rootwin)
        self.light["height"] = 3
        self.light["width"] = 7
        self.light["highlightthickness"] = 2
        self.light["highlightbackground"] = "#7D8298"
        self.light["bg"] = "#FF0000"
        self.columnpos += 2 #otherwise the light would cover the label

        self.light.grid(row=self.rowposition, column=self.columnpos, sticky="e")
        self.columnpos -= 2 #this has to be reversed or everything is off
        

    def check(self):
        self.light["bg"] = "#00FF00"
    
    def change_name(self, new_name):
        self.name = new_name
        
    @staticmethod
    def auto_generate_conwin(number: int, value_per_row: int =5):
        i = 0
        r_var = 0 #var for the position in row
        c_var = 0 #var for the position in column
        lbl_list = []
        while i < number:
            while r_var < value_per_row:
                if i >= number:
                    break
                lbl_list.append(ConWin("Label Nr." + str(i), r_var, c_var))
                r_var += 1
                i += 1
            r_var = 0
            c_var += 5
        
        return lbl_list


#for test purposes
if __name__ == '__main__':
    ConWin.auto_generate_conwin(10)

#the auto generate function could take a list of names each signal and parse and name them according to the list
#in addition the auto generate function is at the moment not capable of setting an own root window
#the light function could be called in the label function
#every label needs one class that is probably not very efficient