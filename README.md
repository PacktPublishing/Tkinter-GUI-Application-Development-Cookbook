# Tkinter GUI Application Development Cookbook


This is the code repository for [Tkinter GUI Application Development Cookbook](https://www.packtpub.com/web-development/tkinter-gui-application-development-cookbook?utm_source=GitHub&utm_medium=repo&utm_campaign=9781788622301), published by [Packt](https://www.packtpub.com). It contains all the supporting project files necessary to work through the book from start to finish.

## About the Book

Tkinter GUI Application Development Cookbook starts with an overview of Tkinter classes and at the same time provides recipes for basic topics, such as layout patterns and event handling. Next, we cover how to develop common GUI patterns, such as entering and saving data, navigating through menus and dialogs, and performing long-running actions in the background.You can then make your apps leverage network resources effectively and perform graphical operations on a canvas and related tasks such as detecting collisions between items. Finally, this book covers using themed widgets, an extension of Tk widgets that have a more native look and feel. Finally, this book covers using the canvas and themed widgets.

By the end of the book, you will have an in-depth knowledge of Tkinter classes, and will know how to use them to build efficient and rich GUI applications.

## Instructions and Navigations
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter01.



The code will look like the following:
```

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn = tk.Button(self, text="Click me!",
                             command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print("Hello, Tkinter!")

if __name__ == "__main__":
    app = App()
    app.title("My Tkinter app")
    app.mainloop()


```

## Related Products
* [Tkinter GUI Application Development Blueprints - Second Edition](https://www.packtpub.com/application-development/tkinter-gui-application-development-blueprints-second-edition?utm_source=GitHub&utm_medium=repo&utm_campaign=9781788837460)

* [Tkinter GUI Application Development Projects [Video]](https://www.packtpub.com/application-development/tkinter-gui-application-development-projects-video?utm_source=GitHub&utm_medium=repo&utm_campaign=9781787280151)

* [Python GUI Programming Cookbook - Second Edition](https://www.packtpub.com/application-development/python-gui-programming-cookbook-second-edition?utm_source=GitHub&utm_medium=repo&utm_campaign=9781787129450)








