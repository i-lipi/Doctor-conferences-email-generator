from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from composio_crewai import ComposioToolSet,Action, App

from crewai_tools import SerperDevTool, ScrapeWebsiteTool

import os
import sys
from dotenv import load_dotenv

load_dotenv()

composio_toolset = ComposioToolSet(api_key=os.getenv('COMPOSIO_API_KEY'))

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pydantic")



email_tool = composio_toolset.get_tools(actions=['GMAIL_SEND_EMAIL'])


@CrewBase
class Ws():
    """Ws crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose= True
        
    )

    @agent
    def reporter(self) -> Agent:
        return Agent(
            config=self.agents_config["reporter"],
            tools=[ScrapeWebsiteTool()],
            verbose= True
    )
    @agent 
    def email_sender(self) -> Agent:
        return Agent(
            config=self.agents_config['email_sender'],
            tools=email_tool,
            verbose=True
    )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"]   
    )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
            output_file="output_research.md"
    )

    @task
    def email_task(self) -> Task:
        return Task(
            config=self.tasks_config["email_task"],
            inputs={"email_list": "{email_list}", "specialty": "{specialty}"}
    )
   

    @crew
    def crew(self) -> Crew:
        """Creates the Ws crew"""
    
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True)