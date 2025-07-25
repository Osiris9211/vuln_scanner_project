# scan_cli.py

from core.scanner import AdvancedScanner

def main():
    url = input("Enter target URL (e.g. http://testphp.vulnweb.com): ").strip()
    scanner = AdvancedScanner(url)
    results, report_file = scanner.run()
    print("\nScan complete.")
    print(f"Vulnerabilities found: {len(results)}")
    print(f"Report saved to: {report_file}")

if __name__ == "__main__":
    main()
