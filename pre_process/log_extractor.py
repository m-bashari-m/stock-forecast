import os

def process_logs(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:  # Using 'a' to append to the output file
        for line in infile:
            line = line.replace("\t", " ")
            parts = line.split(" ")
            year, month, day = parts[5].split('.')
            hour, minute, _ = parts[6].split(':')
            data_section = parts[-1]
            outfile.write(f'{year},{month},{day},{hour},{minute},{data_section}')

    print(f"Data from {input_file} extracted and written to {output_file}")

def process_folder_logs(logs_folder_path, output_file):

    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    

    if not os.path.isfile(output_file):
        with open(output_file, 'w') as outfile:
            outfile.write('year,month,day,hour,minute,open,close,high,low,EMA20,EMA60,EMA100,EMA200,RSI,ADX\n')

    for file in os.listdir(logs_folder_path):
        file_path = os.path.join(logs_folder_path, file)
        if os.path.isfile(file_path):
            process_logs(file_path, output_file)

if __name__ == "__main__": 
    process_folder_logs("./pre_process/raw_logs", "./pre_process/data/data.csv")
