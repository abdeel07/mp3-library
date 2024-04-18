[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/545oUMxH)

## 1. Project Title and Description
    - 🎵 RiffRoom
    - RiffRoom is a music library platform where users can upload songs, like their favorite songs, and create playlists for enjoyment.
## 2. Installation
    - Dependencies: 
        - Node.js (18.18.2)
        - Python (3.12)
        - PostgreSQL (16.2)
    - Installation Instructions:
    
        Flask Backend Initial Setup
        1. Navigate into the backend folder
        2. Once the packages have been installed, create a virtual environment with this command 
        	```py -3 -m venv <name of enviornment>``` or ```python -m venv <name of environment>``` (depending on what version of python you have)
        
        3. Once this command is complete, you should see an env (or a folder named after whatever you have chosen for the name) folder in your backend folder.
        4. To switch into the virtual environment: ```<name of enviornment>\Scripts\activate```
        5. Once in the virtual environment, your terminal should look like this: ```(env) C:\Users\jturk\Documents\Seneca\BSD\BTP405\Project One\BTP-Project-One\backend>```
        6. Run this command when inside the virtual environment and in the backend folder:  ```pip install -r requirements.txt```
        7. Set FLASK_APP environment variable: ```set FLASK_APP=app.py``` or ```$env:FLASK_APP = "app.py"``` (depending on if you're using Command Prompt or PowerShell)
        8. Run the command: flask run to start the backend server.
        9. Lastly, if you want to exit the environment, you can use ```deactivate```

        Vue Frontend Initial Setup
        1. Navigate into the frontend folder, then the ```music-management-app``` folder
        2. Run the command ```npm install```
        3. Wait for packages to load, then run the command ```npm run dev``` 
        
        Setting up PostgreSQL
        1. Head over to PostgreSQL's website and download their installer for your operating system. [Installer](https://www.postgresql.org/download/)
        2. Follow the installer wizard and install PostgreSQL.
        3. Add PostgreSQL's bin directory to the PATH environment variable:
        	- Find your file path (ex: C:\Program Files\PostgreSQL\16\bin).
        	- Use the win + r shortcut to bring up the Run dialog and enter ```sysdm.cpl```.
        	- Select the Advanced tab at the top and click the ```Environment Variables``` button at the bottom.
        	- In environment variables you want to use the bottom section that says ```System```.
        	- Under ```System``` you want to find the ```Path``` variable and click on the ```Edit``` button.
        	- Once ```Edit``` is clicked you can click ```New``` and add your bin path ```C:\Program Files\PostgreSQL\16\bin``` to the environment variable.
        	- Finally you can now click ```Ok``` on every box and you should be able to use PostgreSQL in CMD. 

## 3. Usage
    - Examples: 
        - To start uploading your music first click on the register button on the top right and register for an account.
        - Next Login to your account and start uploading music through the plus button next to uploads. Make sure to fill out the details of the mp3 file.
        - Finally, you can create playlists and add the song you uploaded or like the song you uploaded to add it to your liked songs.
    - Configuration:
        - N/A.
## 4. Features
    - 🎸 Features:
        - Login or register to access the platform
        - Upload your songs and melodies
        - Create personalized playlists
        - Like your favorite songs
## 5. Contributing
    - Guidelines:
        - Bug Reports: If you encounter any issues while using RiffRoom, please open a new issue on our GitHub repository. Be sure to include detailed steps to reproduce the bug and any relevant information about your environment.
        - Feature Requests: Open a new issue on our GitHub repository and share your thoughts.
        - Code Contributions: If you would like to contribute code to RiffRoom, please fork our repository, make your changes, and submit a pull request. Be sure to provide a clear description of your changes.
    - Code Style: N/A
## 6. Credits
    - Authors:
        - John Turkson
        - Hamzah Mandoo
    - Acknowledgments:
        - Inspired by SoundCloud Global Limited & Co. KG.
## 7. License
    - License Information:
        - RiffRoom is open-source software licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
## 8. Additional Sections (Optional)
    - Roadmap:
        - Browse other people's music
        - UI Refinements
