# IOC Extraction Script
import re

def extract_iocs(text):
    # Define regex patterns for different IOC types
    patterns = {
        'urls': r'(https?://[\w.-]+(?:/[^\s]*)?)',
        'ips': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
        'emails': r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}',
        'hashes': r'\b[a-f0-9]{32}\b|\b[a-f0-9]{40}\b|\b[a-f0-9]{64}\b',
        'cves': r'CVE-\d{4}-\d{1,7}'
    }
    iocs = {key: re.findall(pattern, text) for key, pattern in patterns.items()}
    return iocs

# Example usage
if __name__ == '__main__':
    sample_text = 'Check this URL: https://example.com and CVE-2021-12345.'
    print(extract_iocs(sample_text))