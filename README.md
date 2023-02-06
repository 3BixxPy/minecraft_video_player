# Minecraft Video Player


#updated version [here](https://github.com/3BixxPy/mcvideo2) \
converts mp4 to minecraft (71 colors supported) \
[Python code](https://github.com/3BixxPy/minecraft_video/tree/code) \
[Video](https://www.youtube.com/watch?v=KN-YvopMdOs)

![](https://i.imgur.com/AZUGe8f.png)

# Download At
- download link => [Media Fire](https://www.mediafire.com/file/rl1vh684x6lm7lu/minecraft_video_player_1.0.1.rar/file) fixed!
- Your anti-virus might detect this file as a HackTool \
 Hacktools can be used to patch or "crack" some software so it will run without a valid license or genuine product key

# Setting Up The Video
- Go to minecraft_video.exe located in your datapack folder \
and set a video path (C:\videos\video.mp4), datapack path (minecraft\saves\world\datapacks) \
set a width in blocks I recomend anything from 64-100 \
if you didn't generate any jpegs set generate jpegs, they will be located in ```minecraft_video_player\data\minecraft_video\functions\frames```

# Usage
- Reload the datapack ```/reload```
- First you need to set a position for the video with ```/function minecraft_video:set_pos```
- Set the video speed ```/scoreboard players set fps fps X``` X can be any whole number from 1
- Then start the video with ```/function minecraft_video:start_video```
- Use ```/function minecraft_video:pause_video``` to pause and ```/function minecraft_video:reset_video``` to reset
- ```/execute at @e[tag=pos] run tp @e[tag=pos] ~ ~ ~ Xrot Yrot``` to rotate the video

# Included Test Video
- There is a rar file located in datapacks\minecraft_video_player called Bad_Apple
- Make sure the folder minecraft_video\functions\frame_scripts is empty
- And extract Bad_Apple.rar in the frame_scripts
