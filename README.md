## K-drama Companion

K-drama Companion is a comprehensive platform for K-drama enthusiasts, offering features such as character recognition, personalized recommendations, trends analysis, trivia and quizzes, and fan community discussions.

### Features

- **Character Recognition:** Upload an image of a K-drama character to identify and get detailed information about them.
- **Personalized Recommendations:** Receive K-drama recommendations based on your mood or preference.
- **K-Drama Trends:** Explore current trends in K-dramas including popular dramas, trending genres, and viewer demographics.
- **Trivia and Quizzes:** Enjoy K-drama related trivia questions or take personality quizzes to match with K-drama characters.
- **Fan Community:** Participate in discussions and share your thoughts, theories, and favorite moments from K-dramas.

### Folder Structure

```
K-drama-Companion/
│
├── README.md
├── requirements.txt
├── app.py
├── assets/
│   ├── Character Recognition/
│   ├── Fan Community/
│   ├── Kdrama Trends/
│   ├── Personal Recommendations/
│   └── Trivia and Quizzes/
├── LICENSE
```

### Setup Instructions

Follow these steps to set up the K-drama Companion project on your local machine:

1. Clone the repository:
    ```bash
    git clone https://github.com/iUnnati31/K-drama-Companion.git
    ```

2. Navigate to the project directory:
    ```bash
    cd K-drama-Companion
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    conda create -p venv python=3.10 -y
    ```

4. Activate the virtual environment:
    - On Windows:
        ```bash
        conda activate venv/
        ```
    - On macOS and Linux:
        ```bash
        source env/bin/activate
        ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

7. Access the app in your web browser at [http://localhost:8501](http://localhost:8501).

### Usage

- **Character Recognition:** Upload an image of a K-drama character and click "IDENTIFY CHARACTER" to get detailed information about them.
- **Personalized Recommendations:** Select your mood or preference and click "Get Recommendations" to receive K-drama recommendations.
- **K-Drama Trends:** Explore current trends in K-dramas by clicking on the "Analyzing trends..." button.
- **Trivia and Quizzes:** Choose between Trivia and Personality Quiz to test your knowledge or discover your K-drama character match.
- **Fan Community Discussions:** Share your thoughts, theories, and favorite moments in the text area and click "Post Discussion" to participate in the fan community.

### License

This project is licensed under the terms of the [MIT License](LICENSE).

### Acknowledgments

- The project utilizes Google Generative AI models for character recognition and text generation.
- Special thanks to the contributors of Streamlit for providing an excellent framework for building interactive web applications.

