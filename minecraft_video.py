from colorama import Fore

ascii_art = Fore.LIGHTYELLOW_EX + r"""

        _                                        ___                      
       (_)                                      / __)   _                 
 ____   _  ____   _____   ____   ____  _____  _| |__  _| |_               
|    \ | ||  _ \ | ___ | / ___) / ___)(____ |(_   __)(_   _)              
| | | || || | | || ____|( (___ | |    / ___ |  | |     | |_               
|_|_|_||_||_| |_||_____) \____)|_|    \_____|  |_|      \__)                                                          
                            _      _                                      
                           (_)    | |                                     
                     _   _  _   __| | _____   ___      ____  _____  ____  
                    | | | || | / _  || ___ | / _ \    / _  || ___ ||  _ \ 
                     \ V / | |( (_| || ____|| |_| |  ( (_| || ____|| | | |
                      \_/  |_| \____||_____) \___/    \___ ||_____)|_| |_|
                                                     (_____|
                                                                   
""" + Fore.RESET + "documentation at" + Fore.BLUE + " github.com/xxx\n" + Fore.RESET
print(ascii_art)

import os.path
import time
import PIL.Image
import cv2

palette = [
    0, 0, 0,  # black_concrete
    0, 0, 85,  # crying_obsidian
    44, 46, 143,  # blue concrete
    44, 46, 143,  # blue_wool
    39, 51, 27,  # dried_kelp
    53, 132, 128,  # warped_planks
    41, 85, 139,  # lapis_block
    36, 137, 198,  # light_blue_concrete
    66, 6, 8,  # red_nether_bricks
    98, 47, 69,  # crimson_planks
    100, 32, 156,  # purple_concrete
    127, 44, 175,  # purple_wool
    84, 66, 24,  # jungle_log with sides
    94, 94, 94,  # bedrock
    73, 76, 171,  # blue_concrete_powder
    142, 105, 207,  # block_of_amethyst
    163, 39, 34,  # red_wool
    175, 61, 57,  # red_concrete
    169, 48, 159,  # magenta_concrete
    131, 47, 179,  # purple_concrete_powder
    200, 121, 21,  # pumpkin
    160, 77, 78,  # pink_terracotta
    196, 87, 188,  # magenta_concrete_powder
    199, 42, 40,  # red_mushroom_block
    207, 87, 199,  # magenta_wool
    225, 98, 1,  # orange_concrete
    251, 165, 100,  # shroomlight
    214, 101, 143,  # pink_concrete
    217, 100, 212,  # magenta_glazed_terracotta
    94, 169, 24,  # lime_concrete
    76, 237, 134,  # emerald_block
    37, 153, 161,  # cyan_concrete_powder
    65, 186, 222,  # light_blue_wool
    124, 252, 239,  # diamond_block
    108, 146, 31,  # green_glazed_terracotta
    103, 181, 171,  # prismarine_bricks
    108, 161, 252,  # blue_ice
    185, 133, 35,  # yellow_terracotta
    113, 186, 24,  # lime_wool
    194, 200, 75,  # wet_sponge
    164, 164, 164,  # smooth_stone_block
    173, 202, 254,  # ice
    133, 207, 33,  # lime_glazed_terracotta
    225, 226, 227,  # white_concrete_powder
    241, 175, 21,  # yellow_concrete
    244, 168, 193,  # pink_glazed_terracotta
    249, 198, 43,  # yellow_wool
    255, 234, 78,  # gold_block
    220, 255, 255,  # snow_block
    167, 143, 129,  # white_terracotta
    150, 123, 74,  # stripped_oak_wood
    179, 172, 137,  # smooth_sandstone
    120, 82, 69,  # polished_granite
    99, 99, 99,  # stone
    151, 81, 26,  # red_sand
    72, 88, 35,  # moss_block
    116, 87, 64,  # brown_mushroom_block
    58, 46, 71,  # blue_terracotta
    49, 53, 56,  # gray_wool
    69, 73, 74,  # cyan_terracotta
    60, 39, 27,  # brown_terracotta
    57, 71, 28,  # green_concrete
    69, 136, 110,  # waxed_oxidized_copper
    189, 90, 13,  # orange_wool
    127, 90, 63,  # jungle_planks
    152, 139, 95,  # birch_planks
    104, 75, 53,  # dirt
    121, 74, 61,  # bricks
    111, 111, 105,  # gray_wool
    59, 59, 62,  # smooth_basalt
    73, 27, 27,  # netherrack
    127, 131, 141,  # clay

]

block_palette = [
    "black_concrete",
    "crying_obsidian",
    "blue_concrete",
    "blue_wool",
    "dried_kelp_block",
    "warped_planks",
    "lapis_block",
    "light_blue_concrete",
    "red_nether_bricks",
    "crimson_planks",
    "purple_concrete",
    "purple_wool",
    "jungle_wood",
    "bedrock",
    "blue_concrete_powder",
    "amethyst_block",
    "red_wool",
    "red_concrete",
    "magenta_concrete",
    "purple_concrete_powder",
    "pumpkin",
    "pink_terracotta",
    "magenta_concrete_powder",
    "red_mushroom_block",
    "magenta_wool",
    "orange_concrete",
    "shroomlight",
    "pink_concrete",
    "magenta_glazed_terracotta",
    "lime_concrete",
    "emerald_block",
    "cyan_concrete_powder",
    "light_blue_wool",
    "diamond_block",
    "green_glazed_terracotta",
    "prismarine_bricks",
    "blue_ice",
    "yellow_terracotta",
    "lime_wool",
    "wet_sponge",
    "smooth_stone",
    "packed_ice",
    "lime_glazed_terracotta",
    "white_concrete_powder",
    "yellow_concrete",
    "pink_glazed_terracotta",
    "yellow_wool",
    "gold_block",
    "snow_block",
    "white_terracotta",
    "stripped_oak_wood",
    "smooth_sandstone",
    "polished_granite",
    "stone",
    "red_sand",
    "moss_block",
    "brown_mushroom_block",
    "blue_terracotta",
    "gray_wool",
    "clay_terracotta",
    "brown_terracotta",
    "green_concrete",
    "waxed_oxidized_copper",
    "orange_wool",
    "jungle_planks",
    "birch_planks",
    "dirt",
    "bricks",
    "gray_wool",
    "smooth_basalt",
    "netherrack",
    "clay",
]

cache = []
end_time = time.time()
set_empty = False


def convert_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    converted_image = resized_image.convert("P")
    converted_image.putpalette(palette)
    return resized_image.quantize(palette=converted_image, dither=False)


def frame_script(frame_num, path, command):
    global set_empty
    file = f"{path}\{str(frame_num)}.mcfunction"

    if command:
        with open(file, "a") as f:
            f.write(command + "\n")
    elif not set_empty:
        with open(file, "a") as f:
            f.write("")
        set_empty = True


def frame_script_tick(frame_num, path):
    global end_time
    file = path + r"\tick2.mcfunction"
    tick_command = f"execute if score fps_count fps_count matches {frame_num} run function " \
                   f"minecraft_video:frame_scripts/{frame_num} "

    with open(file, "a") as f:
        f.write(tick_command + "\n")
    end_time = time.time()


def main(video_path, datapack_path, width, make_frames):
    global set_empty
    frame_scripts_path = datapack_path + r"\minecraft_video_player\data\minecraft_video\functions\frame_scripts"
    frames_path = datapack_path + r"\minecraft_video_player\data\minecraft_video\functions\frames"
    frame_count = 1
    total_time = 0
    count = 1
    total_blocks = 0

    if not os.path.isdir(frame_scripts_path):
        print(f"{Fore.RED}incorrect datapack path{Fore.RESET}")
        input("")
        exit()

    if make_frames:
        for f in os.listdir(frames_path):
            os.remove(os.path.join(frames_path, f))
    for f in os.listdir(frame_scripts_path):
        os.remove(os.path.join(frame_scripts_path, f))

    video = cv2.VideoCapture(video_path)

    success, image = video.read()
    if not success:
        print(f"{Fore.RED}can't load video{Fore.RESET}")
        input("")
        exit()
    while success and make_frames:
        if count == 2:
            print("generating jpegs..")
        cv2.imwrite(frames_path + r"\%d.jpg" % count, image)
        success, image = video.read()
        count += 1

    frame_total = len(next(os.walk(frames_path))[2])
    if not frame_total:
        print(f"{Fore.RED}you need to generate jpeg frames{Fore.RESET}")
        input("")
        exit()

    for frame in range(frame_total):
        start_time = time.time()
        try:
            image = (PIL.Image.open(f"{frames_path}\{str(frame_count)}.jpg"))
        except PIL.UnidentifiedImageError:
            print(f"{Fore.RED}can't load frame {frame_count}{Fore.RESET}")
            input("")
            exit()

        converted_image = convert_image(image, width)
        pixels = list(converted_image.getdata())

        x = 0
        z = 0
        for i, pixel in enumerate(pixels, start=1):
            command = f"execute at @e[type=minecraft:armor_stand,tag=pos] run setblock ^{x} ^ ^{z} {str(block_palette[pixel])}"

            if not frame_count == 1:
                if command != cache[i - 1]:
                    cache[i - 1] = command
                    total_blocks += 1
                else:
                    command = ""
            elif frame_count == 1:
                cache.append(command)
                total_blocks += 1

            x += 1
            if x == converted_image.width:
                z += 1
                x = 0

            frame_script(frame_count, frame_scripts_path, command)

        frame_script_tick(frame_count, frame_scripts_path)
        if frame_count == frame_total:
            with open(frame_scripts_path + "\\tick2.mcfunction", "a") as f:
                f.write(
                    f"execute if score fps_count fps_count matches {frame_total} run function minecraft_video:reset_video")
            f.close()

        file_size = os.path.getsize(f"{frame_scripts_path}\{frame_count}.mcfunction")
        total_time += round(end_time - start_time, 2)
        estimated_time = round(((total_time / frame_count) * (frame_total - frame_count)))

        if estimated_time > 59:
            unit = "min"
            estimated_time //= 60
        else:
            unit = "s"

        print(
            f"{Fore.RESET}frame {Fore.LIGHTGREEN_EX}{frame_count}/{frame_total}{Fore.RESET} | "
            f"{Fore.MAGENTA}{round(end_time - start_time, 2)}s{Fore.RESET} | "
            f"{Fore.BLUE}size {file_size // 1000}kB{Fore.RESET} | "
            f"{Fore.LIGHTYELLOW_EX}{total_blocks} blocks{Fore.RESET} | "
            f"{Fore.RED}{estimated_time}{unit} remaining{Fore.RESET}")
        set_empty = False
        frame_count += 1
        total_blocks = 0


def reformat_path(path):
    path = list(path.replace("/", "\\"))
    if path[len(path) - 1] == "\\":
        path[len(path) - 1] = ""
    return "".join(path)


generate_frames = None

while True:
    video_path_input = input("your video path: ")
    if video_path_input:
        break

while True:
    datapack_path_input = input("your datapack path: ")
    if datapack_path_input:
        break

while True:
    try:
        video_block_width = int(input("width in blocks: "))
        break
    except ValueError:
        print("numbers only!")

print("do you want to generate new jpeg frames? ")
while True:
    generate_frames_input = input("(y/n): ")
    if generate_frames_input in ["y", "n"]:
        break
if generate_frames_input == "y":
    generate_frames = True
else:
    generate_frames = False

print("this will delete your previous minecraft video and generated jpegs, do you want to proceed?")

while True:
    proceed = input("(y/n): ")
    if proceed == "y":
        main(reformat_path(video_path_input), reformat_path(datapack_path_input), video_block_width,
             make_frames=generate_frames)
        break
    if proceed == "n":
        break
