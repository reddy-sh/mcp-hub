# MCP Hub Documentation

## Overview
MCP Hub is a framework for creating and managing Model Context Protocol (MCP) servers and clients. It leverages the `uv` tool for fast package installation and configuration management.

## Why Use UV?
UV simplifies package management and configuration with blazing-fast commands. Learn a few commands to get started, and you're good to go:

- Initialize a project:
  ```bash
  uv init
  ```
- Sync Python version and dependencies:
  ```bash
  uv sync
  ```

For more details, visit the [UV GitHub repository](https://github.com/astral-sh/uv).

## Motivation
To understand the basics of MCP and get started with creating MCP servers, refer to the [MCP Quickstart Server Guide](https://modelcontextprotocol.io/quickstart/server).

## Getting Started

### How to Create a Sample MCP Server

1. **Create a New Project Directory**
   ```bash
   uv init XYZ
   cd XYZ
   ```

2. **Set Up a Virtual Environment**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   uv add "mcp[cli]" httpx
   ```

4. **Create the Server File**
   ```bash
   touch XYZ.py
   ```

### How to Run the MCP Server
To run the server, use the following command:
```bash
uv run XYZ.py
```

## Example: Creating a New XYZ Server

Follow the steps outlined above to create and run a new XYZ server. Replace `XYZ` with your desired project name.

## Recent Updates

### Notebooks Directory
The `notebooks/` directory has been added to the project. It includes configuration files and scripts for setting up and running JupyterHub. Key files include:
- `jupyterhub_config.py`: Configuration for JupyterHub.
- `start_jupyterhub.sh`: Script to start the JupyterHub server.

### CIFAR-10 Dataset Downloader
A new script has been added under `ai/computer-vision/09_datasets/` to download the CIFAR-10 dataset using TensorFlow/Keras. To use it, run:
```bash
python ai/computer-vision/09_datasets/download_cifar10.py
```
This script downloads the dataset and prints a confirmation message.

## AI Folder

The `ai/` folder contains various subdirectories and scripts related to computer vision and artificial intelligence. Below is an overview of its structure and contents:

### Subdirectories and Files

#### 01_image_handling
- `basic_manipulations.py`: Basic image manipulation techniques.
- `blue_image.png`: Sample image for testing.
- `hello_cv.py`: A simple script to demonstrate computer vision basics.
- `image_representation.py`: Explains image representation in computer vision.
- `read_display_save.py`: Script to read, display, and save images.
- `README.md`: Documentation for this subdirectory.

#### 02_image_preprocessing
- `augmentation.py`: Image augmentation techniques.
- `normalization.py`: Image normalization methods.

#### 03_feature_extraction
- `hog_extraction.py`: Extracts Histogram of Oriented Gradients (HOG) features.
- `sift_surf_extraction.py`: Demonstrates SIFT and SURF feature extraction.

#### 04_basic_ml_concepts
- `hog_svm_classifier.py`: Implements a classifier using HOG features and SVM.

#### 05_deep_learning_cnn
- `cnn_architecture.py`: Defines a Convolutional Neural Network (CNN) architecture.

#### 06_image_classification
- `train_classifier.py`: Script to train an image classifier.

#### 07_object_detection
- `basic_object_detection.py`: Demonstrates basic object detection techniques.

#### 08_image_segmentation
- `basic_segmentation.py`: Explains basic image segmentation methods.

#### 09_datasets
- `download_cifar10.py`: Script to download the CIFAR-10 dataset.

#### 10_utils
- `image_utils.py`: Utility functions for image processing.

### Additional Files
- `main.py`: Entry point for AI-related scripts.
- `pyproject.toml`: Configuration file for the project.
- `README.md`: Documentation for the `ai/` folder.
- `run.sh`: Shell script to execute AI-related tasks.
- `uv.lock`: Lock file for dependencies.