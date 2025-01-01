from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

information = """
    John Breth is an Experienced architect, author, and IT consulting firm founder with a demonstrated history of working in the information technology and services industry. 
    Skilled in IT Strategy, Information Assurance, Information Security, Enterprise Architecture, and Systems Engineering. 
    Strong business development professional with a Master of Science (MS) focused in Information Technology from The Johns Hopkins University - Carey Business School. 
    """

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)
