import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.conf import settings
from .models import Lead


# ── Main page ──────────────────────────────────────────────────────────────────

def index(request):
    """Serve the intake form + results page."""
    return render(request, 'leads/index.html', {})


# ── REST API ───────────────────────────────────────────────────────────────────

@csrf_exempt
@require_http_methods(["POST"])
def create_lead(request):
    """Save a classified lead to the database."""
    try:
        data = json.loads(request.body)
        lead = Lead.objects.create(
            full_name     = data.get('full_name', ''),
            email         = data.get('email', ''),
            phone         = data.get('phone', ''),
            practice_name = data.get('practice_name', ''),
            years_qualified = int(data.get('years_qualified', 0)),
            num_dentists    = int(data.get('num_dentists', 1)),
            specialisms     = data.get('specialisms', ''),
            prev_claims     = data.get('prev_claims', 'None'),
            claim_details   = data.get('claim_details', ''),
            risk_level      = data.get('risk_level', ''),
            risk_summary    = data.get('risk_summary', ''),
            risk_factors    = data.get('risk_factors', []),
        )
        return JsonResponse({'id': lead.pk, 'status': 'saved'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_http_methods(["GET"])
def list_leads(request):
    """Return all leads as JSON."""
    leads = Lead.objects.all().values(
        'id', 'full_name', 'email', 'phone', 'practice_name',
        'years_qualified', 'num_dentists', 'specialisms',
        'prev_claims', 'claim_details',
        'risk_level', 'risk_summary', 'risk_factors',
        'created_at',
    )
    data = []
    for l in leads:
        l['created_at'] = l['created_at'].strftime('%Y-%m-%d %H:%M')
        data.append(l)
    return JsonResponse(data, safe=False)
