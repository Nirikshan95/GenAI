from models.deepseek_loader import load_deepseek_model
from prompts.prompt_template import get_prompt

def main(story_type):
    model=load_deepseek_model()
    prompt=get_prompt(story_type)
    response = model.invoke(prompt)
    return response.content


if __name__ == "__main__":
    story_type=input("Enter the story type: ")
    print(main(story_type))
