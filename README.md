# Convert Jupyter Notebooks to Word Documents

This repository contains a Python script (`convert_ipynb_to_docx.py`) that automates the conversion of all Jupyter Notebook (`.ipynb`) files in the current directory into Word documents (`.docx`).

## Prerequisites

Before running the script, make sure you have the following installed:

1. **Python** (3.7 or newer)
   - [Download and install Python](https://www.python.org/downloads/)

2. **Jupyter Notebook**
   - Install Jupyter Notebook using `pip`:
     ```bash
     pip install notebook
     ```

3. **Pandoc**
   - Download and install Pandoc from [https://pandoc.org/installing.html](https://pandoc.org/installing.html).
   - Ensure Pandoc is added to your system's `PATH` so it can be used from the terminal.

## Steps to Run the Script

Follow these steps to use the script:

1. **Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

   2. **Install Required Python Libraries**
   Install the `nbconvert` package, which is used for converting `.ipynb` to `.md`:
   ```bash
   pip install nbconvert
   ```

3. **Place the Jupyter Notebooks in the Directory**
   Ensure all the `.ipynb` files you want to convert are in the same directory as the script (`convert_ipynb_to_docx.py`).

4. **Run the Script**
   Run the script from the terminal:
   ```bash
   python convert_ipynb_to_docx.py
   ```

5. **View the Output**
   - The script will generate `.docx` files for each `.ipynb` file in the current directory.
   - The `.docx` files will be saved in the same directory as the script.

6. **Clean Up (Optional)**
   - The script automatically removes intermediate `.md` files after the conversion.
   - If you want to keep the `.md` files, edit the script and comment out the `os.remove(md_file)` line.

## Example

Suppose your directory contains the following files:

```plaintext
convert_ipynb_to_docx.py
notebook1.ipynb
notebook2.ipynb
```

After running the script, your directory will look like this:

```plaintext
convert_ipynb_to_docx.py
notebook1.docx
notebook2.docx
```

## Troubleshooting

- **Command not found: pandoc**
  - Ensure Pandoc is installed and added to your system's `PATH`.
  - You can test this by running:
    ```bash
    pandoc --version
    ```

- **Missing Jupyter or nbconvert**
  - Ensure Jupyter is installed using:
    ```bash
    pip install notebook
    ```

- **Script Errors**
  - Make sure your `.ipynb` files are not corrupted or empty.
  - If you encounter specific errors, please open an issue in this repository.

---

Happy converting!
