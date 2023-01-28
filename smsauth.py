# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure
def sendopt(phonenumber):
  account_sid = "ACe2ba56170748bc7babe48fb27243d56f"
  auth_token = "351a3b3f0bd03dc61f6ad528d15aad7a"
  verify_sid = "VA2e90c9ad693e9d95fecc64153fac2ddd"
  verified_number = "+918617257358"

  client = Client(account_sid, auth_token)

  verification = client.verify.v2.services(verify_sid) \
    .verifications \
    .create(to=verified_number, channel="sms")
  print(verification.status)

  otp_code = input("Please enter the OTP:")

  verification_check = client.verify.v2.services(verify_sid) \
    .verification_checks \
    .create(to=verified_number, code=otp_code)
  print(verification_check.status)