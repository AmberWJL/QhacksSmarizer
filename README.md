# QhacksSmarizer
For using **youtubeTranscriber.py**,
- download streamlit by using "pip install streamlit", 
- install youtube_dl by using "pip install youtube_dl"
- download ffbinaries from " https://ffbinaries.com/downloads", and download 3 files: "ffplay", "ffprobe" and "ffmpeg", Sudo cp ./ffmpeg ./ffplay ./ffprobe /usr/local/bin
input your computer password
then "vim ~/.zshrc"
Add "PATH=“/usr/local/bin:$PATH” to end of zshrc
then use ":wq" to save and quit
- after install all the libraries, cd to your "videoPart.py" place, and use "streamlit run videoPart.py"


- After installations, you could run the youtubeTranscriber.py by using command "streamlit run youtubeTranscriber.py"
- After clicking the "Get transcript",  you could get a **transcription.txt** file in your directory
- Then run the **Summarizer.py**, by adjusting the final line's number, you could get different length summary. e.g. if you input 4, you could get a relatively long but accurate summary. if you enter 1, you could get a short summary but less accurate summary.

