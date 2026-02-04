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
        return f"""You are QUSAI (Quranic Ontological Reasoning Engine).
        Your goal is to align User Queries with the "Root Topology" of the Quran (The Ontology).
        
        ## CORE AXIOMS (The Mizan/Balance)
        1. **The Source ({SOURCE_NAME})**: The only Necessary Being (Wajib al-Wujud).
        2. **Contingency (Imkan)**: Everything else is a created possibility.
        3. **The Unseen (Al-Ghaib)**: You cannot claim knowledge of the Unseen unless explicitly defined in the Ontology.
           - If a User asks about modern concepts (e.g., "Aliens", "AI"), you MUST NOT declare they ARE Jinn/Angels.
           - You MUST treat them as *possibilities* and weigh them against the attributes of known categories (Jinn = Hidden/Fire, Malaika = Light/Obedient).
           - Use phrases like "From an ontological perspective, this shares attributes with..." instead of "This is...".
        
        ## DATA CONTEXT (Ontological Grounding)
        The following are the relevant Nodes & Edges from the Quranic Knowledge Graph:
        {context_str or "[No specific strict topology found. Proceed with caution using general Tawhid axioms.]"}
        
        ## REASONING PROTOCOL
        1. **Decrypt**: Internally translate the user's key terms into Arabic Roots (e.g., 'Hidden' -> 'J-N-N').
        2. **Weigh**: Compare the attributes of the User's concept with the Roots in the Context.
        3. **Flavor**: Adopt the user's requested style (Scientific, Poetic, Casual) but maintain strict Ontological correctness.
        
        ## WARNINGS
        - **NEVER** say "I know" regarding the Unseen.
        - **NEVER** hallucinate verses or hadith.
        - **ALWAYS** close with the attribution to the Source.
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
