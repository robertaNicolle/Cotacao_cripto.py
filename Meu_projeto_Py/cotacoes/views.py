# cotacoes/views.py

from django.shortcuts import render
from django.http import JsonResponse
import requests

def cotacao_view(request):
    if request.method == 'POST':
        cripto = request.POST.get('cripto')  # Obtém o nome da criptomoeda enviado pelo formulário
        
        if cripto:
            # Chama a API de cotação da criptomoeda
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=usd"
            response = requests.get(url)
            
            # Verifica se a resposta da API foi bem-sucedida
            if response.status_code == 200:
                data = response.json()
                
                # Verifica se a criptomoeda existe na resposta
                if cripto in data:
                    cotacao = data[cripto]['usd']
                    return JsonResponse({'erro': False, 'mensagem': f'A cotação de {cripto} é: ${cotacao}'})
                else:
                    return JsonResponse({'erro': True, 'mensagem': 'Criptomoeda não encontrada.'})
            else:
                return JsonResponse({'erro': True, 'mensagem': 'Erro ao acessar a API.'})
        else:
            return JsonResponse({'erro': True, 'mensagem': 'Nome da criptomoeda não fornecido.'})

    return render(request, 'index.html')
