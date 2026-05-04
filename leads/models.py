from django.db import models


RISK_CHOICES = [
    ('LOW',    'Low'),
    ('MEDIUM', 'Medium'),
    ('HIGH',   'High'),
]

CLAIMS_CHOICES = [
    ('None', 'None'),
    ('1',    '1 claim'),
    ('2',    '2 claims'),
    ('3+',   '3 or more claims'),
]


class Lead(models.Model):
    # Contact
    full_name     = models.CharField(max_length=200)
    email         = models.EmailField()
    phone         = models.CharField(max_length=30, blank=True)
    practice_name = models.CharField(max_length=200, blank=True)

    # Practice details
    years_qualified = models.PositiveIntegerField()
    num_dentists    = models.PositiveIntegerField()
    specialisms     = models.TextField(blank=True)

    # Claims history
    prev_claims  = models.CharField(max_length=10, choices=CLAIMS_CHOICES)
    claim_details = models.TextField(blank=True)

    # AI output
    risk_level   = models.CharField(max_length=10, choices=RISK_CHOICES, blank=True)
    risk_summary = models.TextField(blank=True)
    risk_factors = models.JSONField(default=list)

    # Meta
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"#{self.pk} {self.full_name} — {self.risk_level}"
