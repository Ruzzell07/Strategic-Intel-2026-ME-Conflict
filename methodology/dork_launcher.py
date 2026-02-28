import webbrowser
import time

# --- Operation Roaring Lion: OSINT Monitoring Queries ---
# These are the UK-English formatted queries we developed for your 2026 ledger.
DORKS = [
    # Global & Infrastructure (UK/Ireland/Australia)
    'site:gov.uk OR site:gov.ie "cyber incident" OR "advisory" "Iran" after:2026-02-27',
    'site:cyber.gov.au "threat update" OR "financial sector" after:2026-02-27',
    
    # SE Asia & Philippines Focus (OFW & Energy Security)
    'site:gov.ph "DMW" OR "DFA" "Iran" OR "Israel" "advisory" after:2026-02-27',
    'site:doe.gov.ph "Middle East" "energy security" OR "oil supply"',
    
    # Strategic Signposts (Hezbollah & IRGC)
    '"Radwan Unit" filetype:pdf "deployment" OR "Litani" after:2026-01-01',
    'site:ir "cyber defense" OR "infrastructure" filetype:pdf'
]

def launch_recon():
    print("🚀 Initialising Strategic Intelligence Reconnaissance...")
    print(f"Targeting {len(DORKS)} critical data streams for 2026 ME Conflict.\n")
    
    for i, dork in enumerate(DORKS, 1):
        # Constructing the Google Search URL
        search_url = f"https://www.google.com/search?q={dork}"
        
        print(f"[{i}] Launching: {dork[:50]}...")
        webbrowser.open_new_tab(search_url)
        
        # We add a small delay to prevent browser overload and look less like a bot
        time.sleep(2)

    print("\n✅ Reconnaissance tabs launched. Begin analysis in your browser.")

if __name__ == "__main__":
    launch_recon()
