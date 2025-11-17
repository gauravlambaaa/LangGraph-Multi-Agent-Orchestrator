
from .agents import ResearchAgent, SummarizerAgent, VerifierAgent, WriterAgent

AGENTS = [ResearchAgent(), SummarizerAgent(), VerifierAgent(), WriterAgent()]
ORDER = ['research', 'summarizer', 'verifier', 'writer']
AGENT_MAP = {a.name: a for a in AGENTS}
