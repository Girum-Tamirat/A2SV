# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = defaultdict(int)
        for cpd in cpdomains:
            count, domain = cpd.split(" ")
            count = int(count)
            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_counts[subdomain] += count
        return [f"{count} {domain}" for domain, count in domain_counts.items()]