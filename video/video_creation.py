from moviepy.editor import ImageClip, AudioFileClip

def create_video(image, audio_file, output_file):
    image_clip = ImageClip(image).set_duration(10)
    audio_clip = AudioFileClip(audio_file)
    final_clip = image_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_file, fps=24, codec="libx264")

if __name__ == "__main__":
    image_file = "background_image.png" 
    audio_file = "summary_audio.mp3" 
    output_video_file = "summary_video.mp4" 
    
    create_video(image_file, audio_file, output_video_file)

    from moviepy.editor import VideoFileClip

    clip = VideoFileClip(output_video_file)
    clip.write_videofile("final_output_video.mp4", codec="libx264", audio_codec="aac")
