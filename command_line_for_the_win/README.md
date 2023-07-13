# Project: Command line for the win

## Resources

#### Read or watch:

* []()
* []()
* []()
* []()
* []()
## Learning Objectives

### General

* A README.md file, at the root of the folder of the project, is mandatory
* This project will be manually reviewed.
* As each task is completed, the name of that task will turn green
* Create a screenshot, showing that you completed the required levels
* Push this screenshot with the right name to GitHub, in either the PNG or JPEG format
## Tasks

| Task | File |
| ---- | ---- |
| 0. First 九 tasks | [0-first_9_tasks.jpg,0-first_9_tasks.png](./0-first_9_tasks.jpg,0-first_9_tasks.png) |
| 1. Reach חי completed tasks | [1-next_9_tasks.jpg,1-next_9_tasks.png](./1-next_9_tasks.jpg,1-next_9_tasks.png) |
| 2. Reach the perfect cube, 27 | [2-next_9_tasks.jpg,2-next_9_tasks.png](./2-next_9_tasks.jpg,2-next_9_tasks.png) |



## Using SFTP Command-Line Tool for File Transfer

To demonstrate the use of the SFTP command-line tool for transferring files from your local machine to a sandbox environment, follow these steps:

1. Open a terminal or command prompt on your local machine.

2. Connect to the sandbox environment using SFTP by typing the following command:
   


Replace `username` with your actual username and `sandbox.example.com` with the hostname or IP address of the sandbox environment.

3. Enter your password when prompted to authenticate the connection.

4. Once connected, you will see an SFTP prompt indicating that you are in the SFTP session.

5. Navigate to the directory on the sandbox environment where you want to transfer the files. For example, if you want to transfer the files to a directory called "screenshots," use the following command:



6. On your local machine, navigate to the directory where your files are located. For example, if they are in a folder called "local/files," use the following command:



7. To upload the files from your local machine to the sandbox environment, use the `put` command. For example, to upload all files in the current directory, use the following command:



This command uploads all files from your local directory to the current directory on the sandbox environment.

8. Wait for the file transfer to complete. The progress will be displayed in the terminal.

9. Once the transfer is finished, use the `ls` command to verify that the files are now in the sandbox environment's directory:



This command lists the files in the current directory on the sandbox environment.

10. To exit the SFTP session, use the `exit` command:

 ```
 exit
 ```

This command will return you to the regular command prompt or terminal.

That's it! You have successfully used the SFTP command-line tool to transfer your files from your local machine to the sandbox environment.
