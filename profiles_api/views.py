from rest_framework.views import APIView # imports APIview class from rest_framework.views modules
from rest_framework.response import Response# imports the Response object which is used to return Responses
#from the APIview. o it's a standard response object that when you call the API view or when Django rest framework calls our API view it's expecting it to return this standard response object


class HelloApiView(APIView):
    """Test api view"""
    """API views are broken up is it expects a function for the different HTTP requests that can be made to the view so the HTTP GET request is typically used to retrieve a list of objects or a specific object so whenever you make a HTTP GET request to the URL that it will be assigned to this API view it will call the get function and it will execute the logic that we write in the get function"""
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        #request- request object -->this is passed in by the Django rest framework and contains details of the request being made to the API and
        #the format which is used to add a format suffix to the end of the endpoint URL
        #format but it's best practice to keep it in here so if u do ever enable formats on your API it will be supported by the functions that we create

        #Now we define a list which will describe all the features of an APIview
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch,put,delete)',
            'Is similar to tradational Django view',
            'Gives you the most control over you application logic',
            'Is mapped Manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
        #Now that we have our API view we can go ahead and wire this up to a URL in Django
