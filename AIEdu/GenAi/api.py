import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from gradio_client import Client
from transformers import VitsModel, AutoTokenizer
import torch
import numpy as np
import scipy.io.wavfile
import simpleaudio as sa
import os
import requests
import simpleaudio as sa
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
# You can access the audio with IPython.display for example
from IPython.display import Audio
@csrf_exempt
async def getAnswer(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        try:
            request_data = json.loads(request.body)
            question = request_data.get("question")
           
            # model= request_data.get("model") or g4f.models.default
            
            if question:
                # Launch the WebSocket server to stream data
                # asyncio.create_task(streamAnswer(8081, questions, model))
                client = Client("Qwen/Qwen1.5-110B-Chat-demo")
                result = client.predict(
		        query=question,
		        history=[],
		        system="You are a helpful assistant.",
		        api_name="/model_chat"
                )
            
                 
                # response = g4f.ChatCompletion.create(model=model,messages=questions)  
                response=result
                return JsonResponse({"response": response})
            else:
                return JsonResponse({"error": "No user input provided"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
async def textToSpeech(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        try:
            request_data = json.loads(request.body)
            text = request_data.get("text")
           
            # model= request_data.get("model") or g4f.models.default
            
            if text:
                model = VitsModel.from_pretrained("facebook/mms-tts-vie")
                tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-vie")
                inputs = tokenizer(text, return_tensors="pt")

                with torch.no_grad():
                    output = model(**inputs).waveform

                    # Chuyển đổi từ torch.Tensor sang numpy.ndarray
                    output_numpy = output.squeeze().cpu().numpy()

                    # Chuyển đổi dữ liệu float sang 16-bit PCM
                    output_int16 = np.int16(output_numpy / np.max(np.abs(output_numpy)) * 32767)

                    # Ghi dữ liệu vào file .wav
                    scipy.io.wavfile.write("techno.wav", rate=model.config.sampling_rate, data=output_int16)

                    # Phát âm thanh
                    wave_obj = sa.WaveObject.from_wave_file("techno.wav")
                    play_obj = wave_obj.play()
                    play_obj.wait_done()
                    os.remove("techno.wav")
            
                 
               
                return JsonResponse({"response": "ok"})
            else:
                return JsonResponse({"error": "No user input providedss"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)

