from langchain.prompts import PromptTemplate
def get_prompt(story_type):

    prompt_template=PromptTemplate(
        input_variables=["story_type"],
        template="Write a creative {story_type} story with an inspiring moral"
        ) 
    return prompt_template.invoke({'story_type':story_type})