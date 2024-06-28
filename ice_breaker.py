from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
import os

information = """
Muhammad Yunus (born 28 June 1940) is a Bangladeshi social entrepreneur, banker, economist and civil society leader who was awarded the Nobel Peace Prize in 2006 for founding the Grameen Bank and pioneering the concepts of microcredit and microfinance.[1] These loans are given to entrepreneurs that are too poor to qualify for traditional bank loans. Yunus and the Grameen Bank were jointly awarded the Nobel Peace Prize "for their efforts through microcredit to create economic and social development from below". The Norwegian Nobel Committee said that "lasting peace cannot be achieved unless large population groups find ways in which to break out of poverty" and that "across cultures and civilizations, Yunus and Grameen Bank have shown that even the poorest of the poor can work to bring about their own development".[2] Yunus has received several other national and international honours. He received the United States Presidential Medal of Freedom in 2009 and the Congressional Gold Medal in 2010.[3]

In February 2011, Yunus together with Saskia Bruysten, Sophie Eisenmann and Hans Reitz co-founded Yunus Social Business – Global Initiatives (YSB). YSB creates and empowers social businesses to address and solve social problems around the world. As the international implementation arm for Yunus' vision of a new, humane capitalism, YSB manages incubator funds for social businesses in developing countries and provides advisory services to companies, governments, foundations and NGOs.

In 2012, he became Chancellor of Glasgow Caledonian University in Scotland, a position he held until 2018.[4][5] Previously, he was a professor of economics at Chittagong University in Bangladesh.[6] He published several books related to his finance work. He is a founding board member of Grameen America and Grameen Foundation, which support microcredit.

Yunus also served on the board of directors of the United Nations Foundation, a public charity to support UN causes, from 1998 to 2021.[7]
"""

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
    res = chain.invoke(input={"information": information})

    print(res)


