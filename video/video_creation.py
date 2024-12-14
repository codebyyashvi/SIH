from moviepy.editor import ImageClip, AudioFileClip

def create_video(image, audio_file, output_file):
    # Create a video clip from the image and set its duration
    image_clip = ImageClip(image).set_duration(10)  # 10 seconds duration for the image
    # Load the audio file
    audio_clip = AudioFileClip(audio_file)

    # Set the audio to the image clip
    final_clip = image_clip.set_audio(audio_clip)

    # Write the final video to a file with specified codec
    final_clip.write_videofile(output_file, fps=24, codec="libx264")

if __name__ == "__main__":
    image_file = "background_image.png"  # Your image file path
    audio_file = "summary_audio.mp3"  # Your audio file path
    output_video_file = "summary_video.mp4"  # Output video file path
    
    # Create the video
    create_video(image_file, audio_file, output_video_file)

    # Optional: If you want to load the video again and do something with it
    # For example, you could do further processing like resizing, trimming, etc.
    from moviepy.editor import VideoFileClip

    clip = VideoFileClip(output_video_file)
    clip.write_videofile("final_output_video.mp4", codec="libx264", audio_codec="aac")
