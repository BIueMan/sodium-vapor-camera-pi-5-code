# Dual IMX477 Camera Test on Raspberry Pi 5

This README explains how to quickly test two IMX477 HQ cameras on a Raspberry Pi 5 using terminal commands.

---

## 1. List detected cameras

To see if both cameras are recognized by the system:

```bash
rpicam-hello --list-cameras
```

You should see two entries like:

```
0 : imx477 ...
1 : imx477 ...
```

## 2. Preview each camera

To preview each camera individually:

```bash
rpicam-hello -c 0   # Preview first camera
rpicam-hello -c 1   # Preview second camera
```

## 3. Reference links

* Raspberry Pi forum discussion 1: [https://forums.raspberrypi.com/viewtopic.php?t=367328\&utm\_source=chatgpt.com](https://forums.raspberrypi.com/viewtopic.php?t=367328&utm_source=chatgpt.com)
* Raspberry Pi forum discussion 2: [https://forums.raspberrypi.com/viewtopic.php?t=387231\&utm\_source=chatgpt.com](https://forums.raspberrypi.com/viewtopic.php?t=387231&utm_source=chatgpt.com)

## 4. Dual camera Python test

The included script `test_2_cam.py` will show a video stream from both cameras simultaneously.
