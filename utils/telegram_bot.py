import requests
import json


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def send_message(self, data: object):
        url = self.api_url + "sendMessage"

        response = requests.post(url, data=data)
        return response.json()

    def send(self, action, data: object):
        url = self.api_url + action

        response = requests.post(url, data=data)
        return response.json()

    def edit_message(self, data: object):
        url = self.api_url + "editMessageText"

        response = requests.post(url, data=data)
        return response.json()

    def send_photo(self, data: object):
        url = self.api_url + "sendPhoto"

        response = requests.post(url, data=data)
        return response.json()

    def send_video(self, data: object):
        url = self.api_url + "sendVideo"

        response = requests.post(url, data=data)
        return response.json()

    def send_document(self, data: object):
        url = self.api_url + "sendDocument"

        response = requests.post(url, data=data)
        return response.json()

    def send_audio(self, data: object):
        url = self.api_url + "sendAudio"

        response = requests.post(url, data=data)
        return response.json()

    def send_sticker(self, data: object):
        url = self.api_url + "sendSticker"

        response = requests.post(url, data=data)
        return response.json()

    def send_animation(self, data: object):
        url = self.api_url + "sendAnimation"

        response = requests.post(url, data=data)
        return response.json()

    def send_voice(self, data: object):
        url = self.api_url + "sendVoice"
        response = requests.post(url, data=data)
        return response.json()

    def deleteMessage(self, data: object):
        url = self.api_url + "deleteMessage"
        response = requests.post(url, data=data)

        return response.json()

    def forward_message(self, data: object):
        url = self.api_url + "forwardMessage"
        response = requests.post(url, data=data)
        return response.json()
