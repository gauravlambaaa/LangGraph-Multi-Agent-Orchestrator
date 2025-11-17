
"""Agent implementations.

Each agent is a simple wrapper around a LangChain LLMChain using a prompt template.
Design keeps concerns separated so agents can be unit-tested individually.
"""
import os
from typing import Dict, Any
from dotenv import load_dotenv
from langchain import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def get_llm(temperature: float = 0.0):
    # LangChain's OpenAI reads the OPENAI_API_KEY from env automatically
    return OpenAI(temperature=temperature)

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

class ResearchAgent(BaseAgent):
    PROMPT = PromptTemplate.from_template("""
You are a concise research assistant. Given a query: {query}
Output in three sections labeled FACTS, SOURCES, KEYWORDS.
FACTS: 5 short bullet points.
SOURCES: 3 credible source suggestions (url or search query).
KEYWORDS: 5 keywords.
""")

    def __init__(self):
        super().__init__('research')
        self.chain = LLMChain(llm=get_llm(0.0), prompt=self.PROMPT)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        query = context.get('query', '')
        output = self.chain.run(query=query)
        return {'research': output}

class SummarizerAgent(BaseAgent):
    PROMPT = PromptTemplate.from_template("""
You are a summarizer. Summarize the research notes into a 6-sentence summary.
Input: {research}
""")

    def __init__(self):
        super().__init__('summarizer')
        self.chain = LLMChain(llm=get_llm(0.0), prompt=self.PROMPT)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        research = context.get('research', '')
        out = self.chain.run(research=research)
        return {'summary': out}

class VerifierAgent(BaseAgent):
    PROMPT = PromptTemplate.from_template("""
You are a verifier. Given the summary and research notes, produce 3 checks and mark each as OK or SUSPECT with short reasoning.
Summary: {summary}
Research: {research}
""")

    def __init__(self):
        super().__init__('verifier')
        self.chain = LLMChain(llm=get_llm(0.0), prompt=self.PROMPT)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        summary = context.get('summary', '')
        research = context.get('research', '')
        out = self.chain.run(summary=summary, research=research)
        return {'verification': out}

class WriterAgent(BaseAgent):
    PROMPT = PromptTemplate.from_template("""
Produce a 300-500 word report using the summary and verification notes. Include a title and a short conclusion.
Summary: {summary}
Verification: {verification}
""")

    def __init__(self):
        super().__init__('writer')
        self.chain = LLMChain(llm=get_llm(0.0), prompt=self.PROMPT)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        summary = context.get('summary', '')
        verification = context.get('verification', '')
        out = self.chain.run(summary=summary, verification=verification)
        return {'report': out}
