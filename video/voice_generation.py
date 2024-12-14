

import pyttsx3

def generate_audio(text, output_file):
    engine = pyttsx3.init()
    
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)  
    engine.save_to_file(text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    with open("summary.txt", "r") as f:
        summary_text = f.read()

    generate_audio(summary_text, "summary_audio.mp3")
