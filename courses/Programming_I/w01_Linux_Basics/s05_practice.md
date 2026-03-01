
[Back](https://www.bioinfo-lab.com/courses/Programming_I/w01_Linux_Basics/)

<br>

---------------------

### Important

Please create a new PPT file, document every subsequent step you take with screenshots, save it as a PDF upon completion of all steps, and submit it to the "Weekly Report Assignment" on Moodle by 23:59 this Sunday. 

This is an important part of your "General Performance". Please ensure timely submission!!!


<br>

---------------------

### 1. Download & Install Termius

* Local Network: IP address on the board (http://IP:8000)

* Udisk

* Baidu Cloud Disk: [click](https://pan.baidu.com/s/10TpxA_oQHuVs4DL2qPQUdg?pwd=biuh) 

* Official Website: [https://termius.com/index.html](https://termius.com/index.html)

* Iphone & Android Phones: Download from App Store


<br>

---------------------

### 2. Register a Termius account.

<b> Termius is FREE! Do NOT subscribe! Use the free version directly. </b>

<br>

---------------------

### 3. Log into the remote Linux Server.

Linux Server:

IP: [click](https://www.bioinfo-lab.com/ip.txt)

Port: 13579

User Name: dt + Student ID (e.g. dt2023000001)

Password: dt + Student ID + @biuh2025 (e.g. dt2023000001@biuh2025)

<br>

---------------------

### 4. Linux Basics

#### pwd, cd, ls

```
# show the path of your home directory
cd ~
pwd

# changes the current working directory to its immediate parent directory
cd ..
pwd

# show all the files and folders under current working directory
ls

# changes the current working directory to your home directory
cd ~
pwd
```

#### mkdir, touch

```
cd ~

# make sure that you are in your home directory
pwd

# create a new folder named "new_folder"
mkdir new_folder

# create a new empty file named "new_file.txt"
touch new_file.txt

# show all the files and folders under current working directory
ls
```

#### less, cat

```
# use less to check the content of a demo file. press "q" to quit
less /home/students/dt2025/resource/demo.txt

# use cat to show the entire content of a demo file.
cat /home/students/dt2025/resource/demo.txt

```

#### cp, mv rm

```
cd ~

# copy the demo.txt to your home directory
cp /home/students/dt2025/resource/demo.txt ~/demo.txt
ls

# move the your demo.txt to demo_mv.txt
mv demo.txt demo_mv.txt
ls

# remove the demo_mv.txt
rm demo_mv.txt
ls

# copy a folder
cp -r new_folder copy_folder
ls

# move a folder
mv new_folder move_folder
ls

# remove a folder
rm -rf copy_folder
ls

```

#### nano

```
cd ~
nano new_nano_file.txt

# write something into "new_nano_file.txt"
# save: Ctrl + O
# Exit: Ctrl + X

ls

# see the content of "new_nano_file.txt"
cat new_nano_file.txt

```

#### SFTP

```
# Use SFTP to upload and download some files.

```

#### Tips

“tab” type the first few letters of a file name or command, then press the Tab key. Linux will automatically complete the rest for you.

“history” You can see all the commands you have run before.

Try "ai", "aiw", and "aid"


<br>

---------------------

### End


