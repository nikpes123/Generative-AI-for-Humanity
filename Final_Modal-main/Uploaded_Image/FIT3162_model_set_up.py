from IPython.display import HTML, display
import base64


def setup_upload_ui():

    # HTML code for the file upload UI
    upload_ui = '''
    <!DOCTYPE html>
    <html>
    <head>
    <title>Image Upload</title>
    <style>
        /* Your CSS styles for the upload UI */
        /* Add styles for the upload box and button */
        .upload-container {
            display: flex;|
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 200px;
            border: 2px dashed #ccc;
            border-radius: 5px;
            cursor: pointer;
        }
        .upload-container:hover {
            border-color: #aaa;
        }
        #file-input {
            display: none;
        }
        .upload-text {
            font-size: 16px;
            color: #888;
        }
    </style>
    </head>
    <body>
    <div class="upload-container" onclick="document.getElementById('file-input').click()">
        <input type="file" id="file-input" accept="image/*">
        <p class="upload-text">Click or drag & drop an image here to upload</p>
    </div>

    <script>
        document.getElementById('file-input').addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(event) {
            const imgData = event.target.result;
            // Mock display of the uploaded image
            const imgElement = document.createElement('img');
            imgElement.src = imgData;
            imgElement.style.maxWidth = '25%';
            document.body.appendChild(imgElement);
            };
            reader.readAsDataURL(file);
        }
        });
    </script>
    </body>
    </html>
    '''
    return upload_ui

def setup_jscode():
    # JavaScript function to send image data to Python
    js_code = '''
    <script>
      document.getElementById('file-input').addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = function(event) {
            const imgData = event.target.result;
            google.colab.kernel.invokeFunction('processImageData', [imgData], {});
          };
          reader.readAsDataURL(file);
        }
      });
    </script>
    '''
    return js_code


# Function to receive image data in Python and save it using imageio
def process_image_data(img_data):
    img_data = img_data.split(",")[1]  # Extract base64 data
    source_image = base64.b64decode(img_data)  # Decode base64 to bytes
    with open('/content/drive/MyDrive/Final_Model/Uploaded_Image/input_image.jpg', 'wb') as f:  # Save the image locally
        f.write(source_image)
    print("Image saved")