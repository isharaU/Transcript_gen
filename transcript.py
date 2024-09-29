import moviepy.editor as mp
import whisper

# Step 1: Load the video and extract the audio
def extract_audio_from_video(video_path, audio_output):
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output)

# Step 2: Transcribe the audio using Whisper
def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # You can use "small", "medium", or "large" models for more accuracy
    result = model.transcribe(audio_path)
    return result['text']

# Step 3: Main function to generate subtitles from video
def generate_transcript(video_path, audio_output='audio.wav'):
    # Extract the audio from the video
    extract_audio_from_video(video_path, audio_output)
    
    # Transcribe the audio
    transcript = transcribe_audio(audio_output)
    
    # Save the transcript to a text file
    with open("transcript.txt", "w") as f:
        f.write(transcript)
    
    print("Transcript generated successfully!")
    return transcript

# Example usage
video_file = "E:\Academic\MA4014 - Linear Models and Multivariate Statistics\Lectures\Week 01.mp4"  # Replace with your video file path
generate_transcript(video_file)
