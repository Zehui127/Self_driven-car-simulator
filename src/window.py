'''Provides the main simulator window'''
import tkinter.ttk as ttk
import tkinter as tk

from visualiser import SimulatorVisualiser
from config import SimulatorConfig

class SimulatorWindow():
    '''The GUI component of the simulator.
    Contains the :class:`SimulatorVisualiser` (Pygame canvas) in a
    :class:`tk.Frame`.
    The :class:`GUIPane` is displayed alongside it.'''

    def __init__(self, config):
        '''Initialise the window and its components'''
        self.config = config

        self._visualiser = None

        self.root = tk.Tk()
        self.root.wm_title('AUDRI Simulator')
        self.root.style = ttk.Style()
        self.root.style.theme_use('clam')

        res = config.VisualiserSize

        self.root.geometry('{}x{}'.format(
            res[0] +config.GUIWidth,
            res[1]))

        canvas = ttk.Frame(self.root, width=res[0], height=res[1])
        canvas.pack(side=tk.LEFT)

        panel = ttk.Frame(self.root, width=config.GUIWidth, height=res[0])
        panel.pack(side=tk.LEFT)
        button = ttk.Button(panel, text='Placeholder')
        button.place(relwidth=1, relheight=1)

        self.root.bind_all('<KeyPress>', self._keyPress)
        self.root.update()
        self._initVisualiser(canvas)

    def tick(self):
        '''Call visualiser tick frequently'''
        self._visualiser.tick()
        self.root.after(self.config.TickRate, self.tick)

    def shutdown(self, *args):
        '''Runs when the window is about to close'''
        if self._visualiser:
            self._visualiser.shutdown()
        self.root.destroy()

    def _initVisualiser(self, canvas):
        '''Initialises the visualiser component of the window'''
        self._visualiser = SimulatorVisualiser(
            self.config,
            str(canvas.winfo_id()))
        self.root.after(0, self.tick)

    def _keyPress(self, event):
        '''Handles window key press events'''
        self._visualiser.keyPress(event.keysym)

if __name__ == '__main__':
    conf = SimulatorConfig()
    win = SimulatorWindow(conf)
    win.root.mainloop()
