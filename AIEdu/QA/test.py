from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# Tên mô hình trên Hugging Face
model_name = "ggnohope/Vietnamese-QA-model"

# Tải tokenizer và model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Tạo pipeline QA
qa_pipeline = pipeline('question-answering', model=model, tokenizer=tokenizer)

# Định nghĩa ngữ cảnh và câu hỏi
context = """
Django là một framework web cao cấp được viết bằng Python, giúp phát triển nhanh chóng và dễ dàng các ứng dụng web bảo mật.
Django bao gồm nhiều tính năng sẵn có, chẳng hạn như xác thực người dùng, quản lý nội dung, bản ghi hoạt động của người dùng, và nhiều hơn nữa.
"""
question = "Django được viết bằng ngôn ngữ lập trình nào?"

# Sử dụng pipeline để trả lời câu hỏi
result = qa_pipeline(question=question, context=context)

# In kết quả
print(f"Câu trả lời: {result['answer']}")
print(f"Điểm tin cậy: {result['score']}")