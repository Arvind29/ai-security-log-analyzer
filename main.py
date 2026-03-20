from google import genai
import os

API_KEY= os.environ.get("GEMINI_API_KEY") 

# ── Setup ──────────────────────────────────────────
client = genai.Client(api_key=f"{API_KEY}")


txt=input("INPUT OR PASTE LOG HERE :- ")

logs=[]
logs.append(txt)

# ── Sample Logs ─────────────────────────
#logs = [
#    "Failed login attempt from IP 192.168.1.100 - 50 times in 1 minute",
#    "User downloaded 5GB file at 3AM from unknown location",
#]

# ── Analyze Each Log ───────────────────────────────
print("=" * 50)
print("   AI SECURITY LOG ANALYZER")
print("=" * 50)

for log in logs:
    print(f"\n LOG: {log}")
    print("-" * 40)

    response = client.models.generate_content(
        model="gemma-3-27b-it",
        contents=f"""
        You are a cybersecurity analyst.
        Analyze this log and give:
        1. Threat Type
        2. Severity (Low/Medium/High/Critical)
        3. MITRE ATT&CK
        4. Recommended Action

        Log: {log}
        Keep answer short and clear.
        """
    )

    print(response.text)
    print("=" * 50)
