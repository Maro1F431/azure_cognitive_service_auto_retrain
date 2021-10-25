# azure_cognitive_service_auto_retrain
The provided code was used for the following project:
The goal was to use the Azure cognitive services to create a model on the cloud that could detect malignant or benign melanoma. The model was served via an API.
The model was retrained automatically using pictures uploaded by users when they used it.
This is what the provided code does. It requires having the data already uploaded on the platform (train and test sets) with the correct tags ("benigb" and "maligant" in our case but you can change it). You also need to add the azure functions on your Azure platform.
Credentials were removed when the code went public so the you need to add your own.
