import streamlit as st
import json
import os

def read_json_from_file(file_path):
    """Read and load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(seconds):
    """Convert seconds to the format hh:mm:ss,mmm."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    millis = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{int(seconds):02},{millis:03}"

def json_to_srt(json_data):
    srt_content = []
    for i, segment in enumerate(json_data['segments'], start=1):
        start_time = format_time(segment['start'])
        end_time = format_time(segment['end'])
        text = segment['text'].strip()
        srt_content.append(f"{i}\n{start_time} --> {end_time}\n{text}\n")
    return "\n".join(srt_content)

def process_folder(folder_path):
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    for json_file in json_files:
        json_path = os.path.join(folder_path, json_file)
        json_data = read_json_from_file(json_path)
        srt_output = json_to_srt(json_data)
        output_file_path = os.path.join(folder_path, json_file.replace('.json', '.srt'))
        with open(output_file_path, 'w') as file:
            file.write(srt_output)
        st.write(f"SRT file has been saved to {output_file_path}")

# Streamlit UI
st.title("JSON to SRT Converter")
folder_path = st.text_input("Enter the path to the folder containing JSON files:")
if st.button("Convert JSON to SRT"):
    if folder_path:
        process_folder(folder_path)
    else:
        st.write("Please enter a valid folder path.")