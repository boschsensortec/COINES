# Media Transfer Protocol (MTP) firmware for Application Board 3.0

[comment]: <> (This is not exactly as the pdf)

The external memory chip W25M02/W25N02 on APP3.0 is based on NAND flash.

FAT filesystem on NAND flash memory results in a complicated solution which uses of lot of RAM.
Moreover use of FAT without Flash Translation Layer (to save RAM) wears out NAND flash with frequent usage.
Hence the choice of [FlogFS](https://github.com/conservify/FLogFS), a filesystem optimized for use with NAND flash.

But the use of `FlogFS`, presents a new problem 'Filesystem access from PC via USB'.
Use of `FlogFS` with USB Mass Storage protocol is not possible because operating system can't recognize `FlogFS` as a valid filesystem.

Use of custom protocol to do filesystem operations would mean re-inventing the wheel and a lot of effort.
User also would not have the same experience as with USB Mass Storage.

Solution was to go with the "Media Transfer Protocol" developed initially by Microsoft for Portable Devices like MP3 players.
Starting from Android Kitkat (v4.4), MTP is the only way to access files on an Android device since the whole flash memory (included user storage space) uses filesystems like ext4, YAFFS, F2FS, etc.

Files in APP3.0 board's NAND flash memory can be viewed using the USB MTP firmware.

Supported on Windows, Linux, Android (via USB OTG) and macOS.

<figure markdown>

  ![Image: MTP Windows](mtp_windows.png){ width="700"}
</figure>

<figure markdown>

  ![Image: MTP Ubuntu Nautilus](mtp_ubuntu_nautilus.png){ width="700"}
</figure>

<figure markdown>

  ![Image: MTP Android 2](mtp_android_2.png){ width="700"}
</figure>

<figure markdown>

  ![Image: MTP Android 3](mtp_android_3.png){ width="700"}
</figure>
