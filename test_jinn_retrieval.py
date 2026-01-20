from qusai_core.ontology.engine import OntologyEngine
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)

def test_retrieval():
    print("Initializing Engine...")
    engine = OntologyEngine()
    engine.load()
    
    query = "Tell me what the topological forms of Jinn are"
    print(f"\nQuery: {query}")
    
    context = engine.get_context(query)
    
    print("\n--- Retrieved Context ---")
    print(context if context else "No context found.")
    
    if "root:jnn" in context:
        print("\n✅ SUCCESS: Found 'root:jnn' in context.")
    else:
        print("\n❌ FAILURE: Did not find 'root:jnn'.")

if __name__ == "__main__":
    test_retrieval()

