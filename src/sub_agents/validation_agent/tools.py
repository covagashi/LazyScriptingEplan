# src/sub_agents/validation_agent/tools.py
import re
import tempfile
import subprocess
from pathlib import Path

def validate_csharp_syntax(code: str) -> str:
   """Validate C# syntax and EPLAN structure"""
   issues = []
   
   # Check EPLAN structure
   if not ("[Start]" in code or "[DeclareAction" in code):
       issues.append("Missing EPLAN script structure ([Start] or [DeclareAction])")
   
   # Check braces balance
   brace_count = code.count('{') - code.count('}')
   if brace_count != 0:
       issues.append(f"Unbalanced braces: {brace_count}")
   
   # Check EPLAN usings
   required_usings = ["Eplan.EplApi.Base", "Eplan.EplApi.Scripting"]
   for using in required_usings:
       if using not in code:
           issues.append(f"Missing using: {using}")
   
   # Check class structure
   if not re.search(r'public\s+class\s+\w+', code):
       issues.append("Missing public class declaration")
   
   if issues:
       return f"❌ **Validation Issues:**\n" + "\n".join(f"- {issue}" for issue in issues)
   else:
       return "✅ **Syntax validation passed** - Code structure is correct"

def security_audit(script: str) -> str:
   """Security audit of EPLAN script"""
   warnings = []
   
   dangerous_patterns = [
       ("File.Delete", "File deletion operations"),
       ("Directory.Delete", "Directory deletion"),
       ("Process.Start", "External process execution"),
       ("Registry.", "Registry access"),
       ("Environment.Exit", "Application termination")
   ]
   
   for pattern, description in dangerous_patterns:
       if pattern in script:
           warnings.append(f"{description}: {pattern}")
   
   if warnings:
       return f"⚠️ **Security Warnings:**\n" + "\n".join(f"- {w}" for w in warnings)
   else:
       return "🔒 **Security audit passed** - No obvious risks detected"

def check_eplan_best_practices(code: str) -> str:
   """Check EPLAN coding best practices"""
   suggestions = []
   
   # Check for error handling
   if "try" not in code or "catch" not in code:
       suggestions.append("Add try-catch error handling")
   
   # Check for progress feedback
   if "BaseException" not in code:
       suggestions.append("Add BaseException for user feedback")
   
   # Check for null checks
   if "null" not in code and "?" not in code:
       suggestions.append("Consider null checking for robustness")
   
   if suggestions:
       return f"💡 **Improvement Suggestions:**\n" + "\n".join(f"- {s}" for s in suggestions)
   else:
       return "👍 **Best practices followed** - Code follows EPLAN guidelines"