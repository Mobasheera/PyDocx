import os
import subprocess

# Get the list of all .ipynb files in the current directory
ipynb_files = [f for f in os.listdir() if f.endswith('.ipynb')]

# Convert each .ipynb to .md and then to .docx
for ipynb_file in ipynb_files:
    # Convert .ipynb to .md using nbconvert
    md_file = ipynb_file.replace('.ipynb', '.md')
    print(f"Converting {ipynb_file} to {md_file}...")
    
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', ipynb_file])

    # Now convert .md to .docx using pandoc
    docx_file = md_file.replace('.md', '.docx')
    print(f"Converting {md_file} to {docx_file}...")
    
    subprocess.run(['pandoc', md_file, '-o', docx_file])

    # Optionally, you can remove the intermediate .md file after conversion
    os.remove(md_file)

print("Conversion complete!")
