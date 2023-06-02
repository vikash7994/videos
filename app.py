from flask import Flask, render_template, request, redirect, send_file
import youtube_dl
from pytube import YouTube
import instaloader
import requests
import os
import io
# from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/terms_and_conditions')
def terms_and_conditions():
   return render_template('terms_and_conditions.html')

@app.route('/contact')
def contact():
   return render_template('contact.html')   

#code for youtube video download
@app.route('/yt')
def yt():
   return render_template('yt.html')
   
@app.route('/downloadyt', methods=["POST", "GET"])
def downloadyt():       
    # Get the YouTube video URL from the form submission
    video_url = request.form['urll']
# Check if URL is empty or invalid
    if not video_url:
        error_message = "Invalid URL. Please enter a valid YouTube video URL."
        return render_template("your_template.html", error_message=error_message)
      # Create a YouTube object from the video URL
    yt = YouTube(video_url)

    # Get the highest quality video stream
    ys = yt.streams.get_highest_resolution()

    # Get the download link for the video
    download_link = ys.url

   
    thumbnail_url = yt.thumbnail_url

    # Render the yt.html template with the thumbnail URL, video URL, and download URL
    return render_template('yt.html', thumbnail_url=thumbnail_url, video_url=download_link, download_url=download_link)


# Code for Facebook video download
@app.route('/fb')
def fb():
   return render_template('fb.html')

@app.route('/download', methods=["POST", "GET"])
def download():
	url = request.form["url"]
	print("Someone just tried to download", url)
	with youtube_dl.YoutubeDL() as ydl:
		url = ydl.extract_info(url, download=False)
		print(url)
		try:
			download_link = url["entries"][-1]["formats"][-1]["url"]
		except:
			download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")

@app.route('/insta')
def insta():
   return render_template('insta.html')
@app.route('/downloadinsta', methods=['POST'])
def downloadinsta():
    link = request.form['insta_url']
    response = requests.get(link, stream=True)
    if response.status_code == 200:
        filename = 'reels.mp4'  # Define the filename as per your requirement
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return redirect('insta.html')
    else:
        return 'Error downloading the Reels video.'

if __name__ == '__main__':
   app.run(port=80, debug= True)