import logging
import gradio as gr
import os
try:
    import spaces
except ImportError:
    # Fallback for local testing without 'spaces'
    class spaces:
        @staticmethod
        def GPU(func):
            return func

from qusai_core.pipeline.middleware import QusaiMiddleware

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Initialize Middleware with Transformers (GPU Native)
# We use the standard HF repo now, not GGUF
middleware = QusaiMiddleware(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    lazy_load=False
)

@spaces.GPU(duration=120) # Request GPU for up to 120s per generation
def chat_interface(message, history, arabic_only):
    if arabic_only:
        message = f"{message} (Please answer strictly in Arabic / العربية)"
    return middleware.process_query(message)

# Gradio UI
with gr.Blocks(title="QUSAI v2 - Mizan") as demo:
    gr.Markdown("# 🕌 QUSAI v2 - Mizan (Pro Tier)")
    gr.Markdown("""
    **System Status:**
    - ✅ **Model**: Qwen 2.5 7B Instruct (ZeroGPU/A100 Accelerated)
    - ✅ **Ontology**: v3 Root Topology + Granular Reasoning Engine
    - ✅ **Bridge**: Universal Concept Map (Active)
    
    *Engineered for Ontological Weighing of Speculative Concepts (e.g., Aliens vs. Jinn).*
    """)
    
    with gr.Row():
        arabic_check = gr.Checkbox(label="Output in Arabic Only (مخرجات عربية فقط)", value=False)
    
    chatbot = gr.ChatInterface(
        fn=chat_interface,
        additional_inputs=[arabic_check],
        type="messages"
    )

if __name__ == "__main__":
    demo.launch()
