from rest_framework.views import APIView # imports APIview class from rest_framework.views modules
from rest_framework.response import Response# imports the Response object which is used to return Responses
#from the APIview. o it's a standard response object that when you call the API view or when Django rest framework calls our API view it's expecting it to return this standard response object
from rest_framework import status# list of handy http status code which can be used in response of apis
from profiles_api import serializers# module creaed in profiles_api

class HelloApiView(APIView):
    """Test api view"""
    """API views are broken up is it expects a function for the different HTTP requests that can be made to the view so the HTTP GET request is typically used to retrieve a list of objects or a specific object so whenever you make a HTTP GET request to the URL that it will be assigned to this API view it will call the get function and it will execute the logic that we write in the get function"""
    serializer_class=serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        #request- request object -->this is passed in by the Django rest framework and contains details of the request being made to the API and
        #the format which is used to add a format suffix to the end of the endpoint URL
        #format but it's best practice to keep it in here so if u do ever enable formats on your API it will be supported by the functions that we create

        #Now we define a list which will describe all the features of an APIview
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch,put,delete)',
            'Is similar to tradational Django view',
            'Gives you the most control over your application logic',
            'Is mapped Manually to URLs',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
        #Now that we have our API view we can go ahead and wire this up to a URL in Django
    def post(self, request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        #self.serializer_class is a function that comes with APIView that retrieves the configured serializer class for our view.
        #data=request.data assigns the data when you make a post request to our APIview the data is passed in as request data so its part of request object. We assing this data to serializer class  and we create new variable for our sericalzer  class called serializer.
        # Django rest framework serializers provide the functionality to validate the input so that is ensuring that the input is valid as per the specification of our serializer fields in our case we're going to be validating that the name is no longer than 10 characters
        # VAlidate like below:
        if serializer.is_valid():
            name=serializer.validated_data.get('name')#Similarly we can validated all the fields mentioned in serializers.py
            message=f'Hello {name}' #this message we're just going to return a message from our API that contains the name that was passed in the post request just to demonstrate
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
    def put(self, request, pk=None):
        """Handle updating an object"""
        #http put is often used to update an object. When you send put request , it will update the entire object
        #When you do http put request , you typically do it to a specific url primary key that is why we have pk in the argument which default to None.We usually , we do a put to the url with the ID of the object that you are updating.
        #And that is what this pk is for to take the id of the object to be updated with put request . We are not actually going to be updating an object , we are just going to return a standard response to demonstrate how you can add the put method to our apiview
        return Response({'method':'PUT'})
    def patch(self, requst, pk=None):
        """Handle a partial update of an object"""
        #Http patch is used to update only the fields that were provided in the request .o if you had a first name and a last name field and you made a patch request with just providing the last name it would only update the last name whereas if you did a put request and you only provided the last name then in that case it would remove the first name completely because HTTP put is essentially replacing an object with the object that was provided whereas patch is only updated the fields that were provided in the request
        return Response({'method':'PATCH'})
    def delete(self, request,pk=None):
        """Delete an object"""
        #Deletes objects in the databases
        return Response({'method':"DELETE"})
