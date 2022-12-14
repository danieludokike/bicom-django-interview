from django.shortcuts import render

from django.http import HttpResponse

from .models import (
    PollingUnit, Agentname, Lga,
    AnnouncedPuResults, Ward,
    AnnouncedWardResults, AnnouncedLgaResults,
    
)


def index(request):
    polling_units = PollingUnit.objects.all()
    return render(request, "index.html", {"polling_units": polling_units})


def ward_result_view(request):
    if request.method == "POST":
        # Getting the local government from the request
        lga = request.POST.get("lga")
        
        # lga instance from the lga table
        lga_name = Lga.objects.get(lga_name=lga).lga_id
        
        # getting the corresponding LGA Result
        lga_results = AnnouncedLgaResults.objects.filter(lga_name=lga_name)
        
        sum_total = 0
        result_display = {}
        # Getting all the polling_units result
        for lga_result in lga_results:
            polling_unit_result = AnnouncedPuResults.objects.filter(result_id=lga_result.result_id)
            for result in polling_unit_result:
                sum_total += result.party_score
        print(sum_total)
        # Getting all the LOCAL GOVERNMENT
        lga = Lga.objects.values_list("lga_name", flat=True)
        
        return render(request, "ward_result.html", {"localgovernments": lga, "results": polling_unit_result})
       
     # Getting all the LOCAL GOVERNMENT
    lga = Lga.objects.values_list("lga_name", flat=True)
    
    return render(request, "ward_result.html", {"localgovernments": lga})


def all_poll_result(request):
    poll_result = AnnouncedPuResults.objects.all()
    return render(request, "total_result.html", {"result": poll_result})
    