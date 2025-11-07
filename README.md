 Doctor Conference Email Generator (CrewAI + Composio + Web Scraping)

This AI-powered automation tool fetches upcoming doctor conferences based on medical specialty and date range, summarizes them, and sends personalized invitation emails to relevant doctors — all using intelligent CrewAI agents, web scraping, and Composio’s email automation.

DEMO LINK
https://www.loom.com/share/c72e88081207456993f82b7e4938eb06

This video was created as a real-world web-research use case for a company, demonstrating how AI agents can replicate research and outreach workflows efficiently. 
Using this idea, we can integrate the work flow into different domains utilizing the necessary API's and by modifying agents according to the use case.

Streamline outreach to medical professionals by:
- Finding upcoming doctor conferences in the USA based on specialty and months
- Summarizing and structuring the findings
- Auto-emailing personalized invitations to the appropriate doctors

Working:
* Searches the web for conferences using:
  - `SerperDevTool` (Google Search)
  - `ScrapeWebsiteTool`  
* Summarizes and compiles a report using LLM agents
* Uses Gmail SMTP to send a well-formatted invitation email to doctors  


Tech Stack
- CrewAI
- Gmail SMTP for Gmail integration / [Composio](https://www.composio.dev/) can also be used
- Web scraping via Serper & CrewAI tools
- Excel (email list input)
- Python, Pydantic, dotenv
