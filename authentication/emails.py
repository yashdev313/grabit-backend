# # from __future__ import print_function
# # import sib_api_v3_sdk
# # from sib_api_v3_sdk.rest import ApiException

# # configuration = sib_api_v3_sdk.Configuration()
# # configuration.api_key['api-key'] = 'xsmtpsib-00041b53168d25b0d89003eef4006816b81b1e58cf7f194a6c5877c0b9011d09-ESMnatkPqIdXNQvJ'

# # api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
# # subject = "from the Python SDK!"
# # sender = {"name":"Sendinblue","email":"help@restmails.com"}
# # replyTo = {"name":"Sendinblue","email":"help@restmails.com"}
# # html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
# # to = [{"email":"yashrajsinghji8@gmail.com","name":"Jane Doe"}]
# # params = {"parameter":"My param value","subject":"New Subject"}
# # send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=replyTo, html_content=html_content, sender=sender, subject=subject)
# # # send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)

# # try:
# #     api_response = api_instance.send_transac_email(send_smtp_email)
# #     print(api_response)
# # except ApiException as e:
# #     print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
# # 


# # 
# from __future__ import print_function
# import sib_api_v3_sdk
# from sib_api_v3_sdk.rest import ApiException

# configuration = sib_api_v3_sdk.Configuration()
# configuration.api_key['api-key'] = 'xsmtpsib-00041b53168d25b0d89003eef4006816b81b1e58cf7f194a6c5877c0b9011d09-ESMnatkPqIdXNQvJ'

# api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
# subject = "from the Python SDK!"
# sender = {"name":"Sendinblue","email":"contact@sendinblue.com"}
# replyTo = {"name":"Sendinblue","email":"contact@sendinblue.com"}
# html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
# to = [{"email":"example@example.com","name":"Jane Doe"}]
# params = {"parameter":"My param value","subject":"New Subject"}
# send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=replyTo, html_content=html_content, sender=sender, subject=subject)

# try:
#     api_response = api_instance.send_transac_email(send_smtp_email)
#     print(api_response)
# except ApiException as e:
#     print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


from django.core.mail import send_mail

def send_otp_mail(subject,otp,email):
    status = send_mail(
       subject,
        f'Your {subject} is {otp}. It is valid for only 5 mins',
        "verify@restmails.com",
        [email],
        html_message=f'<h1>Here is your {subject}</h1> <br/><p>Otp: {otp}</p><p>It is only valid for upto 5 mins</p>',
        fail_silently=True,
    )
    print('status', status)

#  status = send_mail(
#         "Password Reset Email",
#         "Here is the message.",
#         "verify@restmails.com",
#         ["yashrajsinghji8@gmail.com"],
#         fail_silently=False,
#     )