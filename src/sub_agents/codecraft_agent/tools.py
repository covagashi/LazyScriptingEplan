# src/sub_agents/codecraft_agent/tools.py
from ai.optimized_rag import ScriptRAG
from src.ai.documentation_rag import DocumentationRAG
import time
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Global singleton instances
_script_rag = None
_doc_rag = None

def _get_script_rag():
    global _script_rag
    if _script_rag is None:
        _script_rag = ScriptRAG()
    return _script_rag

def _get_doc_rag():
    global _doc_rag
    if _doc_rag is None:
        _doc_rag = DocumentationRAG()
    return _doc_rag

def generate_eplan_script(requirements: str, context: str = "") -> str:
    """Generate complete C# EPLAN script with error handling"""
    try:
        # Get relevant examples and docs
        script_rag = _get_script_rag()
        doc_rag = _get_doc_rag()
        
        examples = script_rag.search_scripts_sync(requirements, top_k=2)
        docs = doc_rag.search_documentation(requirements, top_k=2)
        
        # Create enhanced script template
        timestamp = int(time.time())
        script_template = f'''using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.DataModel;
using System;

public class GeneratedScript_{timestamp}
{{
   [Start]
   public void StartScript()
   {{
       try 
       {{
           new BaseException("Script START: {requirements}", MessageLevel.Message).FixMessage();
           
           // TODO: Implement {requirements}
           {_generate_implementation_code(examples, docs, requirements)}
           
           new BaseException("Script COMPLETE: Task finished successfully", MessageLevel.Message).FixMessage();
       }}
       catch (Exception ex)
       {{
           new BaseException($"Script ERROR: {{ex.Message}}", MessageLevel.Error).FixMessage();
           throw;
       }}
   }}
}}'''
        
        return script_template
        
    except Exception as e:
        logger.error(f"Error in generate_eplan_script: {e}")
        return f"Error generating script: {str(e)}. Please try with different requirements."

def _generate_implementation_code(examples, docs, requirements):
    """Generate implementation based on examples and docs"""
    if examples:
        # Extract patterns from examples
        example_code = examples[0]['document'].get('example', {}).get('script', [])
        if example_code:
            return f"// Based on example: {examples[0]['document']['example'].get('name', 'Unknown')}\n            " + "\n            ".join(example_code[5:15])
    
    return f"// Implementation for: {requirements}\n            // Add your EPLAN automation logic here"

def save_script_to_file(content: str, filename: str = "") -> str:
    """Save generated script to filesystem"""
    try:
        if not filename: 
            timestamp = int(time.time())
            filename = f"generated_script_{timestamp}.cs"
        
        output_dir = Path("C:/temp/Agent")
        output_dir.mkdir(exist_ok=True)
        
        script_file = output_dir / filename
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Script saved to: {script_file}"
        
    except Exception as e:
        logger.error(f"Error in save_script_to_file: {e}")
        return f"Error saving script: {e}"

def enhance_script_with_context(script: str, knowledge_context: str, examples_context: str) -> str:
    """Enhance script with knowledge and examples context"""
    try:
        enhanced_script = script
        
        # Add relevant API calls from knowledge context
        if "API" in knowledge_context:
            enhanced_script += f"\n\n// Relevant API documentation:\n// {knowledge_context[:200]}..."
        
        # Add pattern improvements from examples
        if "Pattern" in examples_context:
            enhanced_script += f"\n\n// Similar pattern found:\n// {examples_context[:200]}..."
        
        return enhanced_script
        
    except Exception as e:
        logger.error(f"Error in enhance_script_with_context: {e}")
        return script  # Return original if enhancement fails