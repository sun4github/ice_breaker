from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
import os



if __name__ == '__main__':
    load_dotenv()
    print("Hello langchain")
    openai_api_key = os.environ['OPENAI_API_KEY']

    summary_template = """
        given the information {information} about a person from I want to create:
         1. a short summary
         2. two interesting facts about them
    """

    summary_prompt_template=PromptTemplate(input_variables=["information"],template=summary_template)
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, api_key=openai_api_key)

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile("https://www.linkedin.com/in/suneel-kanuri-2253667970/",mock=True)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)


