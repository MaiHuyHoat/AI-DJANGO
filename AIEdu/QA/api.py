import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os,torch
from transformers import AutoTokenizer,AutoModelForQuestionAnswering,pipeline
import requests

modelQADir=os.path.join(os.path.dirname(__file__),'Vietnamese-QA-model')
@csrf_exempt
async def getQA(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        try:
            request_data = json.loads(request.body)
            paragraph = request_data.get("paragraph")
            ques= request_data.get("question")
            # model= request_data.get("model") or g4f.models.default
            
            if paragraph:
                # Tải tokenizer và model
                tokenizer = AutoTokenizer.from_pretrained(modelQADir)
                model = AutoModelForQuestionAnswering.from_pretrained(modelQADir)
                qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

                # Định nghĩa ngữ cảnh và câu hỏi
                context =paragraph
                question = ques
                result = qa_pipeline(question=question, context=context)
                print(f"Câu trả lời: {result['answer']}")
                print(f"Điểm tin cậy: {result['score']}")
                return JsonResponse({"response":result['answer']})
            else:
                return JsonResponse({"error": "No user input provided"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
async def getSummarization(request):
    if request.method == 'POST' and request.content_type == 'application/json':
        try:
            request_data = json.loads(request.body)
            paragraph = request_data.get("paragraph")
            
            if paragraph:
                #API_URL = "https://api-inference.huggingface.co/models/VietAI/vit5-large-vietnews-summarization"
                API_URL = "https://api-inference.huggingface.co/models/CreatorPhan/ViSummary"
                headers = {"Authorization": "Bearer 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"}

                def query(payload):
                    response = requests.post(API_URL, headers=headers, json=payload)
                    return response.json()
                
                output = query({
                    "inputs": paragraph,
                })

                if 'error' in output:
                    output = query({
                    "inputs": paragraph,
                    })

                return JsonResponse({"response": output[0].get("summary_text")})
            else:
                return JsonResponse({"error": "No user input provided"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)
    
 

