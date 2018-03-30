import tkinter as tk
class App(tk.Tk):
     def __init__(self):
         super().__init__()
         self.menu = tk.Menu(self, tearoff=0, postcommand=self.enable_selection)
         self.menu.add_command(label="Cut", command=self.cut_text)
         self.menu.add_command(label="Copy", command=self.copy_text)
         self.menu.add_command(label="Paste", command=self.paste_text)
         self.menu.add_command(label="Delete", command=self.delete_text)	

         self.text = tk.Text(self, height=10, width=50)
         self.text.bind("<Button-3>", self.show_popup)
         self.text.pack()
     def enable_selection(self):
         state_selection = tk.ACTIVE if self.text.tag_ranges(tk.SEL) else tk.DISABLED
         state_clipboard = tk.ACTIVE
		 
         try:
             self.clipboard_get()
         except tk.TclError:
             state_clipboard = tk.DISABLED
			 
         self.menu.entryconfig(0, state=state_selection) # Cut
         self.menu.entryconfig(1, state=state_selection) # Copy
         self.menu.entryconfig(2, state=state_clipboard) # Paste
         self.menu.entryconfig(3, state=state_selection) # Delete	


		 
     def show_popup(self, event):
        self.menu.post(event.x_root, event.y_root)

     def cut_text(self):
        self.copy_text()
        self.delete_text()

     def copy_text(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.clipboard_clear()
            self.clipboard_append(self.text.get(*selection))

     def paste_text(self):
        self.text.insert(tk.INSERT, self.clipboard_get())

     def delete_text(self):
        selection = self.text.tag_ranges(tk.SEL)
        if selection:
            self.text.delete(*selection)


if __name__ == "__main__":
    app = App()
    app.mainloop()

             
		 