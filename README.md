# Picturesque

Picturesque is a command-line application that allows you to upload, store, download, and search photos from your very own account. It's super simple to use; all you need to do is run the program in your terminal and follow the instructions!

## Prerequisites

Make sure you have Python 3.8 installed, as well as pip3.

## How to use

1. Download the source code from this repo as a zip file, and unzip the file to your desired location.
2. Navigate to the top folder (Picturesque/). Allow run.sh to be executable:
```
$ chmod +x run.sh
```

3. Run the script:
```
$ ./run.sh
```

*Note: There are quite a few dependencies that need to be installed. This may take a few minutes.* 

## Tech used in this mini-project:

Python:
This program is written in Python 3.8. I have been using a lot of Python to complete assignments in my upper-year courses, for example in my recent AI course, so I'm well familiarized with the language. Python also holds a special place in my heart because it was the first language I taught myself to code in when I was a kid!

Firebase API:
This program uses the Authentication, Storage, and Database hosted on Google's Firebase service. I use an API wrapper, called Pyrebase, to communicate with the service.

Tensorflow and Machine Learning:
I recently completed an AI course, so I thought it might be fun to add an AI element to this project. Although, in the interest of time and not wanting to reinvent the wheel, I used an open source image recognition package called Image AI to add a tag to each photo when you upload them to your account in this app. See https://github.com/OlafenwaMoses/ImageAI.




