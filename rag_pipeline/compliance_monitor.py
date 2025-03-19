class ComplianceMonitor:
    def __init__(self, keywords):
        self.keywords = keywords

    def detect_risks(self, text):
        risks = [keyword for keyword in self.keywords if keyword in text]
        return risks
