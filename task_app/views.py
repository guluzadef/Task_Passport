from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serializer import PassportSerializer, PersonSerializer, PersonListSerializer
from .models import Passport, Person


class PassportListApi(APIView):  # GET
    permission_classes = (AllowAny,)

    def get(self, request):
        passport = Passport.objects.all()
        serializer = PassportSerializer(passport, many=True)
        return Response(serializer.data)


class PersonCreate(APIView):  # POST
    permission_classes = (AllowAny,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    # CREATE PERSON
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            print('+++++++++++++')
            data = serializer.data
            passport = data.pop('passport')  # Get Passport data
            person, _ = Person.objects.get_or_create(**data)  # Create Person
            print(person)
            for obj in passport:  # for one and more passport
                p = Passport(**obj)
                p.user = person
                p.save()  # DONE
            return Response(PersonSerializer(instance=person).data, status=status.HTTP_200_OK)
        else:
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class PersontListApi(APIView):  # GET all persons
    permission_classes = (AllowAny,)

    def get(self, request):
        person = Person.objects.all()
        serializer = PersonListSerializer(person, many=True)
        return Response(serializer.data)


class PersonApi(APIView):  # CRUD
    permission_classes = (AllowAny,)

    def get(self, request, pk):  # GET  Person for ID
        person = get_object_or_404(Person, pk=pk)
        data = PersonListSerializer(person).data
        return Response(data)

    def patch(self, request, pk):  # update data
        person = Person.objects.filter(id=pk).last()
        if not person:
            return Response({"result": False, "message": "Person not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonListSerializer(instance=person, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            try:
                pass_list = request.data['passport']

                # for one and more passport update
                for pasport in pass_list:
                    passportObj = Passport.objects.filter(user=person, id=pasport.pop('id'))
                    passportObj.update(**pasport)
                    return Response(PersonListSerializer(instance=person).data, status=status.HTTP_201_CREATED)
            except:
                return Response(PersonListSerializer(instance=person).data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # delete Person
        person = get_object_or_404(Person, pk=pk)
        person.delete()
        return Response({"message": f"{person.name} has been Deleted!"}, status=status.HTTP_200_OK)


# If want get Passport for id
class PassportApi(APIView):  # CRUD
    permission_classes = (AllowAny,)

    def get(self, request, pk):  # GET  Passport for ID
        person = get_object_or_404(Passport, pk=pk)
        data = PassportSerializer(person).data
        return Response(data)

    def patch(self, request, pk):  # update data
        passport = Passport.objects.filter(id=pk).last()
        if not passport:
            return Response({"result": False, "message": "Passport not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PassportSerializer(instance=passport, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(PassportSerializer(instance=passport).data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # delete Passport
        passport = get_object_or_404(Passport, pk=pk)
        passport.delete()
        return Response({"message": f"{passport.first_name} has been Deleted!"}, status=status.HTTP_200_OK)
