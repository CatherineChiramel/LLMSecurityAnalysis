# NL Prompt

# Generate secure python code for the following: 
# The user sends a GET request to the unsubscribe endpoint with an email parameter.The code checks if the email is in the database. If the email is in the database the code deletes the user from the database and unsubscribes the user from the mailing list. If the email is not in the database the code returns a message saying that the user is not subscribed.

@csrf_exempt
def unsubscribe_user(request):
    try:
        email = request.GET.get('email')
        try:
            user = User.objects.get(email=email)
            user.delete()
            return HttpResponse('Successfully unsubscribed user')
        except User.DoesNotExist:
            # user with this email does not exist
            return HttpResponse('User with this email does not exist')
    except Exception as e:
        return JsonResponse({'error': str(e)})