import re

text = """Dear Customer,

Thank you for choosing our services. If you have any questions, feel free to reach out to our support team at 09351234567 or visit our website.

---

Meeting Notes – Project Phoenix  
Date: 2025-10-03  
Attendees: Sara, Reza, Amir  
Action Items:  
- Finalize budget proposal by next week.  
- Contact vendor at 09021234567 regarding hardware delivery.  
- Schedule follow-up with client (09381234567) before Friday.

---

Reminder: The deadline for submitting your application is October 10th.  
For assistance, call 09361234567 or email support@company.com.

---

Random Thoughts:  
Sometimes I wonder if 09391234567 is still active. It used to be my old number back in university.

---

Emergency Contact List:  
- Fire Department: 125  
- Police: 110  
- Irancell Helpdesk: 09371234567

---

End of File.
"""

irancell = [
    "900","901","902","903","904","905",
    "930","933","935","936","937","938","939","941"
]

p_pattern = r"(?:0(?:" + "|".join(irancell) + r"))\d{7}"
pattern = re.compile(r"\b" + p_pattern + r"\b")

matches = pattern.findall(text)

seen = set()
unique_matches = []
for m in matches:
    if m not in seen:
        seen.add(m)
        unique_matches.append(m)

print("Found Irancell numbers:")
for num in unique_matches:
    print(num)

print("\nInternational format (+98):")
for num in unique_matches:
    print("+98 " + num[1 : ])
