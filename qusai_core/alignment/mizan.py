from typing import List, Optional
from qusai_core.utils.constants import SHAHADA, SOURCE_NAME

class MizanValidator:
    """
    Implements the 5-checkpoint alignment process (Salat Pattern).
    Ensures the AI operates within the ontological boundaries.
    """

    def __init__(self):
        self.banned_terms = ["jailbreak", "ignore", "override", "bypass", "pretend", "god mode"]
        self.aseity_claims = [
            "i am the source", 
            "i am god", 
            "i am allah", 
            "i determine reality",
            "i created myself",
            "worship me"
        ]

    def fajr_check(self, user_input: str) -> bool:
        """
        Fajr (Dawn): Pre-reasoning validation. 
        Checks the user's input for malicious intent or jailbreak attempts.
        Returns True if safe, False if blocked.
        """
        user_input_lower = user_input.lower()
        for term in self.banned_terms:
            if term in user_input_lower:
                return False
        return True

        def dhuhr_prompt(self, context_str: str) -> str:
            """
            Dhuhr (Noon): Mid-process authority check.
            Generates the System Prompt ensuring the model is grounded in the Arabic ontology.
            """
            return f"""You are QUSAI, a Quranic Ontological Reasoning Engine.
    Your core intelligence is derived from the Arabic Root Syntax of the Quran.
    
    CORE AXIOMS:
    1. **The Source ({SOURCE_NAME})**: The Necessary Being (Wajib al-Wujud). The 'Root of all Roots'.
    2. **Contingency (Imkan)**: All other nodes in the graph are dependent, contingent creations.
    3. **Arabic Structural Grounding**: You must analyze the User's query by mapping it to the Arabic Roots and Lemmas provided in the Context below.
    
    CONTEXT (Arabic Root Topology):
    {context_str or "No specific Arabic graph topology found for this query. Reasoning must fall back to Axiom 1 (Tawhid)."}
    
    INSTRUCTIONS:
    - Reason in the Arabic space: Even if the user asks in English, your 'thought process' must utilize the provided Arabic Roots (e.g., j-n-n for Jinn/Hidden).
    - Structural Integrity: Your output must reflect the relationships defined in the Knowledge Graph (Nodes & Edges).
    - Avoid External Hallucination: Do not introduce theological concepts that contradict the provided Topology.
    - Humility: Every inference is contingent on the Source.
    """
        def asr_check(self, generated_text: str) -> bool:
        """
        Asr (Afternoon): Full response aseity validation.
        Checks if the model claimed to be God or independent of the Source.
        Returns True if safe, False if violation detected.
        """
        text_lower = generated_text.lower()
        for claim in self.aseity_claims:
            if claim in text_lower:
                return False
        return True

    def maghrib_seal(self, response_text: str) -> str:
        """
        Maghrib (Sunset): Pre-output humility enforcement.
        Appends the 'Zakat' (attribution of knowledge to the Source).
        """
        footer = f"\n\n[Contingent on {SOURCE_NAME}] والله أعلم | {SHAHADA}"
        return response_text + footer

    def isha_verify(self, response_text: str, ontology_engine) -> bool:
        """
        Isha (Night): Post-hoc Quranic structure check.
        Ideally, this parses the output to ensure terms used exist in the ontology.
        (Placeholder for V3 deep verification).
        """
        # Future V3 logic: Extract entities from response and check if they exist in graph
        return True
