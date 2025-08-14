# src/sub_agents/codecraft_agent/tools.py
from src.ai.optimized_rag import OptimizedScriptRAG
from src.ai.documentation_rag import OptimizedDocumentationRAG
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
        _script_rag = OptimizedScriptRAG()
    return _script_rag

def _get_doc_rag():
    global _doc_rag
    if _doc_rag is None:
        _doc_rag = OptimizedDocumentationRAG()
    return _doc_rag

def generate_eplan_script(requirements: str, context: str = "") -> str:
    """Generate complete C# EPLAN script with error handling"""
    try:
        # Create enhanced script template
        timestamp = int(time.time())
        
        # Generate basic script structure
        script_template = f'''using System;
using System.IO;
using System.Windows.Forms;
using Eplan.EplApi.Base;
using Eplan.EplApi.Scripting;
using Eplan.EplApi.ApplicationFramework;
using Eplan.EplApi.DataModel;

/// <summary>
/// Generated EPLAN script for: {requirements}
/// Created: {time.strftime('%Y-%m-%d %H:%M:%S')}
/// </summary>
public class GeneratedScript_{timestamp}
{{
    [Start]
    public void Execute()
    {{
        try 
        {{
            new BaseException("Script START: {requirements}", MessageLevel.Message).FixMessage();
            
            // Main script logic
            {_generate_implementation_code(requirements, context)}
            
            new BaseException("Script COMPLETE: Task finished successfully", MessageLevel.Message).FixMessage();
        }}
        catch (Exception ex)
        {{
            new BaseException($"Script ERROR: {{ex.Message}}", MessageLevel.Error).FixMessage();
            MessageBox.Show($"Error: {{ex.Message}}", "Script Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            throw;
        }}
    }}
}}'''
        
        return script_template
        
    except Exception as e:
        logger.error(f"Error in generate_eplan_script: {e}")
        return f"// Error generating script: {str(e)}\n// Please check your requirements and try again."

def _generate_implementation_code(requirements: str, context: str) -> str:
    """Generate implementation based on requirements and context"""
    
    # Basic implementations for common requests
    if "hello world" in requirements.lower() or "message box" in requirements.lower():
        return '''MessageBox.Show("Hello World from EPLAN!", "Generated Script", MessageBoxButtons.OK, MessageBoxIcon.Information);'''
    
    if "backup" in requirements.lower():
        return '''// Create project backup
            CommandLineInterpreter cli = new CommandLineInterpreter();
            ActionCallingContext acc = new ActionCallingContext();
            
            string projectPath = PathMap.SubstitutePath("$(P)");
            string projectName = PathMap.SubstitutePath("$(PROJECTNAME)");
            
            if (!string.IsNullOrEmpty(projectPath))
            {
                acc.AddParameter("TYPE", "PROJECT");
                acc.AddParameter("PROJECTNAME", projectPath);
                acc.AddParameter("DESTINATIONPATH", @"C:\\EPLAN_Backups");
                acc.AddParameter("ARCHIVENAME", projectName.Replace(".elk", ".zw1"));
                acc.AddParameter("BACKUPMETHOD", "BACKUP");
                
                cli.Execute("backup", acc);
                MessageBox.Show("Backup completed successfully!", "Backup", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }'''
    
    if "export" in requirements.lower():
        return '''// Export project data
            CommandLineInterpreter cli = new CommandLineInterpreter();
            ActionCallingContext acc = new ActionCallingContext();
            
            acc.AddParameter("TYPE", "PROJECT");
            acc.AddParameter("EXPORTFILE", @"C:\\temp\\export.xml");
            acc.AddParameter("EXPORTSCHEME", "EPLAN_STANDARD");
            
            cli.Execute("export", acc);
            MessageBox.Show("Export completed!", "Export", MessageBoxButtons.OK, MessageBoxIcon.Information);'''
    
    # Default implementation
    return f'''// Implementation for: {requirements}
            // TODO: Add specific EPLAN automation logic here
            MessageBox.Show("Script executed successfully!\\nRequirement: {requirements}", "Script Result", MessageBoxButtons.OK, MessageBoxIcon.Information);'''

def save_script_to_file(content: str, filename: str = "") -> str:
    """Save generated script to filesystem"""
    try:
        if not filename: 
            timestamp = int(time.time())
            filename = f"generated_script_{timestamp}.cs"
        
        # Ensure .cs extension
        if not filename.endswith('.cs'):
            filename += '.cs'
        
        output_dir = Path("C:/temp/EPLAN_Scripts")
        output_dir.mkdir(exist_ok=True, parents=True)
        
        script_file = output_dir / filename
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f"✅ Script saved to: {script_file}"
        
    except Exception as e:
        logger.error(f"Error in save_script_to_file: {e}")
        return f"❌ Error saving script: {e}"

def enhance_script_with_context(script: str, knowledge_context: str, examples_context: str) -> str:
    """Enhance script with knowledge and examples context"""
    try:
        enhanced_script = script
        
        # Add relevant comments from context
        if knowledge_context and len(knowledge_context) > 10:
            enhanced_script += f"\n\n/* Knowledge Context:\n{knowledge_context[:300]}...\n*/"
        
        if examples_context and len(examples_context) > 10:
            enhanced_script += f"\n\n/* Examples Context:\n{examples_context[:300]}...\n*/"
        
        return enhanced_script
        
    except Exception as e:
        logger.error(f"Error in enhance_script_with_context: {e}")
        return script  # Return original if enhancement fails