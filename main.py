import tkinter as tk
from tkinter import ttk
from reconnaissance import Reconnaissance
from scanning import Scanning
from vuln_assessment import VulnerabilityAssessment
from exploitation import Exploitation
from reporting import Reporting

class PenTestTool(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto PenTest Tool")
        self.geometry("800x600")

        # Notebook for tabs
        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill='both')

        # Initialize modules
        self.recon_module = Reconnaissance()
        self.scan_module = Scanning()
        self.vuln_module = VulnerabilityAssessment()
        self.exploit_module = Exploitation()
        self.report_module = Reporting()

        # Adding tabs
        self.recon_tab = ttk.Frame(notebook)
        self.scan_tab = ttk.Frame(notebook)
        self.vuln_tab = ttk.Frame(notebook)
        self.exploit_tab = ttk.Frame(notebook)
        self.report_tab = ttk.Frame(notebook)

        notebook.add(self.recon_tab, text="Reconnaissance")
        notebook.add(self.scan_tab, text="Scanning")
        notebook.add(self.vuln_tab, text="Vulnerability Assessment")
        notebook.add(self.exploit_tab, text="Exploitation")
        notebook.add(self.report_tab, text="Reporting")

        # Populate tabs
        self.setup_recon_tab()
        self.setup_scan_tab()
        self.setup_vuln_tab()
        self.setup_exploit_tab()
        self.setup_report_tab()

    def setup_recon_tab(self):
        tk.Label(self.recon_tab, text="Reconnaissance Tools").pack()
        target_entry = tk.Entry(self.recon_tab, width=50)
        target_entry.pack()
        tk.Button(
            self.recon_tab,
            text="Start Recon",
            command=lambda: self.recon_module.start_recon(target_entry.get())
        ).pack()

    def setup_scan_tab(self):
        tk.Label(self.scan_tab, text="Scanning Tools").pack()
        target_entry = tk.Entry(self.scan_tab, width=50)
        target_entry.pack()
        tk.Button(
            self.scan_tab,
            text="Start Scan",
            command=lambda: self.scan_module.start_scan(target_entry.get())
        ).pack()

    def setup_vuln_tab(self):
        tk.Label(self.vuln_tab, text="Vulnerability Assessment Tools").pack()
        target_entry = tk.Entry(self.vuln_tab, width=50)
        target_entry.pack()
        tk.Button(
            self.vuln_tab,
            text="Start Assessment",
            command=lambda: self.vuln_module.start_assessment(target_entry.get())
        ).pack()

    def setup_exploit_tab(self):
        tk.Label(self.exploit_tab, text="Exploitation Tools").pack()
        tk.Button(
            self.exploit_tab,
            text="Run Exploit",
            command=self.exploit_module.run_exploit
        ).pack()

    def setup_report_tab(self):
        tk.Label(self.report_tab, text="Generate Reports").pack()
        tk.Button(
            self.report_tab,
            text="Generate Report",
            command=self.report_module.generate_report
        ).pack()

if __name__ == "__main__":
    app = PenTestTool()
    app.mainloop()
