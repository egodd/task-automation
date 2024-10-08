import os
from docx2pdf import convert


def convert_all_docx_in_folder():
    input_folder = "files"
    output_folder = "pdfs"

    # Ensure the 'pdfs' directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Check if there are any docx files to convert
    docx_files = [f for f in os.listdir(input_folder) if f.endswith('.docx')]

    if not docx_files:
        print(f"No .docx files found in {input_folder}. Nothing to convert.")
        return

    for file_name in docx_files:
        docx_file = os.path.join(input_folder, file_name)
        output_pdf = os.path.join(output_folder, file_name.replace('.docx', '.pdf'))

        try:
            print(f'Converting {file_name} to PDF...')
            # Convert and save PDF to the 'pdfs' folder
            convert(docx_file, output_pdf)
            print(f'Successfully converted {file_name} to {output_pdf}')
        except Exception as e:
            print(f'Error converting {file_name}: {e}')


if __name__ == "__main__":
    convert_all_docx_in_folder()