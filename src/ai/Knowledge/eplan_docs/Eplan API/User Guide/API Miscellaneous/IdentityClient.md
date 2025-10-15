# IdentityClient

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/IdentityClient.html

---

This chapter shows how to work with the  Eplan.IdentityClient.Authentification  and  Eplan.IdentityClient.Types  namespaces.

First create an  IEIdentityClient  object and make sure you are signed in to the Eplan Cloud:

- [C#](#i-tab-content-b132f597-c5f1-4d48-89a2-3811c57b2723)

```


// Create IdentityClient instance

IEIdentityClient IdentityClient = EIdentityClient.Instance;



// Make sure you are signed in to Eplan Cloud

Task<AuthenticationData> signInData = IdentityClient.Signin();

AuthenticationData signInResult = signInData.Result;



// Check if success

if (signInResult.IsSuccess)

    new Decider().Decide(EnumDecisionType.eOkDecision, "Sign in success", "Result", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

```

Get example information from the user cloud profile:

- [C#](#i-tab-content-955ec2cf-0305-4cf7-9851-1dac3cd7aff8)

```


// User profile information

Task<IdentityClientResponse> userProfile = IdentityClient.GetUserProfile();

IdentityClientResponse getUserProfileResult = userProfile.Result;



// Show exmaple information

if (getUserProfileResult.IsSuccess)

{

    string message = $"Organization Name: {getUserProfileResult.OrganizationName},\nEmail: {getUserProfileResult.Email}";

    new Decider().Decide(EnumDecisionType.eOkDecision, message, "UserProfile success", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

```

Set the  **ClientId**  name to work with a specific API service in the Eplan Cloud:

- [C#](#i-tab-content-e3f35e75-e246-4ebc-bc87-acb2b5332bfc)

```


// ClientId of specific Eplan Cloud API application

string ClientId = "Proper_Client_Id_Name";

```

Notice:  
**ClientId**  is case-sensitive and can be found on [Eplan Cloud Developer Portal](https://developer.eplan.com/) inside tooltip of product tag:



Use the  GetHttpClient()  method to work with Eplan Cloud API endpoints:

- [C#](#i-tab-content-353a2610-6eab-41ee-aafd-ca550a4c3a05)

```


// Initialize httpClient object

var url = "https://api.eplan.com/estockservice/v2.0/";

HttpClient httpClient = null;

IdentityClientResponse httpClientRespone = IdentityClient.GetHttpClient(strClientId, url, ref httpClient);



// Get collections

if (httpClientRespone.IsSuccess)

{

     HttpResponseMessage GetAsyncResult = httpClient.GetAsync("collections").Result;

     string message = $"Status: {GetAsyncResult.StatusCode.ToString()},\nResult: {GetAsyncResult.Content.ReadAsStringAsync().Result}";

     new Decider().Decide(EnumDecisionType.eOkDecision, message, "Get result", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

```

The  GetAccessToken()  is called internally by  GetHttpClient(), but it is still possible to use this method directly:

- [C#](#i-tab-content-c60bed65-fd4f-424b-bd7a-6df4c5a01189)

```


// Get access Token

IdentityClientResponse tokenResponse = IdentityClient.GetAccessToken(strClientId);

```

Sign out and exit:

- [C#](#i-tab-content-9fe1828e-c13c-49f8-8f30-b58161d91e70)

```


// Sign out

Task<IdentityClientResponse> response = IdentityClient.Signout();

IdentityClientResponse signOutResult = response.Result;



if (signOutResult.IsSuccess)

    new Decider().Decide(EnumDecisionType.eOkDecision, "Sign out success", "Result", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);





// Exit IdentityClient

IdentityClientResponse exitResponse = IdentityClient.Exit();



if (exitResponse.IsSuccess)

    new Decider().Decide(EnumDecisionType.eOkDecision, "Exit success", "Result", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

```

## Warning about deprecated endpoints

To receive a warning when a deprecated URL is addressed, the  EplanCloudResourceDeprecationEvent  must be subscribed to. In the following example, a message box will pop up as soon as a deprecated endpoint is addressed:



For this purpose, an event handler is registered for the EplanCloudResourceDeprecationEvent.

- [C#](#i-tab-content-5d17fe1d-e706-432d-9a03-f26d2d00bef7)

```


// Create an IdentityClient instance

IEIdentityClient IdentityClient = EIdentityClient.Instance;



// Create an endpoint deprecation event handling

EventHandler<EplanCloudResourceDeprecationArgs> DeprecationHandler = (sender, args) =>

{

    // Show a message box that displays the deprecated URL as well as the deprecation timestamp and sunset timestamp

    string message = $"The Eplan URL '{args.Uri}' is depreacted. Deprecation: {args.Deprecation}. Sunset: {args.Sunset}.";

    MessageBox.Show(message);

};



try

{

    // Register an event handler for the EplanCloudResourceDeprecationEvent

    IdentityClient.EplanCloudResourceDeprecationEvent += DeprecationHandler;



    // Call an Eplan Cloud deprecated endpoint

    string deprecatedURL = "yourDeprecatedEndpointURL";

    HttpClient httpClient = null;

    var result =

        IdentityClient.GetHttpClient(strClientId, deprecatedURL, ref httpClient);



    if (result.IsSuccess)

    {

        var response = httpClient.GetAsync(deprecatedURL).Result;



        // Handle response

        if (!response.IsSuccessStatusCode)

        {

            MessageBox.Show($"Eplan Cloud call failed. Error = {response.ReasonPhrase}");

        }



        // Give the deprecation message some time to pop up

        MessageBox.Show("Waiting for event...");

    }

    else

    {

        MessageBox.Show(result.Error);

    }

}

catch (Exception e)

{

    MessageBox.Show(e.Message);

}

finally

{

    // Unregister the event handler for EplanCloudResourceDeprecationEvent

    IdentityClient.EplanCloudResourceDeprecationEvent -= DeprecationHandler;

}

```