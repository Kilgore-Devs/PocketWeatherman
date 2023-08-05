import tkinter as tk


def celsius():  # defines fx to covert Fahrenheit to Celsius output weather conditions
    degrees_fahrenheit = float(fahrenheit_entry.get())  # gets the F temp from entry field as a float
    temp_celsius = (degrees_fahrenheit - 32) / 1.8  # converts F to Celsius provided by formula
    celsius_var.set("It's {0:.2f} degrees Celsius.".format(temp_celsius))  # sets temp tp Celsius
#  The following if statements determine weather condition based on temperature-might change to ranges
    if temp_celsius >= 32:
        condition_var.set("Why is it so hot?!")
    elif 25 < temp_celsius < 32:
        condition_var.set("Bit warm out, isn't it?")
    elif 15 < temp_celsius <= 25:
        condition_var.set("Ahh, the temperature is just right! :)")
    elif 0 < temp_celsius <= 15:
        condition_var.set("Bit nippy, isn't it?")
    elif -100 < temp_celsius <= 0:
        condition_var.set("The bone chilling pain, let's get out of here and head south, preferably by a beach!")
    else:
        condition_var.set("Thank you for using the app!")


root = tk.Tk()  # creates a window

root.title("Pocket Weatherman")  # titles the window
# Set window size and have it centered on screen on next 5 lines
window_width = root.winfo_screenwidth() // 2
window_height = root.winfo_screenheight() // 2
x = (root.winfo_screenwidth() - window_width) // 2
y = (root.winfo_screenheight() - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

root.configure(bg='light blue')  # sets the bg color
from PIL import Image, ImageTk  # I think this belongs in the beginning of the code imports image proc lib

image = Image.open("clouds.jpg")  # Loads the image file

image = image.resize((window_width, window_height),)  # Resize the image to fit the window size

tk_image = ImageTk.PhotoImage(image)  # Create a Tkinter-compatible image object

# Create a label with the background image
background_label = tk.Label(root, image=tk_image)
background_label.place(relwidth=1, relheight=1)
celsius_var = tk.StringVar()
condition_var = tk.StringVar()
fahrenheit_label = tk.Label(root, text="What's the temperature in Fahrenheit?",
                            bg='light blue', fg='black', font=('Arial', 12))  # Is this is causing the white vert line?
fahrenheit_label.pack()
fahrenheit_entry = tk.Entry(root)  # creates entry field fo the Fahrenheit temp
fahrenheit_entry.pack()
celsius_button = tk.Button(root, text="Convert to Celsius", command=celsius)  # creates button to init conversion to Cel
root.bind('<Return>', lambda event=None: celsius())
celsius_button.pack()
# Following line creates the label to display temp in Celsius
celsius_label = tk.Label(root, textvariable=celsius_var, bg='white', fg='black',
                         font=('Arial', 12))
celsius_label.pack()

condition_label = tk.Label(root, textvariable=condition_var, bg='white', fg='black',
                           font=('Arial', 12))  # Creat and pack label to display weather
condition_label.pack()

root.mainloop()  # Start the main loop of the app
