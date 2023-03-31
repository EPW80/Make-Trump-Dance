import os

output_folder = "frames"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

from PIL import Image

def gif_to_frames(gif_file, output_folder):
    img = Image.open(gif_file)
    frames = []

    for i in range(img.n_frames):
        img.seek(i)
        frame = img.copy()
        frame_file = f"{output_folder}/frame_{i}.png"
        frame.save(frame_file)
        frames.append(frame_file)

    return frames

gif_file = "videogame/data/trumpgif.gif"
output_folder = "frames"
frames = gif_to_frames(gif_file, output_folder)
