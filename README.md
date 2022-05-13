# backup-management
The objective of this project was to develop an application that generates backup of several directories at once.

## How to run it?
Just run the backup-management.exe file. 

## How to use it?
You must inform the source path of the file and the backup destination in the text fields and click on "Insert". In this way, a list will be made with the informed backups. If you need to delete any records, just select them in the list and click "Delete". To generate the backup, use the "Run backup" button, causing the .zip files to be generated.

### Insert:
![image](https://user-images.githubusercontent.com/80294295/162634915-42bb982f-5648-43ec-a452-48c37540729f.png)
![image](https://user-images.githubusercontent.com/80294295/162634935-cf22df49-7eea-45b0-a2a8-04e62eeb064d.png)

### Delete:
![image](https://user-images.githubusercontent.com/80294295/162634960-d69abf94-fb2a-4de8-90c0-d6e1f2deba69.png)
![image](https://user-images.githubusercontent.com/80294295/162634976-bde7197f-4fd1-43e5-b8f5-d4874306b98d.png)

### Run backup:
![image](https://user-images.githubusercontent.com/80294295/162635009-a298c225-fcb4-439a-9411-32c3e61e7fc4.png)
![image](https://user-images.githubusercontent.com/80294295/162635025-eaa8881a-3f77-4bc6-819d-af07c376b717.png)
![image](https://user-images.githubusercontent.com/80294295/162635047-54b2dcc6-6122-4129-82e5-5eab9d202d7c.png)

## Remarks
- The document "arquivos.txt" must be in the same directory as the executable. This is where the informed paths are stored.
- The generated backup file will always be in the format "backup-"date"--"time".zip". 
- The project works with backup of directories (folders) and not single files.
