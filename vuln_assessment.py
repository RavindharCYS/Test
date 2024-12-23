import requests

class VulnerabilityAssessment:
    def start_assessment(self, target):
        try:
            print(f"Starting vulnerability assessment on {target}...")

            # Query a public CVE database API
            api_url = f"https://cve.circl.lu/api/search/{target}"
            print(f"Querying API: {api_url}")
            response = requests.get(api_url)

            if response.status_code == 200:
                vulnerabilities = response.json()

                if vulnerabilities:
                    print(f"\nFound {len(vulnerabilities)} vulnerabilities for {target}")
                    for vuln in vulnerabilities:
                        cve_id = vuln.get('id', 'N/A')
                        summary = vuln.get('summary', 'No summary available')
                        published_date = vuln.get('Published', 'N/A')

                        print(f"\nCVE ID: {cve_id}")
                        print(f"Summary: {summary}")
                        print(f"Published Date: {published_date}")
                else:
                    print(f"No vulnerabilities found for {target}.")
            else:
                print(f"API Error: HTTP Status Code {response.status_code}")

        except requests.RequestException as req_err:
            print(f"Network Error during API request: {req_err}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    target = input("Enter the software or library name to assess: ")
    assessor = VulnerabilityAssessment()
    assessor.start_assessment(target)
