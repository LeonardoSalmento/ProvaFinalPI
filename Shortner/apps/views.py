from django.shortcuts import render, redirect
from apps.models import *
from apps.forms import *
from django.views.generic.base import View
from rest_framework import viewsets, status
from apps.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages




# Create your views here.

def index(request):
    form = SiteForm()

    contexto = {
        'form':form
    }

    return render(request, 'index.html', contexto)


def desencurtar(request, texto):
    dados = 'http://localhost:8000/' + texto
    site = Site.objects.get(texto_encurtado = dados)
    return redirect(site.texto_original)


class EncurtarUrlView(View):
    def post(self, request):
        form = SiteForm(request.POST)

        if form.is_valid():
            dados_form = dados_form = form.cleaned_data
            site = Site()
            site.texto_original = dados_form['texto_original']
            #site.texto_encurtado = site.encurta()
            
            if len(site.texto_original)<=35:
                   messages.warning(request, 'URL muito curta')
                   return redirect('index')

            
            site.texto_encurtado = 'http://localhost:8000/' + dados_form['texto_original'][10] + dados_form['texto_original'][20] + dados_form['texto_original'][30] + dados_form['texto_original'][35] + dados_form['texto_original'][11]


            if(len(site.texto_original)<len(site.texto_encurtado)):
                   messages.warning(request, 'Não foi possível encurtar a url')
                   return redirect('index')
            site.save()

            contexto = {
                'site':site
            }

            return render(request, 'new_url.html', contexto)

        return redirect('index')


class EncurtarUrlViewApi(viewsets.ModelViewSet):
    serializer_class = SiteSerializer

    def get_queryset(self):
        return  Site.objects.all()

    def create(self, request, pk=None):
        serialized_data = SiteSerializer(data=request.data)
        if serialized_data.is_valid():
            try:
                site = Site()
                site.texto_original =  serialized_data.data['texto_original']
                site.texto_encurtado = 'http://localhost:8000/' + dados_form['texto_original'][10] + dados_form['texto_original'][20] + dados_form['texto_original'][30] + dados_form['texto_original'][35] + dados_form['texto_original'][11]
                if(len(site.texto_original)<len(site.texto_encurtado)):
                   return Response({'error':'Não foi possível encurtar a url'}, status=status.HTTP_400_BAD_REQUEST)
                
                site.save()
                
                return Response({ "texto_encurtado": site.texto_encurtado})
            except:
                return Response({'error':'não foi possível encurtar a url, ela já é menor que a encurtada'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def url_encurtada(request, url_encurtada):

    try:
        site = Site.objects.filter(texto_encurtado="http://localhost:8000/"+url_encurtada).first()
    except Site.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({"texto_original":site.texto_original})