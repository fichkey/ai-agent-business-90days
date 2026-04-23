!pip install langchain_groq
!pip install typing
!pip install langchain
!pip install langchain_core
!pip install pydantic

from langchain_groq import ChatGroq
from  langchain_core.tools import tool
from typing import Optional, List
from pydantic import BaseModel, Field
import os

llama3 = ChatGroq (temperature = 0.2
                     api_key = os.getenv (groqapikey), #for security reasons actual groqkey is omitted from the github file
                     model = "meta-llama/llama-4-scout-17b-16e-instruct",
                    )               
#stopped here


class Market_Research (BaseModel) :
  executive_summary : str = Field (description = "Write a detailed Executive Summary like in a consulting report. Use real numbers and a detailed analysis")
  key_pain_points: List[str] = Field (description = "List at least six pain points with enough details on the pain point.")
  moat_opportunities: List [str] = Field (description = "List at least 6-8 competitive advantages. Base them on deep research and analysis")
  gtm_recommendations:  List [str] = Field (description = "Give detailed and practical recommendations for Cogneesol.")
  realistic_addressable_market_range : str = Field (description = "Give a realistic number range for middle-market agency migrations per year (e.g. 100-300). Base it on real industry data.")

Market_Research.schema()

structured__mktresearch_llama3 = llama3.with_structured_output (Market_Research)

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import SimpleJsonOutputParser, JsonOutputParser

prompt = PromptTemplate.from_template ("""
                                       You are an expert data parser, parse data from user query. Use this schema:
                                       {schema}
                                       Respond only as JSON based on above-mentioned schema. Strictly follow JSON Schema and do not add any extra fields. 
                                       If you do not know any field, then set it to None.
                                       {query}
                                       """)


llm = prompt | llama3 |SimpleJsonOutputParser()
result = llm.invoke({
    "schema": Market_Research.schema(),                    
    "query": """You are an elite market researcher with specialization on insurance brokerages. You have over 25 years experience in the industry.
Task: Create a market research on insurance policy data migration from one backend system to another during an acquisition of an insurance agency.
Context: you are researching insurance agencies that are very active in acquiring other insurance agencies. You should outline a comprehensive list of scenarios of acquisitions (e.g. agency acquisition, book of business acquisition, etc.). You should outline the motivation for these acquisitions. You should segment the acquisition, You should outline pain points during such acquisitions. You should outline all players in such an acquisition. Your focus should be M&A between middle-sized agencies. You should segment the acquisition, by geography, type of business, Line of insurance business. You should have a section on pain points of migrating policy data, and current approaches agencies are taking. You should identify possible MOATs for someone offering migration services. You should include recommendations for go to market strategies. Your audience are executives at Cogneesol, looking to create strategy, targeting agencies for data migration services. Your audience is proficient in insurance and technology. Your audience has very little connections among insurance agencies.
Format: Easy to read report, maximum of 10 pages.
Examples: This is a sample of a good report. https://3409306.fs1.hubspotusercontent-na1.net/hubfs/3409306/Go-No-Go-Guide-to-Market-Expansion.pdf . keep in mind that this is an example for formatting, but it’s not on the subject you’re researching. Do not take any of the report’s content into consideration.
Constraints: Do not make it basic. Do not focus on extra large brokerages. Do not focus on insurance carriers M&A."""
})

mkt_research_json = (prompt | llama3).invoke ({"query": """You are an elite market researcher with specialization on insurance brokerages. You have over 25 years experience in the industry.
Task: Create a market research on insurance policy data migration from one backend system to another during an acquisition of an insurance agency.
Context: you are researching insurance agencies that are very active in acquiring other insurance agencies. You should outline a comprehensive list of scenarios of acquisitions (e.g. agency acquisition, book of business acquisition, etc.). You should outline the motivation for these acquisitions. You should segment the acquisition, You should outline pain points during such acquisitions. You should outline all players in such an acquisition. Your focus should be M&A between middle-sized agencies. You should segment the acquisition, by geography, type of business, Line of insurance business. You should have a section on pain points of migrating policy data, and current approaches agencies are taking. You should identify possible MOATs for someone offering migration services. You should include recommendations for go to market strategies. Your audience are executives at Cogneesol, looking to create strategy, targeting agencies for data migration services. Your audience is proficient in insurance and technology. Your audience has very little connections among insurance agencies.
Format: Easy to read report, maximum of 10 pages.
Examples: This is a sample of a good report. https://3409306.fs1.hubspotusercontent-na1.net/hubfs/3409306/Go-No-Go-Guide-to-Market-Expansion.pdf . keep in mind that this is an example for formatting, but it’s not on the subject you’re researching. Do not take any of the report’s content into consideration.
Constraints: Do not make it basic. Do not focus on extra large brokerages. Do not focus on insurance carriers M&A.""", "schema": Market_Research.schema_json()})

print (mkt_research_json.content)



                            
