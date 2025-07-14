# 🩺 Doctor Conference Email Generator (CrewAI + Composio + Web Scraping)

This AI-powered automation tool fetches upcoming doctor conferences based on medical specialty and date range, summarizes them, and sends personalized invitation emails to relevant doctors — all using intelligent CrewAI agents, web scraping, and Composio’s email automation.

---

## 📌 Project Objective

Streamline outreach to medical professionals by:

- Finding upcoming doctor conferences in the USA based on specialty and months
- Summarizing and structuring the findings
- Auto-emailing personalized invitations to the appropriate doctors

---

## 🧠 What It Does

🔹 Searches the web for conferences using:
  - `SerperDevTool` (Google Search)
  - `ScrapeWebsiteTool`  
🔹 Summarizes and compiles a report using LLM agents  
🔹 Uses Composio’s Gmail API to send a well-formatted invitation email to doctors  

---

## ⚙️ Tech Stack

- 🧠 [CrewAI](https://github.com/joaomdmoura/crewai)
- ✉️ [Composio](https://www.composio.dev/) for Gmail integration
- 🌐 Web scraping via Serper & CrewAI tools
- 📄 Excel (email list input)
- 🐍 Python, Pydantic, dotenv
