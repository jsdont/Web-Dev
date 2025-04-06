from django.http.response import JsonResponse
from .models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    data = [company_to_json(c) for c in companies]
    return JsonResponse(data, safe=False)

def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)
    return JsonResponse(company_to_json(company))

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancies.all()
        data = [vacancy_to_json(v) for v in vacancies]
        return JsonResponse(data, safe=False)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company not found'}, status=404)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = [vacancy_to_json(v) for v in vacancies]
    return JsonResponse(data, safe=False)

def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        return JsonResponse(vacancy_to_json(vacancy))
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy not found'}, status=404)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = [vacancy_to_json(v) for v in vacancies]
    return JsonResponse(data, safe=False)

def company_to_json(company):
    return {
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }

def vacancy_to_json(vacancy):
    return {
        'id': vacancy.id,
        'name': vacancy.name,
        'description': vacancy.description,
        'salary': vacancy.salary,
        'company': vacancy.company.id
    }
