from fpdf import FPDF

class Reporting:
    def __init__(self):
        self.pdf = FPDF()

    def add_title(self, title):
        self.pdf.set_font("Arial", size=16, style='B')
        self.pdf.cell(200, 10, txt=title, ln=True, align='C')
        self.pdf.ln(10)

    def add_subheading(self, subheading):
        self.pdf.set_font("Arial", size=14, style='B')
        self.pdf.cell(200, 10, txt=subheading, ln=True)
        self.pdf.ln(5)

    def add_paragraph(self, text):
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, txt=text)
        self.pdf.ln(5)

    def add_table(self, headers, data):
        self.pdf.set_font("Arial", size=12)

        # Print headers
        for header in headers:
            self.pdf.cell(40, 10, txt=header, border=1, align='C')
        self.pdf.ln()

        # Print data rows
        for row in data:
            for item in row:
                self.pdf.cell(40, 10, txt=str(item), border=1, align='C')
            self.pdf.ln()

    def generate_report(self, report_data):
        try:
            print("Generating report...")
            self.pdf.add_page()

            # Add title and content
            self.add_title("PenTest Report")
            self.add_subheading("Executive Summary")
            self.add_paragraph(report_data.get("executive_summary", "No summary provided."))

            self.add_subheading("Findings")
            findings = report_data.get("findings", [])
            if findings:
                for finding in findings:
                    self.add_paragraph(f"- {finding}")
            else:
                self.add_paragraph("No findings reported.")

            self.add_subheading("Detailed Table")
            headers = report_data.get("table_headers", [])
            data = report_data.get("table_data", [])
            if headers and data:
                self.add_table(headers, data)
            else:
                self.add_paragraph("No table data available.")

            # Save the report
            self.pdf.output("pentest_report.pdf")
            print("Report saved as pentest_report.pdf")
        except Exception as e:
            print(f"Error during report generation: {e}")

if __name__ == "__main__":
    sample_data = {
        "executive_summary": "This report summarizes the findings of the recent penetration test.",
        "findings": [
            "Open port 22 (SSH) with weak credentials.",
            "Unpatched software vulnerabilities found on server X.",
            "Insecure file permissions on critical files."
        ],
        "table_headers": ["Vulnerability", "Severity", "Status"],
        "table_data": [
            ["Weak SSH Credentials", "High", "Unresolved"],
            ["Unpatched Software", "Medium", "In Progress"],
            ["Insecure File Permissions", "Low", "Resolved"]
        ]
    }

    reporter = Reporting()
    reporter.generate_report(sample_data)
