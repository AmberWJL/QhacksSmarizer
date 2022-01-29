# QhacksSmarizer
For using videoPart.py,
- download streamlit by using "pip install streamlit", 
- install youtube_dl by using "pip install youtube_dl"
- download ffbinaries from " https://ffbinaries.com/downloads", and download 3 files: "ffplay", "ffprobe" and "ffmpeg", Sudo cp ./ffmpeg ./ffplay ./ffprobe /usr/local/bin
输入你电脑password
然后 vim ~/.zshrc
在文件结尾加上
PATH=“/usr/local/bin:$PATH”
按esc后输入:wq退出

- after install all the libraries, cd to your "videoPart.py" place, and use "streamlit run videoPart.py"

