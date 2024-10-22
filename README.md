# Sorting Algorithms Visualizer

This project is a web application that visualizes various sorting algorithms. It allows users to input a list of numbers and select a sorting algorithm to see how the algorithm sorts the list step-by-step.

## Features

- **Bubble Sort**: A simple comparison-based sorting algorithm.
- **Optimized Bubble Sort**: An improved version of bubble sort that stops early if the list is already sorted.
- **Selection Sort**: A comparison-based sorting algorithm that divides the list into a sorted and an unsorted region.

## Installation

1. Clone the repository

2. Navigate to the project directory:
    ```sh
    cd sortingAlgorithmsVisualizer
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000`.

## Project Structure

- `app.py`: The main Flask application file containing the sorting algorithms and routes.
- `templates/index.html`: The HTML template for the web interface.
- `static/`: Directory for static files like images.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [Vercel](https://vercel.com/) - Hosting for the live demo.

## Live Demo

Check out the live demo [here](https://sorting-algorithms-visualizer-ten.vercel.app).
