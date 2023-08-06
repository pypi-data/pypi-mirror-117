# LoginID Python SDK

## About 

LoginID’s server SDK enables websites and apps to utilize FIDO2 certified strong customer authentication, including the ability to provide more sensitive operations such as credential management. By leveraging the end user’s existing device biometrics or however the device is unlocked (e.g. PIN for Windows Hello), you can quickly integrate multi-factor authentication into your site. LoginID also offers [Transaction Confirmation](https://docs.loginid.io/Guides/Flows/tx-conf-guide/), where a transaction can be cryptographically signed providing proof of the user’s confirmation of that specific transaction, which is perfect for online merchants or FIs looking for secure payment authentication. Our service is aligned with PSD2, GDPR, CCPA, and HIPPA. The server SDK to connect with LoginID's infrastructure
## Installation


1. Install from GitHub:

```
git clone git@github.com:loginid1/python-sdk.git
cd python-sdk

pip install -e .
```
2. Install with `pip` 
```
pip install loginid
```

## Quick start
Once the package is installed, you can import the package and connect to LoginID's backend

```
from loginid import LoginID, LoginIdManagement

lApplication = LoginID(CLIENT_ID, PRIVATE_KEY)
lManagement = LoginIdManagement(MANAGEMNET_CLIENT_ID, MANAGEMENT_PRIVATE_KEY)

# verify a JWT token
token = "some_JWT_token" 
print(lApplication.verifyToken(token, USERNAME))

# extract user ID with management
print(lManagement.getUserId(USERNAME))
```

Refer to our documentations at
https://docs.loginid.io/Server-SDKs/Python/python-get-started for more details.

## Tell us how we’re doing
Have our solution in production? Tell us about your site on marketing@loginid.io and we’ll post on our social channels!