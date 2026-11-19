import subprocess
import time
import json
import urllib.request
import asyncio
import websockets
import base64
import os
import pymupdf

async def run():
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    port = 9222
    proc = subprocess.Popen([chrome_exe, "--headless=new", f"--remote-debugging-port={port}", "--disable-gpu", "--no-sandbox"])
    time.sleep(1.5)
    try:
        # Find page target
        req = urllib.request.Request(f"http://127.0.0.1:{port}/json/list")
        with urllib.request.urlopen(req) as resp:
            targets = json.loads(resp.read())
        
        page_target = [t for t in targets if t["type"] == "page"][0]
        page_ws = page_target["webSocketDebuggerUrl"]
        print("Connecting to page:", page_ws)
        
        async with websockets.connect(page_ws) as ws:
            test_html_path = os.path.abspath(r"d:\StudentDropout\paper_source\test_flow.html")
            file_url = f"file:///{test_html_path.replace(os.sep, '/')}"
            await ws.send(json.dumps({"id": 1, "method": "Page.navigate", "params": {"url": file_url}}))
            await ws.recv()
            await asyncio.sleep(1.2)
            
            header_tpl = """<div style="font-family: 'Times New Roman', serif; font-size: 8pt; width: 100%; margin: 0 18mm; display: flex; justify-content: space-between; border-bottom: 0.8px solid #000; padding-bottom: 2px;"><span><b>International Journal of Scientific Research in Engineering and Management (IJSREM)</b></span><span><b>ISSN: 2582-3930</b></span></div>"""
            footer_tpl = """<div style="font-family: 'Times New Roman', serif; font-size: 8pt; width: 100%; margin: 0 18mm; display: flex; justify-content: space-between; border-top: 0.8px solid #000; padding-top: 2px;"><span>&copy; 2026, IJSREM | https://ijsrem.com</span><span>DOI: &nbsp;|&nbsp; Page <span class="pageNumber"></span></span></div>"""
            
            print_cmd = {
                "id": 2,
                "method": "Page.printToPDF",
                "params": {
                    "landscape": False,
                    "displayHeaderFooter": True,
                    "headerTemplate": header_tpl,
                    "footerTemplate": footer_tpl,
                    "printBackground": True,
                    "paperWidth": 8.27,
                    "paperHeight": 11.69,
                    "marginTop": 0.85,
                    "marginBottom": 0.75,
                    "marginLeft": 0.71,
                    "marginRight": 0.71,
                    "preferCSSPageSize": False
                }
            }
            await ws.send(json.dumps(print_cmd))
            res = json.loads(await ws.recv())
            pdf_data = base64.b64decode(res["result"]["data"])
            
            out_file = r"d:\StudentDropout\paper_source\cdp_flow_test.pdf"
            with open(out_file, "wb") as f:
                f.write(pdf_data)
            print("PDF generated successfully:", out_file, len(pdf_data), "bytes")
            
            doc = pymupdf.open(out_file)
            print("CDP PDF page count:", len(doc))
            for i in range(len(doc)):
                page = doc[i]
                text = page.get_text()
                print(f"Page {i+1}: length={len(text)}, starts with: {repr(text.splitlines()[0] if text.splitlines() else '')}")
            doc.close()
    finally:
        proc.terminate()

if __name__ == "__main__":
    asyncio.run(run())
