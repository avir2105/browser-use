from browser_use import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr
import os
import asyncio
from browser_use import BrowserConfig
from browser_use import Agent, Browser, BrowserConfig
 
 
# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key="AIzaSyDZUYR1M1SCC_1sRctEPByst6Z_6Nmsla4")
 
 
browser = Browser(
    config = BrowserConfig(
        chrome_instance_path="C:\Program Files\Google\Chrome\Application\chrome"
    )
)
 
agent = Agent(
    task="open chrome,search github and click on avir2105/GPU_Memory repository and click on issues",
    llm=llm,
    browser=browser,
)
 
async def main():
    await agent.run()
 
    input('Press Enter to close the browser...')
    await browser.close()
 
if __name__ == '__main__':
    asyncio.run(main())