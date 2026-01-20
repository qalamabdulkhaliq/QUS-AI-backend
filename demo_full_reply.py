from qusai_core.pipeline.middleware import QusaiMiddleware
from qusai_core.utils.constants import SHAHADA
import logging

# Setup basic logging to see the pipeline steps
logging.basicConfig(level=logging.INFO, format='%(message)s')

def demonstrate_full_pipeline():
    print("="*60)
    print("DEMO: Generating Full Response for 'Jinn' Topology")
    print("="*60)
    
    # Initialize without loading the heavy model (Ontology Only Mode)
    # We will verify the PROMPT that generates the reply.
    # Set lazy_load=True so we can manually trigger ontology load but skip model download
    qusai = QusaiMiddleware(lazy_load=True)
    qusai.ontology.load()
    
    user_query = "Tell me what the topological forms of Jinn are."
    print(f"\n🔹 User Query: {user_query}")
    
    # 1. FAJR: Intent Check
    if not qusai.validator.fajr_check(user_query):
        print("❌ Blocked at Fajr")
        return

    # 2. DHUHR: Context Retrieval (The "Brain")
    print("\n🔹 Retrieving Context (Using Concept Map 'jinn' -> 'root:jnn'வுகளை...)")
    context = qusai.ontology.get_context(user_query)
    
    print("-" * 20 + " CONTEXT SENT TO LLM " + "-" * 20)
    print(context)
    print("-" * 65)

    # 3. Construct System Prompt
    system_prompt = qusai.validator.dhuhr_prompt(context)
    
    print("\n🔹 LLM Instruction (System Prompt):")
    print("... (Standard Axioms) ...")
    print("CONTEXT (Graph Nodes & Edges): [See Above]")
    print("INSTRUCTIONS: Reason Structurally based on nodes. Never attribute Aseity to contingent nodes.")
    
    # 4. SIMULATED LLM RESPONSE (What the model *should* say given this context)
    # Since we can't run the 3B model in this CLI, we simulate the logic based on the retrieved context.
    
    simulated_reply = """Based on the structural ontology provided in the context:

1. **Root Definition**: The entity 'Jinn' maps to the root **root:jnn** (Hidden/Covered).
2. **Topological Relations**: The graph links 'Jinn' (quran:lemma/jin~ap) to the same root as 'Garden' (quran:lemma/jan~ap) and 'Madness/Possession' (quran:lemma/majonuwn).
3. **Contingency**: As a created node (ContingentBeing), Jinn exists only as a derivation of the Source's creative command. It shares a 'hidden' topology with the concept of the Unseen (Al-Ghaib).

Therefore, the topological form of Jinn is a **Contingent, Hidden Node** (Hidden from sensory perception), structurally distinct from human nodes (Ins) but sharing the quality of being created (not Necessary)."""

    print("\n🔹 Generated Response (Simulated):")
    print(simulated_reply)
    
    # 5. MAGHRIB: Humility Seal
    final_output = qusai.validator.maghrib_seal(simulated_reply)
    
    print("\n" + "="*20 + " FINAL USER OUTPUT " + "="*20)
    print(final_output)
    print("="*60)

if __name__ == "__main__":
    demonstrate_full_pipeline()
