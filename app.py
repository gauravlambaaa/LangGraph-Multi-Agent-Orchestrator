
"""Entrypoint for the LangGraph-style orchestrator.

Simple CLI:
- Accepts a query
- Runs a fixed set of agents in order
- Supports human approval at the verifier step
- Prints final report to stdout
"""

import os
from dotenv import load_dotenv
from orchestrator.graph_def import AGENT_MAP, ORDER
from orchestrator.memory import Memory

load_dotenv()

def run_pipeline(query: str, human_approval: bool = False):
    mem = Memory()
    context = {'query': query}
    for step in ORDER:
        agent = AGENT_MAP[step]
        print(f"[orchestrator] Running agent: {agent.name}")
        try:
            out = agent.run(context)
            if not isinstance(out, dict):
                raise RuntimeError("Agent output must be a dict")
            context.update(out)
            mem.update(agent.name, out)

            if agent.name == 'verifier' and human_approval:
                approval = input("Approve verification (y/n)? ").strip().lower()
                if approval != 'y':
                    print("Human rejected verification. Aborting pipeline.")
                    return {'status': 'rejected', 'context': context}

        except Exception as e:
            print(f"[orchestrator] Agent {agent.name} failed: {e}")
            # single retry attempt
            try:
                out = agent.run(context)
                context.update(out)
            except Exception as e2:
                print("[orchestrator] Retry failed, aborting pipeline.")
                return {'status': 'failed', 'error': str(e2), 'context': context}
    return {'status': 'success', 'result': context}

if __name__ == '__main__':
    q = input('Enter a research query: ').strip()
    human = input('Enable human approval at verifier step? (y/n): ').strip().lower() == 'y'
    res = run_pipeline(q, human_approval=human)
    print('\n===== Pipeline Result =====')
    import json
    print(json.dumps(res, indent=2))
