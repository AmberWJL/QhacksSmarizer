import streamlit as st
import youtube_dl
import requests
import pprint
from configure import auth_key
from time import sleep
import os


#this code is from Assembly AI tutorial
if 'status' not in st.session_state:
    st.session_state['status'] = 'submitted'

ydl_opts = {
   'format': 'bestaudio/best',
   'postprocessors': [{
       'key': 'FFmpegExtractAudio',
       'preferredcodec': 'mp3',
       'preferredquality': '192',
   }],
   'ffmpeg-location': './',
   'outtmpl': "./%(id)s.%(ext)s",
}

transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
upload_endpoint = 'https://api.assemblyai.com/v2/upload'

headers_auth_only = {'authorization': auth_key}
headers = {
   "authorization": auth_key,
   "content-type": "application/json"
}
CHUNK_SIZE = 5242880
 
@st.cache
def transcribe_from_link(link, categories: bool):
	_id = link.strip()

	def get_vid(_id):
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			return ydl.extract_info(_id)

	# download the audio of the YouTube video locally
	meta = get_vid(_id)
	save_location = meta['id'] + ".mp3"

	print('Saved mp3 to', save_location)


	def read_file(filename):
		with open(filename, 'rb') as _file:
			while True:
				data = _file.read(CHUNK_SIZE)
				if not data:
					break
				yield data


	# upload audio file to AssemblyAI
	upload_response = requests.post(
		upload_endpoint,
		headers=headers_auth_only, data=read_file(save_location)
	)

	audio_url = upload_response.json()['upload_url']
	print('Uploaded to', audio_url)

	# start the transcription of the audio file
	transcript_request = {
		'audio_url': audio_url,
		'iab_categories': 'True' if categories else 'False',
	}

	transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)

	# this is the id of the file that is being transcribed in the AssemblyAI servers
	# we will use this id to access the completed transcription
	transcript_id = transcript_response.json()['id']
	polling_endpoint = transcript_endpoint + "/" + transcript_id

	print("Transcribing at", polling_endpoint)

	return polling_endpoint


def get_status(polling_endpoint):
	polling_response = requests.get(polling_endpoint, headers=headers)
	st.session_state['status'] = polling_response.json()['status']

def refresh_state():
	st.session_state['status'] = 'submitted'


st.title('Smarizer')

link = st.text_input('Enter your YouTube video URL', 'https://www.youtube.com/watch?v=qDj0e96WfrY', on_change=refresh_state)
st.video(link)

st.text("The transcription is " + st.session_state['status'])

polling_endpoint = transcribe_from_link(link, False)

st.button('Get transcript', on_click=get_status, args=(polling_endpoint,))

transcript=''
if st.session_state['status']=='completed':
	polling_response = requests.get(polling_endpoint, headers=headers)
	transcript = polling_response.json()['text']

st.markdown(transcript)

with open("transcription.txt", "w") as file:
    file.write(transcript)
    file.close()

level = 0
level = st.number_input("please input the level(1-5) of summary you need(you need to click 'Get transcript' first): ",min_value=1, max_value=5, step=1)
data = ""
print("userinput",level)

if st.button("Get Summary"):
	from Summarizer import read_article 
	from Summarizer import sentence_similarity 
	from Summarizer import build_similarity_matrix 
	from Summarizer import generate_summary 
	from Summarizer import degree_summary 
	return_summary = generate_summary("transcription.txt", degree_summary("transcription.txt",level))
	st.markdown(return_summary)


