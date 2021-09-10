import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Tk + Matplotlib")
        self.master.resizable(0, 0)
        
        self.amp = tk.DoubleVar(value=6)
        self.freq = tk.IntVar(value=1)
        self.var_color = tk.IntVar()
        self.amp_max = 12
        self.freq_max = 20
        self.t_max = 3
        
        self.plot_colors = {0: 'blue', 1: 'red', 2: 'green', 3: 'magenta'}
        
        # ------------------------------ Frames -------------------------------------
        frm = tk.Frame(self.master)
        frm.pack()
        
        frm1 = tk.Frame(frm)
        frm1.pack(padx=10, pady=10)
        frm2 = tk.Frame(frm)
        frm2.pack(padx=10, pady=10)
        frm3 = tk.Frame(frm)
        frm3.pack(padx=10, pady=10)
        
        frmAmp = tk.LabelFrame(frm2, text="Amplitud")
        frmFreq = tk.LabelFrame(frm2, text="Frecuencia")
        
        frmAmp.pack(side=tk.LEFT, padx=10, pady=10, ipadx=6)
        frmFreq.pack(side=tk.LEFT, padx=10, pady=10, ipadx=6)
        
        frmColor = tk.LabelFrame(frm3, text="Color")
        frmColor.pack(padx=10, pady=10, ipadx=2)
        
        # ------------------- Matplotlib initial plot ---------------------------
        self.fig, self.ax = plt.subplots(figsize=(6, 4), facecolor='#F0F0F0')
        self.t = np.linspace(0, self.t_max, 50 * self.freq_max)
        y = self.amp.get() * np.sin(2 * np.pi * self.freq.get() * self.t)
        self.line, = self.ax.plot(self.t, y, color=self.plot_colors[self.var_color.get()])
        self.ax.grid(linestyle=':')
        self.ax.set_xlim([0, self.t_max])
        self.ax.set_ylim([-self.amp_max - 3, self.amp_max + 3])
        self.ax.set_title(f"Onda senoidal @ {self.freq.get()}Hz")
        self.ax.set_xlabel("Tiempo [seg]")
        self.ax.set_ylabel("Amplitud")
        
        # -------------------------------- frm1 ---------------------------------
        self.graph = FigureCanvasTkAgg(self.fig, master=frm1)
        self.graph.get_tk_widget().pack(expand=True, fill=tk.BOTH)
        
        # -------------------------------- frmAmp --------------------------------
        self.btnAmp_Low = tk.Button(frmAmp, text="<<", font="Arial 12", width=4, 
                                    command=self.set_amp_low)
        self.btnAmp_High = tk.Button(frmAmp, text=">>", font="Arial 12", width=4,
                                     command=self.set_amp_high)
        
        self.btnAmp_Low.grid(row=0, column=0, padx=10, pady=10)
        self.btnAmp_High.grid(row=0, column=1, padx=10, pady=10)
        
        # -------------------------------- frmFreq -------------------------------
        self.btnFreq_Low = tk.Button(frmFreq, text="<<", font="Arial 12", width=4, 
                                     command=self.set_freq_low)
        self.btnFreq_High = tk.Button(frmFreq, text=">>", font="Arial 12", width=4,
                                      command=self.set_freq_high)
        
        self.btnFreq_Low.grid(row=0, column=0, padx=10, pady=10)
        self.btnFreq_High.grid(row=0, column=1, padx=10, pady=10)
        
        # -------------------------------- frmColor -------------------------------
        self.rdoBlue = tk.Radiobutton(frmColor, text="Azul", variable=self.var_color, value=0,
                                      command=self.set_plot_color)
        self.rdoRed = tk.Radiobutton(frmColor, text="Rojo", variable=self.var_color, value=1,
                                     command=self.set_plot_color)
        self.rdoGreen = tk.Radiobutton(frmColor, text="Verde", variable=self.var_color, value=2,
                                       command=self.set_plot_color)
        self.Magenta = tk.Radiobutton(frmColor, text="Magenta", variable=self.var_color, value=3, 
                                      command=self.set_plot_color)
        
        self.rdoBlue.grid(row=0, column=0, padx=10, pady=5)
        self.rdoRed.grid(row=0, column=1, padx=10, pady=5)
        self.rdoGreen.grid(row=0, column=2, padx=10, pady=5)
        self.Magenta.grid(row=0, column=3, padx=10, pady=5)
        
    
    def set_amp_low(self):
        if self.amp.get() > 0:
            self.amp.set(self.amp.get() - 0.25)
            self.draw_graph()
    
    
    def set_amp_high(self):
        if self.amp.get() < self.amp_max:
            self.amp.set(self.amp.get() + 0.25)
            self.draw_graph()
            
    
    def set_freq_low(self):
        if self.freq.get() > 1:
            self.freq.set(self.freq.get() - 1)
            self.draw_graph()
    
    
    def set_freq_high(self):
        if self.freq.get() < self.freq_max:
            self.freq.set(self.freq.get() + 1)
            self.draw_graph()
        
        
    def set_plot_color(self):
        self.line.set_color(self.plot_colors[self.var_color.get()])
        self.graph.draw()
        
        
    def draw_graph(self):
        self.line.set_ydata(self.amp.get() * np.sin(2 * np.pi * self.freq.get() * self.t))
        self.ax.set_title(f"Onda senoidal @ {self.freq.get()}Hz")
        self.graph.draw()
    
    
        
root = tk.Tk()
App(root)
root.mainloop()
