# Dual IMX477 Camera Setup and Test on Raspberry Pi 5

This README explains how to set up and test two IMX477 HQ cameras on a Raspberry Pi 5.

---

## 1. Setup / Configuration

To enable both cameras, you need to modify `/boot/firmware/config.txt`.

1. Open the config file with a text editor:

```bash
sudo nano /boot/firmware/config.txt
```

2. Add the following lines at the end of the file:

```
[all]
camera_auto_detect=0
dtoverlay=imx477,cam0
dtoverlay=imx477,cam1
```

3. Save the file and reboot the Pi:

```bash
sudo reboot
```

4. **Cleanup:** After testing, you can remove these lines to restore default camera auto-detection.

---

## 2. List detected cameras

To see if both cameras are recognized by the system:

```bash
rpicam-hello --list-cameras
```

You should see two entries like:

```
0 : imx477 ...
1 : imx477 ...
```

---

## 3. Preview each camera

To preview each camera individually:

```bash
rpicam-hello -c 0   # Preview first camera
rpicam-hello -c 1   # Preview second camera
```

---

## 4. Reference links

* Raspberry Pi forum discussion 1: [https://forums.raspberrypi.com/viewtopic.php?t=367328\&utm\_source=chatgpt.com](https://forums.raspberrypi.com/viewtopic.php?t=367328&utm_source=chatgpt.com)
* Raspberry Pi forum discussion 2: [https://forums.raspberrypi.com/viewtopic.php?t=387231\&utm\_source=chatgpt.com](https://forums.raspberrypi.com/viewtopic.php?t=387231&utm_source=chatgpt.com)

---

## 5. Dual camera Python test

The included script `test_2_cam.py` will show a video stream from both cameras simultaneously.
cam 0 (camera a) is situated behind the FBH590-10 Bandpass filter (images will be mostly red). 
cam 1 (camera b) is situated behind the NF594-23 Notch filter (images will contain almost all rgb spectrum).

---

## 6. Picture Taking

Pictures can be taken using the 2_cam_pic.py script. 

IMPORTANT: As of now, due to hardware constraints, both cameras are rotated. Their pictures need to be 
rotated manually before attempting to align them.
 
- cam 0 needs to be rotated 270 degrees clockwise. 
- cam 1 needs to be rotated 90 degrees clockwise. 
 
---

## 7. Video Taking

Videos can be taken using the 2_cam_vid.py script. 
Notice they are saved in a .h264 format!
As with pictures, videos are rotated. 

---
## 8. Image & Video analysis

Some basic analysis is done in ImageAnalysis.ipynb. 
As of now, images don't get rotated, but videos do. 
The analysis works on basic exampls (pics/videos with much light and no filters), but don't work 
well with filters and low light. 


