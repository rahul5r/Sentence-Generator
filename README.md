# Sentence Generator using OpenAI's GPT-2

### Introduction

This project utilizes OpenAI's GPT-2 engine to generate short and meaningful sentences based on user-specified parameters. The sentences are constructed with a given keyword, emotion, action, and contextual statement direction. The user interface is built using Gradio, allowing easy interaction and customization.

### Getting Started

To run this project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/racker9r/Sentence-Generator.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   Replace the placeholder in the `api_key` variable with your OpenAI API key.

   ```python
   api_key = "your-api-key-here"
   ```

   Ensure your API key is kept confidential and not shared publicly.

4. Run the project:

   ```bash
   python sentence_generator.py
   ```

   This will launch the Gradio interface, allowing you to interact with the sentence generator.

### Usage

1. Launch the interface by running the project.

2. Input the following parameters:

   - Keyword(s) (Separate by a comma if multiple)
   - Emotion(s) (Separate by a comma if multiple)
   - Action (Optional)
   - Number of Sentences
   - Statement Direction

3. Click on the "Generate Sentences" button.

4. View the generated sentences in the output textbox.

### Example

```python
Keyword(s): love
Emotion(s): happiness
Action: sharing
Number of Sentences: 5
Statement Direction: me to you
```

Generated Sentences:
1. Happiness fills my heart as I share my love with you.
2. Sharing my love brings immense joy to my soul.
3. I express boundless happiness by sharing my love with you.
4. My heart overflows with joy as I share my love with you.
5. Sharing the essence of love brings unparalleled happiness to me.

### Note

- Ensure your OpenAI API key is set up correctly.
- Adjust the `max_tokens` parameter in the `generate_statement` function based on your requirements.


### UI Screenshots
![Screenshot 2024-01-21 170957](https://github.com/racker9r/Sentence-Generator/assets/111962760/a6a127cb-c255-4eec-8f38-947a0ba51c2f)
