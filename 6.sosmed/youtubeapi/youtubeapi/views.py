from django.views.generic import TemplateView
import requests

class HomeView(TemplateView):
    template_name = "index.html"
    api_key = 'AIzaSyC-IpGE2nkQsstBu4KAOEV2u5v2Qxcud8E'
    id_youtube = 'UCx7zc0MyoSdDSQXvq5Gl8gg'
    part = 'snippet,statistics'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Penggunaan try-except untuk menangani kesalahan saat mengambil data dari URL
        try:
            json_url = f"https://www.googleapis.com/youtube/v3/channels?part={self.part}&id={self.id_youtube}&key={self.api_key}"
            response = requests.get(json_url)
            response.raise_for_status()  # Mengecek apakah ada kesalahan saat melakukan permintaan
            data = response.json()
        except requests.exceptions.RequestException as e:
            data = {'error': 'Failed to fetch data'}

        context['data'] = data
        # print(context) 
        return context
