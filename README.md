# Generative AI for Face Anonymization

## Overview
This project leverages advanced Generative AI technologies, specifically StyleGAN2 and Pix2PixHD, to address privacy concerns in AI-generated imagery through the anonymization of human faces. By implementing gender-swapping techniques within latent and pixel spaces, the project ensures the generation of realistic, high-resolution anonymized images, maintaining essential attributes like hair, background, and pose.

## Key Features
- **Integrated StyleGAN2 and Pix2PixHD**: Seamlessly generates authentic facial images with high-resolution transformations.
- **Gender-Swap Anonymization**: Modifies gender-specific traits while preserving non-identity features to protect individual identities effectively.
- **Cosine Similarity Scoring**: Ensures that the anonymization process retains essential features by measuring the similarity between the original and anonymized images.
- **Streamlined Deployment**: Ready-to-use Jupyter Notebook via Google Colab with free GPU support for straightforward implementation without complex environment setups.

## Project Motivation
As AI technologies increasingly permeate the field of image generation, ensuring privacy compliance remains a paramount challenge. This project aims to safeguard individual identities, allowing for the continued use of large, diverse datasets in AI research and development without compromising privacy.

## Repository Contents
- `models/`: Contains the core scripts for preprocessing, classification (using ResNet18), and the anonymization pipelines.
- `notebooks/`: Jupyter Notebooks ready for Google Colab use, covering the entire process from image upload to anonymization and results analysis.
- `results/`: Includes sample outputs, detailed logs, and performance metrics to demonstrate the efficacy of the implemented methods.
- `docs/`: (Optional) Additional documentation, user guides, and methodological descriptions.

## Getting Started
1. **Launch in Colab**: [Open the notebook](https://colab.research.google.com/drive/15RFBtXzo-lvKwMCkgh_0ZgeCASOPOgLE?usp=sharing) directly in your browser.
2. **Run All Cells**: Execute the steps sequentially to upload your image, process the anonymization, and view or save the results.
3. **Customize Parameters**: Adjust thresholds or model settings to experiment with different levels of anonymization.

## Prerequisites
- **Recommended**: Google Colab for a ready-to-use environment with GPU.
- **Optional Local Setup**:
  - Python 3.x
  - Deep learning libraries (TensorFlow or PyTorch, as per your implementation)
  - Common libraries like NumPy, scikit-learn, Pillow, and Matplotlib.

## Further Reading
For more detailed information about the project, including background, methodologies, and detailed analyses, please refer to the [Final Report PDF](./Final%20Report.pdf) available in this repository.

## How to Contribute
- Interested in contributing? Please submit an issue or pull request with your suggestions or enhancements.

---
