# QhacksSmarizer
For using videoPart.py,
- download streamlit by using "pip install streamlit", 
- install youtube_dl by using "pip install youtube_dl"
- download ffbinaries from " https://ffbinaries.com/downloads", and download 3 files: "ffplay", "ffprobe" and "ffmpeg", Sudo cp ./ffmpeg ./ffplay ./ffprobe /usr/local/bin
input your computer password
then "vim ~/.zshrc"
Add "PATH=“/usr/local/bin:$PATH” to end of zshrc
then use ":wq" to save and quit
- after install all the libraries, cd to your "videoPart.py" place, and use "streamlit run videoPart.py"

