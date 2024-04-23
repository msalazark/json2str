import json

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

# Simula el JSON que tienes
json_file_path = 'test.json'
json_data = read_json_from_file(json_file_path)

# Genera el contenido SRT del JSON
srt_output = json_to_srt(json_data)
print(srt_output)


# Ruta del archivo SRT de salida
output_file_path = 'salida.srt'

# Escribir el contenido SRT en un archivo
with open(output_file_path, 'w') as file:
    file.write(srt_output)
    print(f"SRT file has been saved to {output_file_path}")