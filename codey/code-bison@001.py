from vertexai.language_models import CodeGenerationModel


language = "python function"
file_format = "json"
extract_info = "names"
requirments = """
              - the name should be start with capital letters.
              - There should be no duplicate names in the final list.
              """

prefix = f"""Create a {language} to parse {file_format} and extract {extract_info} with the following requirements: {requirments}.
              """
code_generation_model = CodeGenerationModel.from_pretrained("code-bison@001")

response = code_generation_model.predict(prefix=prefix, max_output_tokens=1024)

print(response.text)