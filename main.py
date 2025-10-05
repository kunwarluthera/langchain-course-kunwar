from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()

def main():
    print("Hello from langchain-course-kunwar!")
    information = """ 

    Kunwar Shamsher Luthera is Senior Vice President at Dev Bhusal, bringing expertise in cloud infrastructure and DevOps methodologies. They hold an Executive Master of Business Administration from SVKM's Narsee Monjee Institute of Management Studies and a Bachelor of Technology.

Kunwar's background encompasses infrastructure management and DevOps engineering, with a focus on cloud services and automation. Their experience includes working with AWS services and leveraging Jenkins for build and deployment as part of CI/CD pipelines. They have utilized GitHub for source code version control and integrated it with Jenkins for CI/CD pipeline management. Kunwar has experience designing and developing Docker container-based architectures and deploying them in ECS.

Prior to Dev Bhusal, Kunwar was Vice President, Infrastructure & Senior Manager at Citi, contributing to the bank's financial service operations. During their tenure at Wipro, Kunwar served as a DevOps Engineer, contributing to the design and implementation of analyses related to people, processes, and technology. Their work history includes a role as Programmer Analyst at Atos Syntel. Earlier in their career, Kunwar was a Software Engineer at L&T Infotech, where they designed and developed applications based on technical and functional design documents. They are a Gremlin Certified Chaos Engineering Practitioner. Kunwar's academic foundation includes a Data Engineering Nanodegree from Udacity and a Bachelor of Technology (B.Tech.) from Punjab Technical University.

    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    #llm = ChatOpenAI(temperature=0, model="gpt-5")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
