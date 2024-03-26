  
# this to return with no exception 
about = About.objects.filter(id=id).first()  # Retrieve the object or None if not found
about = About.objects.get(id=id)  #this returns exception when the object not found
about = About.objects.all  #to return all objects
about.delete() # to delete an object
about.save # to create or update




