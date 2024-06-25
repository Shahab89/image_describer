# Intelligent Image Describer API

## Overview

This project is designed to help visually impaired individuals by generating detailed descriptions of images. The system uses image captioning and text-to-speech technologies to provide audio descriptions in either English or German.

## Features

- Upload an image and receive a detailed description.
- Generate audio descriptions in English or German.
- Uses state-of-the-art models for image captioning and description generation.

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Transformers (HuggingFace)](https://huggingface.co/transformers/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [aiofiles](https://pypi.org/project/aiofiles/)
- [OpenAI](https://www.openai.com/)

## Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Shahab89/image_describer.git
    cd image_describer
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the necessary directories for storing images and sounds:
    ```sh
    mkdir -p images sounds
    ```

5. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your-openai-api-key
    ```

## Usage

1. Run the FastAPI server:
    ```sh
    uvicorn main:app --reload
    ```

2. Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Endpoints

- **Upload Image**
    - **POST** `/upload_image`
    - Upload an image file to the server.
    - **Request**: Multipart form data with the key `image`.

- **Generate Description**
    - **GET** `/description`
    - Generate a detailed description for the last uploaded image.
    - **Parameters**: `language` (either `en` for English or `de` for German).

- **Generate Speech**
    - **GET** `/speech`
    - Generate an audio file of the description for the last uploaded image.
    - **Parameters**: `language` (either `en` for English or `de` for German).

### Example

1. **Upload an Image**:
    ```sh
    curl -X 'POST' \
      'http://127.0.0.1:8000/upload_image' \
      -H 'accept: application/json' \
      -H 'Content-Type: multipart/form-data' \
      -F 'image=@path_to_your_image.jpg'
    ```

2. **Generate a Description**:
    ```sh
    curl -X 'GET' \
      'http://127.0.0.1:8000/description?language=en' \
      -H 'accept: application/json'
    ```

3. **Generate Speech**:
    ```sh
    curl -X 'GET' \
      'http://127.0.0.1:8000/speech?language=en' \
      -H 'accept: application/json'
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
