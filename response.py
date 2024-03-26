def abouts(request):  
    abouts = About.objects.all()  
    # return HttpResponse(abouts)
    abouts_data = About.objects.all().values()
    # Construct the JSON structure
    data = {'data': list(abouts_data)}
    # Return JSON response
    return JsonResponse(data)
