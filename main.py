import os
import gradio as gr
import openai

# Insert your API key Here
api_key = "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"

if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

def generate_statement(keyword, emotion, action, num, sd):
    try:
        # Validate the number of sentences
        num = int(num)
        if num <= 0:
            return "Number of sentences must be a positive integer."

        # Construct a more detailed request message
        request_message = f"""Generate {num} short and meaningful sentences that convey the following:
        
        Context: A statement expressing {emotion} emotion.
        Action: {action}
        Direction: A statement from {sd}.
        
        Use the keyword(s) '{keyword}' in each sentence. Ensure that the sentences are unique, coherent, and follow proper grammar.
        Avoid using pronouns; use nouns instead.
        
        Example: If 'keyword' is 'love,' 'emotion' is 'happiness,' 'action' is 'sharing,' 'num' is 5, and 'sd' is 'me to you,' then a sample output could be:
        'Happiness fills my heart as I share my love with you.'
        
        Provide {num} such unique sentences with the sentence number infront of it."""

        # Initialize the OpenAI API client
        openai.api_key = api_key

        # Generate text using GPT-2
        response = openai.Completion.create(
            engine="text-davinci-002",  # GPT-2 engine
            prompt=request_message,
            max_tokens=1500,  # Adjust max_tokens as needed
            n=1  # Number of responses to generate
        )

        generated_text = response.choices[0].text.strip()
        return generated_text

    except ValueError:
        return "Number of sentences must be a positive integer."


def launch_interface():
    iface = gr.Interface(
        fn=generate_statement,
        inputs=[
            gr.components.Textbox(label="Keyword(s) (Separate by a comma if multiple)"),
            gr.components.Textbox(label="Emotion(s) (Separate by a comma if multiple)"),
            gr.components.Textbox(label="Action (Optional)"),
            gr.components.Number(label="Number of Sentences"),
            gr.components.Radio(["me to you", "me to them", "him to them", "they to me"], label="Statement Direction")
        ],
        outputs=[gr.components.Textbox(label="Generated Sentences")],
    )
    iface.launch()

if __name__ == "__main__":
    launch_interface()
