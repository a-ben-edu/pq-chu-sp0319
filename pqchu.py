## Main file for user interface
import tkinter as tk
from tkinter import N, W, E, S
from tkinter import ttk
from polynomial import Poly2

class PQApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
    
        self.l_a:tk.StringVar = tk.StringVar()
        self.l_b:tk.StringVar = tk.StringVar()
        self.l_c:tk.StringVar = tk.StringVar()
        self.r_a:tk.StringVar = tk.StringVar()
        self.r_b:tk.StringVar = tk.StringVar()
        self.r_c:tk.StringVar = tk.StringVar()
        self.answertext = tk.StringVar()
        
        self.init_widgets()
        self.grid()

    def init_widgets(self):
        mainframe = ttk.Frame(self, padding=(3, 3, 12, 12))
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.left_a_entry = tk.Entry(mainframe, width=5, textvariable=self.l_a)
        self.left_a_entry.insert(0,'0')
        self.left_a_entry.grid(column=0,row=1)
        self.left_a_label = ttk.Label(mainframe, text="x^2 +").grid(column=1,row=1)

        self.left_b_entry = tk.Entry(mainframe, width=5, textvariable=self.l_b)
        self.left_b_entry.insert(0,'0')
        self.left_b_entry.grid(column=2,row=1)
        self.left_b_label = ttk.Label(mainframe, text="x +").grid(column=3,row=1)

        self.left_c_entry = tk.Entry(mainframe, width=5, textvariable=self.l_c)
        self.left_c_entry.insert(0,'0')
        self.left_c_entry.grid(column=4,row=1)
        self.left_c_label = ttk.Label(mainframe, text=" = ").grid(column=5,row=1)

        self.right_a_entry = tk.Entry(mainframe, width=5, textvariable=self.r_a)
        self.right_a_entry.insert(0,'0')
        self.right_a_entry.grid(column=6,row=1)
        self.right_a_label = ttk.Label(mainframe, text="x^2 +").grid(column=7,row=1)

        self.right_b_entry = tk.Entry(mainframe, width=5, textvariable=self.r_b)
        self.right_b_entry.insert(0,'0')
        self.right_b_entry.grid(column=8,row=1)
        self.right_b_label = ttk.Label(mainframe, text="x +").grid(column=9,row=1)

        self.right_c_entry = tk.Entry(mainframe, width=5, textvariable=self.r_c)
        self.right_c_entry.insert(0,'0')
        self.right_c_entry.grid(column=10,row=1)

        self.quit_button = tk.Button(self, text='Exit', command=self.quit)
        self.quit_button.grid(column=0, row=2, sticky=(W,S))

        self.answer_label = tk.Label(mainframe, textvariable=self.answertext).grid(column=2,row=2, columnspan=7)
        self.answertext.set("Enter equation an press solve")
        
        self.solve_button = tk.Button(self, text='Solve', command=self.solve)
        self.solve_button.grid(column=1, row=2 )

    def read_fields(self)-> tuple[Poly2, Poly2]:
        left_poly = Poly2(a=float(self.left_a_entry.get()), b=float(self.left_b_entry.get()), c=float(self.left_c_entry.get()))      
        right_poly = Poly2(a=float(self.right_a_entry.get()), b=float(self.right_b_entry.get()), c=float(self.right_c_entry.get()))
        return (left_poly, right_poly)
    
    def solve(self):
        left_poly, right_poly = self.read_fields()
        left_poly = left_poly-right_poly
        right_poly = 0
        left_poly = left_poly * left_poly.a**-1
        
        x1 = -1*left_poly.b/2 + left_poly.b**2/4-left_poly.c



        self.answertext.set(str(x1))

        ##NEEDS CODE TO SOLVE EQUATION HERE. CAN YOU DO IT?

def main():
    app = PQApp()
    app.master.title('PQ-chu')
    app.mainloop()

if __name__=='__main__':
    main()