import os
from tqdm import tqdm

def jsp():

    total_iterations = 10000

    progress_bar = tqdm(total=total_iterations, desc="Creating Files")

    for i in range(total_iterations):
        progress_bar.update(1)
        f = open(f"C:/Users/matth/OneDrive/Documents/mort/virus_{i}.txt","w")
        f.close()
    progress_bar.close()
jsp()