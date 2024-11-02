/flight-api
├── .github/
│   └── workflows/
│       ├── flight-cicd.yml             # Flight service CI/CD
│       ├── hotel-cicd.yml              # Hotel service CI/CD
│       ├── bus-cicd.yml                # Bus service CI/CD
│       ├── car-cicd.yml                # Car service CI/CD
│       ├── event-cicd.yml              # Event service CI/CD
│       ├── holidays-cicd.yml           # Holidays service CI/CD
│       ├── insurance-cicd.yml          # Insurance service CI/CD
│       ├── train-cicd.yml              # Train service CI/CD
│       ├── api-gateway-cicd.yml        # API gateway CI/CD
│       └── integration-tests.yml       # Integration tests workflow
├── .gitignore                          # Ignore unnecessary files (e.g., .venv, __pycache__, etc.)
├── Dockerfile                          # Root Dockerfile for the entire project or the API gateway
├── docker-compose.yml                  # Docker Compose file for multi-service setup
├── requirements.txt                    # Root requirements file for shared dependencies
├── main.py                             # Root entry point if running an umbrella app (optional)
├── .venv/                              # Virtual environment folder (ideally add to .gitignore)
│
├── api-gateway/                        # API Gateway for routing traffic to microservices
│   ├── app/
│   │   ├── Dockerfile                  # Dockerfile specific to API Gateway
│   │   ├── main.py                     # Entry point for API Gateway
│   │   ├── README.md                   # Documentation for the API Gateway setup
│   │   └── requirements.txt            # Dependencies specific to API Gateway
│   └── k8s/
│       └── api-gateway.yaml            # Kubernetes manifest for API Gateway deployment
│
├── search/                             # Directory for all microservices related to search          
│   ├── flight/                         # Flight search microservice
│   │   ├── app/
│   │   │   ├── main.py                 # FastAPI application entry point
│   │   │   ├── config.py               # Configuration settings
│   │   │   ├── api/                    # API layer
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py           # API route definitions
│   │   │   │   └── schemas/            # Request/Response models
│   │   │   │       ├── __init__.py
│   │   │   │       ├── bdfare.py       # Bdfare models
│   │   │   │       ├── flyhub.py       # Flyhub models
│   │   │   │       └── common.py       # Shared models
│   │   │   ├── core/                   # Business logic
│   │   │   │   ├── __init__.py
│   │   │   │   ├── flight_search.py    # Core search logic
│   │   │   │   ├── providers/          # Provider integrations
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── bdfare.py       # Bdfare API client
│   │   │   │   │   └── flyhub.py       # Flyhub API client
│   │   │   │   └── utils/              # Utilities
│   │   │   │       ├── __init__.py
│   │   │   │       ├── auth.py         # Authentication
│   │   │   │       └── validators.py   # Input validation
│   │   │   ├── infrastructure/         # Infrastructure layer
│   │   │   │   ├── __init__.py
│   │   │   │   ├── cache/              # Caching
│   │   │   │   │   └── redis.py        # Redis implementation
│   │   │   │   └── logging/            # Logging
│   │   │   │       └── logger.py       # Logger config
│   │   │   └── tests/                  # Tests
│   │   │       ├── __init__.py
│   │   │       ├── conftest.py         # Test config
│   │   │       ├── test_bdfare.py      # Bdfare tests
│   │   │       ├── test_flyhub.py      # Flyhub tests
│   │   │       └── test_routes.py      # Route tests
│   │   ├── Dockerfile                  # Container config
│   │   ├── README.md                   # Service docs
│   │   └── requirements.txt            # Dependencies
│   │
│   ├── bus/
│   │   ├── app/
│   │   │   ├── main.py                 # Entry point for Bus microservice
│   │   │   ├── infrastructure/         # Infrastructure files (database, helpers)
│   │   │   └── tests/                  # Unit and integration tests
│   │   ├── Dockerfile                  # Dockerfile for Bus microservice
│   │   ├── README.md                   # Documentation for Bus microservice
│   │   └── requirements.txt            # Dependencies for Bus microservice
│   │
│   ├── car/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── infrastructure/
│   │   │   └── tests/
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── requirements.txt
│   │
│   ├── event/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── infrastructure/
│   │   │   └── tests/
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── requirements.txt
│   │
│   ├── holidays/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── infrastructure/
│   │   │   └── tests/
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── requirements.txt
│   │
│   ├── hotels/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── infrastructure/
│   │   │   └── tests/
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── requirements.txt
│   │
│   ├── insurance/
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── infrastructure/
│   │   │   └── tests/
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── requirements.txt
│   │
│   └── train/
│       ├── app/
│       │   ├── main.py
│       │   ├── infrastructure/
│       │   └── tests/
│       ├── Dockerfile
│       ├── README.md
│       └── requirements.txt
│
├── shared/                             # Common modules shared across microservices
│   ├── auth/
│   │   └── main.py                     # Authentication logic (e.g., JWT/OAuth)
│   ├── caching/
│   │   └── cache.py                    # Caching logic (e.g., Redis integration)
│   ├── logging/
│   │   └── logger.py                   # Centralized logging setup
│   ├── monitoring/
│   │   └── monitor.py                  # Monitoring logic (e.g., Prometheus metrics)
│   └── utils/
│       └── helpers.py                  # Utility functions
│
├── tests/                              # Integration and end-to-end tests across services
│   ├── conftest.py
│   ├── test_authentication.py
│   ├── test_bdfare.py
│   ├── test_combined.py
│   ├── test_flyhub.py
│
└── k8s/                                # Kubernetes manifests for deployment
    ├── namespace.yaml
    ├── configmaps/
    │   ├── api-gateway-config.yaml
    │   ├── bus-config.yaml
    │   ├── car-config.yaml
    │   ├── event-config.yaml
    │   ├── flight-config.yaml
    │   ├── holidays-config.yaml
    │   ├── hotel-config.yaml
    │   ├── insurance-config.yaml
    │   ├── train-config.yaml
    ├── deployments/
    │   ├── api-gateway-deployment.yaml
    │   ├── flight-deployment.yaml
    │   ├── hotel-deployment.yaml
    │   ├── bus-deployment.yaml
    │   ├── car-deployment.yaml
    │   ├── event-deployment.yaml
    │   ├── holidays-deployment.yaml
    │   ├── insurance-deployment.yaml
    │   └── train-deployment.yaml
    ├── secrets/
    │   ├── api-gateway-secrets.yaml
    │   └── microservices-secrets.yaml
    ├── services/
    │   ├── api-gateway-service.yaml
    │   └── microservices-services.yaml
    └── volumes/
        ├── redis-volume.yaml
        ├── mongo-volume.yaml
        └── postgres-volume.yaml


Develop Flight Service:
    Check Documentation Bdfare & Flyhub
    
    BDFARE Documentation
        Bdfare Enterprise API Documentation 
            Bdfare is a leading travel technology company in Bangladesh, specializing in advanced B2B travel portal, mobile app and APIs. Our fast, robust, and sophisticated API simplifies travel booking processes for agents, empowering them to access comprehensive travel services effortlessly. Partner with us to elevate your travel business with cutting-edge solutions. 
            This documentation provides detailed information on how to integrate with our API to enhance your travel booking experience. 
            ➤ API Environments 
            ● Sandbox Environment: To explore and test our API endpoints in the staging/test environment please check below details. In swagger you will get json samples for requests and responses and also you can test our api endpoints there. For short description per parameter or json fields you can check Schema provided for each endpoint in swagger. 
            Base URL 
            https://bdf.centralindia.cloudapp.azure.com/api/enterprise 
            Swagger Documentation 
            https://bdf.centralindia.cloudapp.azure.com/bdfare-enterprise-api/swagger /index.html 
            ● Live Environment: Once your integration using our sandbox is complete, we will provide you with some test cases to get certification for live environment. For the live environment check the details below. 
            Base URL 
            https://bdfare.com/api/enterprise 
            Swagger Documentation 
            https://bdfare.com/bdfare-enterprise-api/swagger/index.html
            ➤ API Endpoints 
            AirShopping 
            ● Description: Search and retrieve flight results. 
            ● Endpoint: base_url/AirShopping 
            MiniRule 
            ● Description: Obtain penalty details. 
            ● Endpoint: base_url/MiniRule 
            FareRules 
            ● Description: Retrieve fare rules post AirShopping or OfferPrice. ● Endpoint: base_url/FareRules 
            OfferPrice 
            ● Description: Confirm pricing before booking. 
            ● Endpoint: base_url/OfferPrice 
            OrderSell 
            ● Description: Finalize pricing confirmation before booking. ● Endpoint: base_url/OrderSell 
            OrderCreate 
            ● Description: Create booking and generate the respective PNR. ● Endpoint: base_url/OrderCreate 
            OrderRetrieve 
            ● Description: Retrieve booking details using booking ID. ● Endpoint: base_url/OrderRetrieve 
            OrderCancel 
            ● Description: Cancel bookings (Only applicable for OnHold bookings). ● Endpoint: base_url/OrderCancel 
            OrderReshopPrice 
            ● Description: Re-verify price before booking confirmation (Mandatory before OrderChange). 
            ● Endpoint: base_url/OrderReshopPrice 
            OrderChange 
            ● Description: Complete payment and confirm bookings. 
            ● Endpoint:base_url/OrderChange 
            GetBalance 
            ● Description: Retrieve account balance. 
            ● Endpoint: base_url/GetBalance
            ➤ API Integration Flow
            API Integration Flow Steps
            GetBalance

            Description: Retrieves the account balance.
            Endpoint: /GetBalance
            AirShopping

            Description: Searches and retrieves available flight results.

            Endpoint: /AirShopping

            Dependencies:

            FareRules: Retrieves fare rules after AirShopping or OfferPrice.
            Endpoint: /FareRules
            MiniRule: Obtains penalty details.
            Endpoint: /MiniRule
            OfferPrice

            Description: Confirms pricing before proceeding to booking.
            Endpoint: /OfferPrice
            OrderSell

            Description: Finalizes pricing confirmation before booking.
            Endpoint: /OrderSell
            OrderCreate

            Description: Creates the booking and generates the respective PNR.
            Endpoint: /OrderCreate
            OrderRetrieve

            Description: Retrieves booking details using the booking ID.
            Endpoint: /OrderRetrieve
            OrderCancel

            Description: Cancels bookings (only applicable for OnHold bookings).
            Endpoint: /OrderCancel
            OrderReshopPrice

            Description: Re-verifies the price before booking confirmation, mandatory before using OrderChange.
            Endpoint: /OrderReshopPrice
            OrderChange

            Description: Completes payment and confirms bookings.
            Endpoint: /OrderChange
            This flow represents the main interactions and dependencies between each API endpoint. The order shown reflects the usual process of searching, confirming pricing, creating, retrieving, and modifying or canceling bookings, as well as checking account balance.
            ➤ API Endpoints & Description 
                Air Shopping: Search and retrieve flight results. Results will expire after 15 minutes. 
                ● URL: base_url/AirShopping 
                ● Method: POST 
                Request Fields: 
                ● pointOfSale (string): Point of sale is the country/location code (alpha-2) (e.g., "BD", "AE"). 
                ● request (object): Contains the details of the flight request. ○ originDest (object array): List of objects where each has origin and destination details. These objects contain: 
                ■ originDepRequest (object): Details of the departure location and date. 
                ■ iatA_LocationCode (string): Origin or Departure airport 
                code (e.g., "DAC"). 
                ■ date (string): Departure date (e.g., "2024-03-25"). 
                ■ destArrivalRequest (object): Details of the arrival location and date. 
                ■ iatA_LocationCode (string): Arrival airport code (e.g., 
                "CXB"). 
                ■ date (string): Arrival date (optional for one-way 
                trips). 
                ○ pax (array): List of objects for passenger details. 
                ■ paxID (string): Unique passenger ID and the format is 'PAX' followed by a serial number (e.g., "PAX1"). For multiple 
                passengers, increment the number (e.g., "PAX2", "PAX3"). 
                ■ ptc (string): Passenger type code. Use "ADT" for adults, 
                "CHD" for children, and "INF" for infants. For children, add an age code (e.g., "C03" for a 3-year-old). If "CHD" is used without an age code, it defaults to 11 years. 
                ○ shoppingCriteria (object): This object defines the flight search criteria, including trip type, cabin class, and preferences. ■ tripType (string): Type of trip ("Oneway", "Return", 
                "Circle"). 
                ■ travelPreferences (object): 
                ■ vendorPref (string array, optional): Preferred airlines 
                (e.g., ["BG", "QR", "TK"] or null if no need). 
                ■ cabinCode (string): Cabin type ("Economy", 
                "PremiumEconomy", "Business", "First"). 
                ■ returnUPSellInfo (boolean): Indicates whether to include 
                branded fare (true or false). Branded fares offer additional conveniences and services that can make travel more 
                comfortable and flexible.
                Request Samples: 
                One-way Request: 
                { 
                "pointOfSale": "BD", 
                "request": { 
                "originDest": [ 
                { 
                "originDepRequest": { 
                "iatA_LocationCode": "DAC", 
                "date": "2024-01-15" 
                }, 
                "destArrivalRequest": { 
                "iatA_LocationCode": "CXB" 
                } 
                } 
                ], 
                "pax": [ 
                { 
                "paxID": "PAX1", 
                "ptc": "ADT" 
                } 
                ], 
                "shoppingCriteria": { 
                "tripType": "Oneway", 
                "travelPreferences": { 
                "vendorPref": [], 
                "cabinCode": "Economy" 
                }, 
                "returnUPSellInfo": true 
                } 
                } 
                }
                Return Request: 
                { 
                "pointOfSale": "BD", 
                "request": { 
                "originDest": [ 
                { 
                "originDepRequest": { 
                "iatA_LocationCode": "DAC", 
                "date": "2024-01-15" 
                }, 
                "destArrivalRequest": { 
                "iatA_LocationCode": "CXB" 
                } 
                }, 
                { 
                "originDepRequest": { 
                "iatA_LocationCode": "CXB", 
                "date": "2024-01-20" 
                }, 
                "destArrivalRequest": { 
                "iatA_LocationCode": "DAC" 
                } 
                } 
                ], 
                "pax": [ 
                { 
                "paxID": "PAX1", 
                "ptc": "ADT" 
                }, 
                { 
                "paxID": "PAX2", 
                "ptc": "C05" 
                } 
                ], 
                "shoppingCriteria": { 
                "tripType": "Oneway", 
                "travelPreferences": { 
                "vendorPref": [], 
                "cabinCode": "Economy" 
                }, 
                "returnUPSellInfo": true 
                } 
                } 
                }
                Multicity Request: 
                { 
                "pointOfSale": "BD", 
                "request": { 
                "originDest": [ 
                { 
                "originDepRequest": { 
                "iatA_LocationCode": "DAC", 
                "date": "2024-01-15" 
                }, 
                "destArrivalRequest": { 
                "iatA_LocationCode": "KUL" 
                } 
                }, 
                { 
                "originDepRequest": { 
                "iatA_LocationCode": "DAC", 
                "date": "2024-01-20" 
                }, 
                "destArrivalRequest": { 
                "iatA_LocationCode": "DXB" 
                } 
                }, 
                { 
                "originDepRequest": { 
                "iatA_LocationCode": "DAC", 
                "date": "2024-01-25" 
                }, 
                "destArrivalRequest": { 
                "iatA_LocationCode": "BKK" 
                } 
                } 
                ], 
                "pax": [ 
                { 
                "paxID": "PAX1", 
                "ptc": "ADT" 
                }, 
                { 
                "paxID": "PAX2", 
                "ptc": "C05" 
                } 
                ], 
                "shoppingCriteria": { 
                "tripType": "Circle", 
                "travelPreferences": { 
                "vendorPref": [], 
                "cabinCode": "Economy" 
                }, 
                "returnUPSellInfo": true 
                } 
                } 
                }
                Response Fields: 
                1. Root Object 
                ● message: string 
                A descriptive message about the response. 
                ● requestedOn: timestamp (e.g., 2024-07-29T08:24:17.110Z) 
                The timestamp when the request was made. 
                ● respondedOn: timestamp (e.g., 2024-07-29T08:24:17.110Z) 
                The timestamp when the response was sent. 
                ● response: Object 
                The main response object contains detailed data. 
                ● statusCode: string 
                The status code of the response. 
                ● success: boolean 
                Indicates if the request was successful (true or false). 
                ● error: Object (optional) 
                Contains error details if the request was not successful. 
                2. Response Object 
                ● traceId: string 
                A unique identifier for tracking the request/response. 
                ● offersGroup: Array of Offer Objects 
                List of offers/flights available in the response. 
                ● specialReturn: boolean 
                Indicates if there is a special return offer group (true or false). If you search for domestic return flights and if the specialReturn value is true then offers/flights will come inside the specialReturnOfferGroup object. ● specialReturnOfferGroup: Objects 
                Special return means domestic return flights (e.g., Dhaka to Cox’s Bazar). Contains special return offers if applicable. Here offers will come in two separate arrays of offers, OB (Outbound offers) and IB (Inbound offers). 
                SpecialReturnOfferGroup Object 
                ● OB: Array of Offer Objects 
                List of outbound offers or flights. Same object structure as Offer in offersGroup. 
                ● IB: Array of Offer Objects 
                List of inbound offers or flights. Same object structure as Offer in offersGroup. 
                Offer Object 
                ● offer: Object 
                Detailed offer information. 
                ● twoOnewayIndex: string (e.g., OB) 
                Indicates whether the offer is for outbound (OB) or inbound (IB). ● offerId: string 
                Unique identifier for the offer.
                ● validatingCarrier: string 
                Carrier/Airline code validating the offer. 
                ● refundable: boolean 
                Indicates if the offer is refundable. 
                ● fareType: string 
                Type of fare (OnHold/Web). If fareType is OnHold, then it's possible to book and hold a flight, if fareType is Web then only instant purchase is allowed for this booking. 
                ● paxSegmentList: Array of PaxSegment Objects 
                List of passenger segments for the offer. In other words this array contains flight segments. 
                ● fareDetailList: Array of FareDetail Objects 
                Details of fare for each passenger type. 
                ● price: Price Object 
                Pricing details for the offer. 
                ● penalty: Penalty Object 
                Penalty details associated with the offer. 
                ● baggageAllowanceList: Array of BaggageAllowance Objects Baggage allowances per segment for the offer. 
                ● upSellBrandList: Array of UpSellBrand Objects 
                List of upsell brands or branded fares available with the offer. If available then the first one is the default or lowest one. Branded fares offer additional conveniences and services that can make travel more comfortable and flexible. 
                ● seatsRemaining: number 
                Number of seats remaining for the offer. 
                PaxSegment Object 
                ● paxSegment: Object 
                Detailed passenger/flight segment information. 
                ● departure: Departure Object 
                Departure details for the segment. 
                ● arrival: Arrival Object 
                Arrival details for the segment. 
                ● marketingCarrierInfo: MarketingCarrierInfo Object 
                Marketing carrier/airline details. 
                ● operatingCarrierInfo: OperatingCarrierInfo Object 
                Operating carrier/airline details. 
                ● iatA_AircraftType: AircraftType Object 
                Aircraft type information. 
                ● rbd: string 
                RBD stands for Reservation Booking Designator, a code to indicate the booking class or fare class within each cabin class. While cabin classes (e.g., Economy) refer to the general type of service, RBDs provide a more granular level of detail. Each cabin class can have multiple booking classes (RBDs) like Y, B, M, H, etc., each representing different fare levels, restrictions, and benefits. 
                ● flightNumber: number 
                Flight number (e.g., 123). 
                ● segmentGroup: number 
                Segment grouping number. Whether you search for oneway or return or multi
                city, all the segments will be inside paxSegmentList even if there are stopovers. So to group them you can use this segmentGroup number. ● returnJourney: boolean 
                Indicates if it's a return journey. 
                ● airlinePNR: string 
                Passenger Name Record. 
                ● technicalStopOver: Array of TechnicalStopOver Objects Technical stopover details. 
                ● duration: number 
                Flight duration in minutes. 
                ● cabinType: string 
                Cabin type, e.g., Economy. 
                Departure Object 
                ● iatA_LocationCode: string 
                Origin or departure airport code. 
                ● terminalName: string 
                Terminal name for the departure. 
                ● aircraftScheduledDateTime: timestamp 
                Scheduled departure date and time. 
                Arrival Object 
                ● iatA_LocationCode: string 
                Destination or arrival airport code. 
                ● terminalName: string 
                Terminal name for the arrival. 
                ● aircraftScheduledDateTime: timestamp 
                Scheduled arrival date and time. 
                MarketingCarrierInfo Object 
                ● carrierDesigCode: string 
                Carrier designation code. 
                ● marketingCarrierFlightNumber: number 
                Marketing carrier's flight number. 
                ● carrierName: string 
                Name of the marketing carrier. 
                OperatingCarrierInfo Object 
                ● carrierDesigCode: string 
                Carrier designation code. 
                ● carrierName: string 
                Name of the operating carrier. 
                AircraftType Object 
                ● iatA_AircraftTypeCode: string 
                IATA aircraft type code.
                TechnicalStopOver Object 
                ● iatA_LocationCode: string 
                Airport or location code for the stopover. 
                ● aircraftScheduledArrivalDateTime: timestamp 
                Scheduled arrival date and time at the stopover. 
                ● aircraftScheduledDepartureDateTime: timestamp 
                Scheduled departure date and time from the stopover. 
                ● arrivalTerminalName: string 
                Terminal name at stopover arrival. 
                ● departureTerminalName: string 
                Terminal name at stopover departure. 
                FareDetail Object 
                ● baseFare: number 
                Base fare amount. 
                ● tax: number 
                Tax amount. 
                ● otherFee: number 
                Any other fees. 
                ● discount: number 
                Discount amount. 
                ● vat: number 
                Value Added Tax amount. 
                ● currency: string 
                Currency code. 
                ● paxType: string 
                Passenger type, e.g., ADT for adults, CHD for childs, INF for infants. ● paxCount: number 
                Number of passengers. 
                ● subTotal: number 
                Subtotal amount. 
                Price Object 
                ● totalPayable: TotalPayable Object 
                Total amount payable. 
                ● gross: Gross Object 
                Gross total amount. 
                ● discount: Discount Object 
                Discount details. 
                ● totalVAT: TotalVAT Object 
                VAT details. 
                TotalPayable Object 
                ● total: number 
                Total amount payable.
                ● currency: string 
                Currency code. 
                Gross Object 
                ● total: number 
                Gross total amount. 
                ● currency: string 
                Currency code. 
                Discount Object 
                ● total: number 
                Total discount amount. 
                ● currency: string 
                Currency code. 
                TotalVAT Object 
                ● total: number 
                Total VAT amount. 
                ● currency: string 
                Currency code. 
                Penalty Object 
                ● refundPenaltyList: Array of RefundPenalty Objects List of refund penalties per segment. 
                ● exchangePenaltyList: Array of ExchangePenalty Objects List of exchange penalties per segment. 
                RefundPenalty Object 
                ● departure: string 
                Departure location. 
                ● arrival: string 
                Arrival location. 
                ● penaltyInfoList: Array of PenaltyInfo Objects List of penalty information. 
                PenaltyInfo Object 
                ● type: string 
                Type of penalty, e.g., Before or After. 
                ● textInfoList: Array of TextInfo Objects 
                List of detailed penalty information per passenger type. TextInfo Object 
                ● paxType: string 
                Passenger type, e.g., Adult.
                ● info: Array of strings 
                Detailed penalty information. 
                ExchangePenalty Object 
                ● Same structure as RefundPenalty Object and its childs. 
                BaggageAllowance Object 
                ● departure: string 
                Departure location. 
                ● arrival: string 
                Arrival location. 
                ● checkIn: Array of CheckIn Objects 
                Check-in baggage allowances per passenger type. 
                ● cabin: Array of Cabin Objects 
                Cabin baggage allowances per passenger type. 
                CheckIn Object 
                ● paxType: string 
                Passenger type, e.g., Adult. 
                ● allowance: string 
                Check-in baggage allowance, e.g., 10Kg. You may get SB as a value and that means Standard Baggage. 
                Cabin Object 
                ● paxType: string 
                Passenger type, e.g., Adult. 
                ● allowance: string 
                Cabin baggage allowance, e.g., 10Kg. You may get SB as a value and that means Standard Baggage. 
                UpSellBrand Object 
                ● offerId: string 
                Offer identifier. 
                ● brandName: string 
                Brand name. 
                ● refundable: boolean 
                Indicates if the offer is refundable. 
                ● fareDetailList: Array of FareDetail Objects 
                List of fare details. Same as described above. 
                ● price: Price Object 
                Pricing details. Same as described above. 
                ● penalty: Penalty Object 
                Penalty details. Same as described above. 
                ● baggageAllowanceList: Array of BaggageAllowance Objects Baggage allowances. Same as described above.
                ● rbd: string 
                Booking class. Same as described above. ● meal: boolean 
                Indicates if a meal is included. 
                ● seat: string 
                Seat information, if applicable. 
                ● miles: string 
                Miles information, if applicable. 
                ● refundAllowed: boolean 
                Indicates if a refund is allowed. 
                ● exchangeAllowed: boolean 
                Indicates if exchange is allowed. 
                3. Error Object 
                ● errorCode: string 
                Error code. 
                ● errorMessage: string 
                Error message.

    Flyhub Documentation
        1. Process flow Diagram

            1. Process Flow Diagram
            Authenticate (Mandatory)
            Initiates the process.
            AirSearch (Mandatory)
            Searches for available flights.
            AirRules (Mandatory)
            Retrieves rules associated with flights.
            Promotions (Optional)
            Contains three optional steps:
            AirPromotion - Applies promotions to a booking.
            AirCheckPromotion - Checks if any promotions are available.
            AirRemovePromotion - Removes applied promotions.
            AirPrice (Mandatory)
            Retrieves the price for the selected flight.
            AirPreBook (Mandatory)
            Pre-booking process to hold the selected flight.
            AirBook (Mandatory)
            Books the selected flight.
            Booking Status (Mandatory)
            Checks the current status of the booking.
            IsMinRulesAvailable (Decision Point)
            If true:
            AirMinRules - Enforces minimum rules (Optional).
            If false, proceed without minimum rules enforcement.
            Cancel Booking (Optional)
            Contains:
            BookingPending - Indicates the booking is pending.
            AirCancel - Cancels the booking if needed.
            Booking Status (Decision Point)
            If "Booked" status:
            AirTicket - Issues the ticket.
            If "PendingInProcess" status:
            AirRetrieve - Retrieves the pending booking details.


# Flyhub Authentication API Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Common Headers](#common-headers)
3. [Root URLs](#root-urls)
4. [Endpoints](#endpoints)
    - [Authentication](#authentication)
5. [Error Handling](#error-handling)
6. [Sample Code Snippet](#sample-code-snippet)

---

### Introduction

The **Flyhub API** provides a secure way to authenticate users and obtain a bearer token required for accessing other API endpoints. This document provides information about the required headers, base URLs, and request/response formats for the Flyhub Authentication API.

---

### Common Headers

The following headers are common across all API requests:

| Header Key       | Header Value         |
|------------------|----------------------|
| Content-Type     | `application/json`   |
| Accept-Encoding  | `gzip, deflate`      |

---

### Root URLs

Use the appropriate base URL depending on the environment:

- **Production**: `https://api.flyhub.com/api/v1/`

---

### Endpoints

#### 1. Authentication

**Purpose**: Generates an authentication token, valid for 7 days, to be used in all subsequent API requests.

- **Endpoint**: `<RootURL>/Authenticate`
- **Method**: `POST`
- **Authentication**: None required for this endpoint.

##### Request Structure

| Field       | Type   | Description                        | Required |
|-------------|--------|------------------------------------|----------|
| username    | String | The username provided by Flyhub   | Yes      |
| apikey      | String | The API key provided by Flyhub    | Yes      |

**Sample Request Body:**

```json
{
  "username": "your_username",
  "apikey": "your_apikey"
}
```

##### Response Structure

| Field       | Type         | Description                                                | Mandatory |
|-------------|--------------|------------------------------------------------------------|-----------|
| FirstName   | String       | First name of the authenticated user                       | Yes       |
| LastName    | String       | Last name of the authenticated user                        | Yes       |
| Email       | String       | Email address of the authenticated user                    | Yes       |
| TokenId     | String       | The bearer token used for subsequent API requests          | Yes       |
| Status      | Enumeration  | Indicates the authentication status (0-Notset, 1-Success, 2-Failed) | Yes       |
| Error       | Object       | Contains error details (if any)                            | Yes       |

- **Error Structure**:

    | Field        | Type          | Description                                  | Mandatory |
    |--------------|---------------|----------------------------------------------|-----------|
    | Error code   | Enumeration   | Error code (refer to error codes in annexure) | No        |
    | Error Message | String        | Error message                                | No        |

**Sample Response Body:**

```json
{
  "FirstName": "John",
  "LastName": "Doe",
  "Email": "johndoe@example.com",
  "TokenId": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "Status": 1,
  "Error": null
}
```

##### Usage Notes

- The `TokenId` should be included as a `Bearer Token` in the `Authorization` header for all other API requests.
- The token is valid for 7 days and needs to be regenerated upon expiration.

---

### Error Handling

The Flyhub API will return an error object if the authentication fails. Here’s an example of a possible error response:

**Sample Error Response:**

```json
{
  "FirstName": "",
  "LastName": "",
  "Email": "",
  "TokenId": "",
  "Status": 2,
  "Error": {
    "ErrorCode": "401",
    "ErrorMessage": "Invalid username or API key"
  }
}
```

#### Error Codes

Refer to the annexure for a full list of error codes and their meanings.

---

### Sample Code Snippet

Here's a code snippet for calling the Flyhub Authentication API using Python and FastAPI.

```python
import requests

# Flyhub API base URL
ROOT_URL = "http://api.sandbox.flyhub.com/api/v1/Authenticate"

# Common headers
headers = {
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate"
}

# Authentication payload
payload = {
    "username": "your_username",
    "apikey": "your_apikey"
}

response = requests.post(ROOT_URL, json=payload, headers=headers)

if response.status_code == 200:
    print("Authentication successful:", response.json())
else:
    print("Error occurred:", response.json())
```

---

### Testing the Endpoint with Swagger UI

Run the FastAPI application and visit `http://127.0.0.1:8000/docs` to see the Swagger UI, where you can interact with the `/authenticate` endpoint, view required headers, and test the request directly.

---

This documentation will guide users through the setup, request format, response handling, and error management for the Flyhub Authentication API. Let me know if you need further details!

### 5. Flight APIs

This section covers the API specifications for searching available flights and retrieving booking details. 

#### 5.1 Air Search API

This API allows users to search for available flights based on origin, destination, travel date, and passenger details.

- **URL**: `<RootUrl>/AirSearch`
- **HTTP Method**: `POST`
- **Authorization**: Bearer token in request headers

#### Headers

| Header Key    | Header Value                                          |
|---------------|-------------------------------------------------------|
| Authorization | Bearer `<Token ID Received in authentication response>` |

#### Request Parameters

| Level | Parameter        | Type       | Description                                                    | Mandatory |
|-------|-------------------|------------|----------------------------------------------------------------|-----------|
| 1     | AdultQuantity     | Integer    | Number of adults                                               | Yes       |
| 2     | ChildQuantity     | Integer    | Number of children                                             | Yes       |
| 3     | InfantQuantity    | Integer    | Number of infants                                              | Yes       |
| 4     | EndUserIp         | String     | User's IP Address                                              | Yes       |
| 5     | JourneyType       | Enumeration | Journey Type: 1 - Oneway, 2 - Return, 3 - Multicity           | Yes       |
| 6     | Segments          | Array      | List of flight segments                                        | Yes       |
| 6.1   | Origin            | String     | IATA code of origin city (e.g., DEL, MAA)                      | Yes       |
| 6.2   | Destination       | String     | IATA code of destination city (e.g., HYD, BLR)                 | Yes       |
| 6.3   | Cabin Class       | Enumeration | Cabin class: 1 - Economy, 2 - Premium Economy, 3 - Business, 4 - First | Yes |
| 6.4   | DepartureDateTime | Date       | Departure date in `yyyy-mm-dd` format (e.g., 2019-04-30)       | Yes       |
| 7     | Preferred Airlines | String Array | Filter to specify preferred airlines                          | No        |
| 8     | Exclude Airlines  | String Array | Filter to exclude certain airlines                            | No        |

##### Sample Request

```json
{
  "AdultQuantity": 1,
  "ChildQuantity": 0,
  "InfantQuantity": 0,
  "EndUserIp": "192.168.1.1",
  "JourneyType": "1",
  "Segments": [
    {
      "Origin": "DEL",
      "Destination": "DXB",
      "CabinClass": "1",
      "DepartureDateTime": "2018-12-04"
    }
  ]
}
```

#### Response Parameters

| Level | Parameter            | Type               | Description                                           | Mandatory |
|-------|-----------------------|--------------------|-------------------------------------------------------|-----------|
| 1     | SearchId             | String             | Unique search identifier                              | Yes       |
| 2     | Results              | Array              | Array of available flights                            | Yes       |
| 2.1   | ResultID             | String             | Unique identifier for each flight result              | Yes       |
| 2.2   | IsRefundable         | Boolean            | Indicates if fare is refundable                       | Yes       |
| 2.3   | Fares                | Array of Fare      | Fare breakdown for each passenger type                | Yes       |
| 2.4   | Discount             | Decimal            | Total discount amount                                 | Yes       |
| 2.5   | ValidatingCarrier    | String             | Validating carrier code                               | Yes       |
| 2.6   | LastTicketDate       | DateTime (nullable) | Last date to issue ticket                             | Yes       |
| 2.7   | Segments             | Array of Segment   | Segment details including origin, destination, and airline information | Yes |
| 2.8   | TotalFare            | Decimal            | Total fare for the booking                            | Yes       |
| 2.9   | Currency             | String             | Currency code (e.g., BDT, INR)                        | Yes       |
| 2.10  | Availability         | Integer            | Number of available seats                             | Yes       |
| 2.11  | FareType             | Enumeration        | Fare type: 1 - NET, 2 - Instant Ticketing             | Yes       |
| 2.12  | HoldAllowed          | Boolean            | Indicates if the book-and-hold option is available    | No        |
| 2.13  | Error (if any)       | Error Element      | Contains error code and message if any                | No        |

##### Sample Response

```json
{
  "SearchId": "1b123aae-dd05-48e7-b12a-b14436595c50",
  "Results": [
    {
      "ResultID": "e80ee235-3a31-4435-a308-4bc8cdd50ec7",
      "IsRefundable": true,
      "Fares": [
        {
          "BaseFare": 14697.67,
          "Tax": 2068.20,
          "Currency": "BDT",
          "OtherCharges": 716.85,
          "Discount": 0.00,
          "PaxType": 1,
          "PassengerCount": 1,
          "ServiceFee": 0.00
        }
      ],
      "Discount": 0.00,
      "Validatingcarrier": "G8",
      "LastTicketDate": null,
      "Segments": [
        {
          "TripIndicator": 1,
          "Origin": {
            "AirportCode": "DEL",
            "AirportName": "Indira Gandhi Intl",
            "Terminal": "2",
            "CityCode": "DEL",
            "CityName": "New Delhi",
            "CountryCode": "IN",
            "CountryName": "India"
          },
          "DepTime": "2018-12-04T20:55:00",
          "Destination": {
            "AirportCode": "CCU",
            "AirportName": "Netaji Subhas Chandra",
            "Terminal": "",
            "CityCode": "CCU",
            "CityName": "Kolkata",
            "CountryCode": "IN",
            "CountryName": "India"
          },
          "Airline": {
            "AirlineCode": "G8",
            "AirlineName": "GoAir",
            "FlightNumber": "105",
            "BookingClass": "A",
            "CabinClass": "Y",
            "OperatingCarrier": "G8"
          },
          "Baggage": "15 Kg",
          "JourneyDuration": "125",
          "StopQuantity": "0"
        }
      ],
      "TotalFare": 12950.00,
      "Currency": "INR",
      "Availability": 0
    }
  ]
}
```

This detailed specification provides the structure, required parameters, and expected responses for the Air Search API, helping users understand the request and response structure for searching flight availability.

Here's the documentation layout for the AirPrice API, following a structured approach to cover each essential stage:

---

## API Documentation: AirPrice

### Overview
The **AirPrice API** provides pricing details for a specific search result from the AirSearch API, including options for additional services like extra baggage. This is a **POST** request and requires authorization.  

- **URL**: `<RootUrl>/AirPrice`
- **Method**: POST
- **Authorization**: Bearer Token

### Request Headers
| Header Key      | Header Value                               |
|-----------------|--------------------------------------------|
| Authorization   | Bearer `<Token>` received in Authentication |

### Request Parameters
| Field    | Type   | Description                                       | Mandatory |
|----------|--------|---------------------------------------------------|-----------|
| SearchID | String | Unique search ID from the AirSearch response.     | Yes       |
| ResultID | String | ID of the chosen itinerary from the AirSearch.    | Yes       |

#### Sample Request
```json
{
    "SearchID": "1b123aae-dd05-48e7-b12a-b14436595c50",
    "ResultID": "e80ee235-3a31-4435-a308-4bc8cdd50ec7"
}
```

### Response Elements
The AirPrice API response consists of several key components, including the search ID, available extra services, fare breakdown, flight segments, and error information if applicable.

#### Primary Fields
| Level | Field                | Type                 | Description                                  | Mandatory |
|-------|-----------------------|----------------------|----------------------------------------------|-----------|
| 1     | SearchId             | String               | The unique search ID used for tracking.      | Yes       |
| 2     | Results              | Array of Result      | Contains pricing and service details.        | Yes       |
| 2.1   | PassportMandatory    | Boolean              | Indicates if a passport is required.         | Yes       |
| 2.2   | ExtraServices        | Object               | Details about additional services like baggage. | Yes   |

#### Extra Services: Baggage Details
| Field     | Type    | Description                   | Mandatory |
|-----------|---------|-------------------------------|-----------|
| BaggageID | String  | Unique ID for baggage option. | Yes       |
| Weight    | String  | Weight allowance in kg.       | Yes       |
| Currency  | String  | Currency for the price.       | Yes       |
| Price     | Decimal | Cost of extra baggage.        | Yes       |
| Origin    | String  | Origin airport code.          | Yes       |
| Destination | String | Destination airport code.   | Yes       |
| PaxID     | String  | Passenger ID.                 | Yes       |

#### Fares Details
| Field          | Type       | Description                          | Mandatory |
|----------------|------------|--------------------------------------|-----------|
| BaseFare       | Decimal    | Base fare cost.                      | Yes       |
| Tax            | Decimal    | Tax amount.                          | Yes       |
| Currency       | String     | Currency of fare.                    | Yes       |
| OtherCharges   | Decimal    | Additional charges, if any.          | Yes       |
| Discount       | Decimal    | Discount applied to the booking.     | Yes       |
| PaxType        | Enum       | Passenger type (Adult, Child, Infant). | Yes   |
| PassengerCount | Integer    | Number of passengers.                | Yes       |
| ServiceFee     | Decimal    | Additional service fee if applicable. | Yes    |

#### Segment Information
Each flight segment contains the origin, destination, airline details, and journey information.

| Level      | Field           | Type       | Description                  | Mandatory |
|------------|------------------|------------|------------------------------|-----------|
| 2.9        | Segments         | Array      | Flight segment details       | Yes       |
| 2.9.1      | TripIndicator    | Enum       | Indicates outbound/inbound.  | Yes       |
| 2.9.2.1.1  | AirportCode      | String     | Origin airport IATA code.    | Yes       |
| 2.9.2.2    | DepTime          | Date Time  | Departure time.              | Yes       |
| 2.9.3.1.1  | AirportCode      | String     | Destination airport code.    | Yes       |
| 2.9.3.2    | ArrTime          | Date Time  | Arrival time.                | Yes       |
| 2.9.4      | Airline          | Object     | Airline details for segment. | Yes       |

### Error Handling
The API provides an error object if any issues occur during the request. Typical errors include fare unavailability, price changes, or itinerary adjustments.

| Field         | Type         | Description                                 | Mandatory |
|---------------|--------------|---------------------------------------------|-----------|
| ErrorCode     | Enum         | Code indicating the type of error.          | No        |
| ErrorMessage  | String       | Detailed message describing the error.      | No        |
| RePriceStatus | Enum         | Indicates reprice status for the itinerary. | No        |

### Sample Response
```json
{
    "SearchId": "1b123aae-dd05-48e7-b12a-b14436595c50",
    "Results": [
        {
            "PassportMandatory": false,
            "ExtraServices": {
                "Baggage": [
                    {
                        "BaggageID": "3a6fb4bd-c58a-4602-adc6-4f6baf3d9e25",
                        "Weight": "5 Kg",
                        "Currency": "BDT",
                        "Price": 2565.00,
                        "Origin": "DEL",
                        "Destination": "CCU"
                    }
                ]
            },
            "ResultID": "e80ee235-3a31-4435-a308-4bc8cdd50ec7",
            "IsRefundable": true,
            "Fares": [
                {
                    "BaseFare": 14697.67,
                    "Tax": 2068.20,
                    "Currency": "BDT",
                    "OtherCharges": 716.85,
                    "Discount": 0.0,
                    "PaxType": 1,
                    "PassengerCount": 1,
                    "ServiceFee": 0.00
                }
            ],
            "Segments": [
                {
                    "TripIndicator": 1,
                    "Origin": {
                        "Airport": {
                            "AirportCode": "DEL",
                            "AirportName": "Indira Gandhi Intl",
                            "CityName": "New Delhi",
                            "CountryCode": "IN"
                        },
                        "DepTime": "2018-12-04T20:55:00"
                    },
                    "Destination": {
                        "Airport": {
                            "AirportCode": "CCU",
                            "AirportName": "Netaji Subhas Chandra",
                            "CityName": "Kolkata",
                            "CountryCode": "IN"
                        },
                        "ArrTime": "2018-12-04T23:00:00"
                    },
                    "Airline": {
                        "AirlineCode": "G8",
                        "FlightNumber": "105",
                        "BookingClass": "A"
                    },
                    "Baggage": "15 Kg"
                }
            ],
            "TotalFare": 17483.00,
            "Currency": "BDT"
        }
    ],
    "Error": null,
    "RePriceStatus": 3
}
```

### Status Codes
- **200 OK**: Successfully retrieved the price details.
- **400 Bad Request**: Invalid request parameters.
- **401 Unauthorized**: Invalid or missing authentication token.
- **404 Not Found**: SearchID or ResultID not found.
- **500 Internal Server Error**: Error processing the request.

--- 

This stage-by-stage documentation covers essential details and guides developers and integrators on how to use the AirPrice API effectively. Let me know if there’s anything specific to add or clarify!

### Documentation for the `AirRules` API

---

#### 1. **Overview**
The `AirRules` API is an optional endpoint that provides the terms and conditions for a selected itinerary. Although it is not mandatory to call this API before booking, displaying these rules before booking is recommended to ensure that users are informed of any restrictions, rescheduling policies, or cancellation terms.

- **URL**: `<RootUrl>/AirRules`
- **Method**: `POST`
- **Authorization Header**:
  - **Header key**: Authorization
  - **Header value**: Bearer `<Token ID Received in Authentication Response>`

---

#### 2. **Request Parameters**

| **Level** | **Element** | **Type** | **Description**                               | **Mandatory** |
|-----------|-------------|----------|-----------------------------------------------|---------------|
| 1         | SearchID    | String   | Search ID received in the `AirSearch` response | Yes           |
| 2         | ResultID    | String   | Result ID of the selected itinerary from `AirSearch` | Yes           |

**Sample Request**:
```json
{
    "SearchID": "1b123aae-dd05-48e7-b12a-b14436595c50",
    "ResultID": "e80ee235-3a31-4435-a308-4bc8cdd50ec7"
}
```

---

#### 3. **Response Structure**

| **Level** | **Element**       | **Type**         | **Description**                                                         | **Mandatory** |
|-----------|--------------------|------------------|-------------------------------------------------------------------------|---------------|
| 1         | RuleType          | String           | Code representing the type of rule                                      | Yes           |
| 2         | RuleDetails       | String           | Description of the rule                                                 | Yes           |
| 3         | PaxType           | Enumeration      | Type of passenger (1: Adult, 2: Child, 3: Infant)                       | Yes           |
| 4         | AirlineCode       | String           | IATA code for the airline                                               | Yes           |
| 5         | CityPair          | String           | Origin and destination cities (e.g., "DAC-CGP")                         | Yes           |
| 6         | Error             | Error element    | Contains error details if an issue occurred                             | Yes           |
| 6.1       | ErrorCode         | Enumeration      | Code corresponding to the error (refer to annexure)                     | No            |
| 6.2       | ErrorMessage      | String           | Descriptive error message                                               | No            |

**Sample Response**:
```json
[
    {
        "RuleType": "AO9RBINF",
        "RuleDetails": "1. All Guests, including children and infants, must present valid identification at check-in... etc.",
        "PaxType": 3,
        "AirlineCode": "G8",
        "CityPair": "DEL-CCU",
        "Error": null
    }
]
```

---

#### 4. **Detailed Field Descriptions**
- **RuleType**: Code that identifies the type of rule, used for tracking and categorization of terms and conditions.
- **RuleDetails**: A detailed text description of the terms, including requirements for identification, rescheduling, cancellation, and check-in times.
- **PaxType**: Indicates the type of passenger; the response may contain different rules based on passenger categories such as adults, children, and infants.
- **AirlineCode**: The IATA airline code representing the carrier to which these rules apply.
- **CityPair**: A string combining the origin and destination city codes to indicate the route these rules pertain to.
- **Error**: If present, this element provides details about any issues with the request, including error code and descriptive message.

---

#### 5. **Use Cases**
- **Displaying Booking Conditions**: Retrieve terms and conditions for a specific itinerary before proceeding with the booking. Useful for ensuring customers are aware of policies on rescheduling, cancellations, and other rules.
- **Error Handling**: In cases where errors occur, the `Error` element in the response will provide details to assist in troubleshooting, such as invalid `SearchID` or `ResultID` values.

Here's a structured documentation stage for the **Air Pre-Book** API based on the information you've provided. This section includes an overview, details about the API request and response, and a sample request and response.

---

## 5.4 Air Pre-Book API Documentation

### Overview
The **Air Pre-Book** API is designed to initialize the booking process for air travel. It allows the user to provide passenger details and an itinerary result to proceed with the booking.

### API Endpoint
- **URL**: `<RootUrl>/AirPreBook`
- **Method**: `POST`

### Additional Headers
| Header Key     | Header Value                       |
|----------------|------------------------------------|
| Authorization   | Bearer `<Token id received in authentication>` |

### Request Structure
The request body should be a JSON object containing the following fields:

| Level | Element       | Type     | Description                                                 | Mandatory |
|-------|---------------|----------|-------------------------------------------------------------|-----------|
| 1     | SearchID     | String   | Search ID received in the AirSearch response                | Yes       |
| 2     | ResultID     | String   | Result ID of the interested itinerary                       | Yes       |
| 3     | Passengers    | List     | Contains details about passengers                            | Yes       |
| 3.1   | Title         | String   | Salutation (Mr, Ms, Mrs)                                   | Yes       |
| 3.2   | FirstName     | String   | Passenger's first name                                      | Yes       |
| 3.3   | MiddleName    | String   | Passenger's middle name                                     | No        |
| 3.4   | LastName      | String   | Passenger's last name                                       | Yes       |
| 3.5   | PaxType       | Enum     | Type of passenger (Adult, Child, Infant)                   | Yes       |
| 3.6   | DateOfBirth   | String   | Passenger's date of birth                                   | Yes       |
| 3.7   | Gender        | Enum     | Gender (Male, Female)                                      | Yes       |
| 3.8   | PassportNumber | String  | Passport number                                             | No        |
| 3.9   | PassportExpiryDate | String | Passport expiry date                                   | No        |
| 3.10  | PassportNationality | String | Passport nationality                                   | No        |
| 3.11  | Address1      | String   | Address of the passenger                                    | Yes       |
| 3.12  | Address2      | String   | Additional address field                                     | No        |
| 3.13  | CountryCode   | String   | Country code                                               | Yes       |
| 3.14  | Nationality   | String   | Passenger's nationality                                     | Yes       |
| 3.15  | ContactNumber | String   | Contact number                                             | Yes       |
| 3.16  | Email         | String   | Email address                                             | Yes       |
| 3.17  | IsLeadPassenger | Boolean | Whether the passenger is the lead passenger                | Yes       |
| 3.18  | FFAirline     | String   | Frequent flyer airline                                      | No        |
| 3.19  | FFNumber      | String   | Frequent flyer number                                       | No        |
| 3.20  | Baggage       | Element  | Carrying baggage information                                 | No        |
| 3.20.1| BaggageID     | String   | Baggage ID                                                | No        |
| 4     | PromotionCode  | String   | Promotion code applied for the booking                      | No        |

### Sample Request
```json
{
  "SearchID": "1b123aae-dd05-48e7-b12a-b14436595c50",
  "ResultID": "e80ee235-3a31-4435-a308-4bc8cdd50ec7",
  "Passengers": [
    {
      "Title": "Mr",
      "FirstName": "karim",
      "LastName": "ahmed",
      "PaxType": "Adult",
      "DateOfBirth": "1975-10-06",
      "Gender": "Male",
      "Address1": "test",
      "CountryCode": "BD",
      "Nationality": "BD",
      "ContactNumber": "577989789789",
      "Email": "test@m.com",
      "IsLeadPassenger": true
    }
  ]
}
```

### Response Structure
The response body will be a JSON object with the following fields:

| Level | Element        | Type    | Description                                                 | Mandatory |
|-------|----------------|---------|-------------------------------------------------------------|-----------|
| 1     | SearchID      | String  | Search ID                                                   | Yes       |
| 2     | Results       | List    | Contains the flight details                                 | Yes       |
| 2.1   | PassportMandatory | Boolean | Passport mandatory status                                 | Yes       |
| 2.2   | ExtraServices  | Element | Contains additional service details                         | Yes       |
| 2.3   | ResultID      | String  | Result ID                                                  | Yes       |
| 2.4   | IsRefundable   | Boolean | Is the fare refundable or not                               | Yes       |
| 2.5   | Fares         | List    | Contains fare details                                       | Yes       |
| 2.6   | Discount      | Decimal | Discount amount of the booking                              | Yes       |
| 2.7   | ValidatingCarrier | String | Validating carrier                                        | Yes       |
| 2.8   | LastTicketDate | DateTime[Nullable] | Last Ticket Date                                  | Yes       |
| 2.9   | Segments      | List    | Contains details about flight segments                      | Yes       |
| 2.10  | TotalFare     | Decimal | Total fare                                                 | Yes       |
| 2.11  | Currency      | String  | Currency                                                   | Yes       |
| 2.12  | Availability   | Integer | Number of available seats                                   | Yes       |
| 3     | RePriceStatus  | Enum    | Price status (FareUnavailable, PriceChange, NoPriceChange) | No        |
| 4     | AppliedPromotion | Element | Contains promotion details                                 | No        |
| 5     | Error         | Element | Contains error details                                      | No        |

### Sample Response
```json
{
  "SearchId": "1b123aae-dd05-48e7-b12a-b14436595c50",
  "Results": [
    {
      "PassportMandatory": false,
      "ExtraServices": {
        "Baggage": []
      },
      "ResultID": "e80ee235-3a31-4435-a308-4bc8cdd50ec7",
      "IsRefundable": true,
      "Fares": [
        {
          "BaseFare": 14697.67,
          "Tax": 2068.20,
          "Currency": "BDT",
          "OtherCharges": 716.85,
          "Discount": 0.0,
          "PaxType": 1,
          "PassengerCount": 1,
          "ServiceFee": 0.00
        }
      ],
      "Discount": 0.0,
      "ValidatingCarrier": "G8",
      "LastTicketDate": null,
      "segments": [
        {
          "TripIndicator": 1,
          "Origin": {
            "Airport": {
              "AirportCode": "DEL",
              "AirportName": "Indira Gandhi Intl",
              "Terminal": "2",
              "CityCode": "DEL",
              "CityName": "New Delhi",
              "CountryCode": "IN",
              "CountryName": "India"
            },
            "DepTime": "2018-12-04T20:55:00"
          },
          "Destination": {
            "Airport": {
              "AirportCode": "CCU",
              "AirportName": "Netaji Subhas Chandra",
              "Terminal": "",
              "CityCode": "CCU",
              "CityName": "Kolkata",
              "CountryCode": "IN",
              "CountryName": "India"
            },
            "ArrTime": "2018-12-04T23:00:00"
          },
          "Airline": {
            "AirlineCode": "G8",
            "AirlineName": "GoAir",
            "FlightNumber": "105",
            "BookingClass": "A",
            "CabinClass": "Y",
            "OperatingCarrier": "G8"
          },
          "Baggage": "15 Kg",
          "JourneyDuration": "125",
          "StopQuantity": "0"
        }
      ],
      "TotalFare": 17483.00,
      "Currency": "BDT",
      "Availability": 0
    }
  ],
  "Error": null,
  "RePriceStatus": 1
}
```

### Notes
- Ensure that all mandatory fields are filled correctly to avoid errors in processing the booking.
- Error messages and codes can be referred to in the annexure for further troubleshooting.

---

This documentation stage provides a clear and detailed overview of the **Air Pre-Book** API, its structure, and usage examples, making it easier for developers to integrate and utilize the API in their applications. Let me know if you need any modifications or additional sections!

Here's a summary of the **AirBook API** based on the information you've provided, structured for clarity and usability in your project:

### **AirBook API Overview**

#### **Purpose**
The AirBook API is used for booking flight itineraries, which can either hold an itinerary temporarily or immediately issue tickets based on the fare type.

#### **Fare Types**
1. **NET Fare Type**:
   - The API holds the itinerary for a certain period.
   - Itinerary status changes to **Booked**.
   - **No charges** for calling this API; you must use the AirTicketing API to generate the ticket.

2. **InstantTicket Fare Type**:
   - The API generates tickets immediately.
   - Itinerary status changes to **Ticketed**.
   - **User is charged** for the total cost unless the itinerary status is **Unconfirmed**.

---

### **API Details**

#### **Endpoint**
- **URL**: `<RootUrl>/AirBook`
- **Method**: `POST`

#### **Headers**
- **Authorization**: `Bearer <Token id received in authentication>`

---

### **Request Parameters**
```json
{
    "SearchID": "string",         // Mandatory: Search id from AirSearch response
    "ResultID": "string",         // Mandatory: Result id of the selected itinerary
    "Passengers": [                // Mandatory: List of passenger details
        {
            "Title": "string",     // Mandatory: Mr, Ms, Mrs
            "FirstName": "string", // Mandatory: Passenger's first name
            "MiddleName": "string",// Optional: Passenger's middle name
            "LastName": "string",  // Mandatory: Passenger's last name
            "PaxType": "string",    // Mandatory: Adult, Child, Infant
            "DateOfBirth": "string",// Mandatory: Passenger's date of birth
            "Gender": "string",     // Mandatory: Male, Female
            "PassportNumber": "string", // Optional: Passport number
            "PassportExpiryDate": "string", // Optional: Passport expiry date
            "PassportNationality": "string", // Optional: Passport nationality
            "Address1": "string",   // Mandatory: Passenger's address
            "Address2": "string",   // Optional: Additional address
            "CountryCode": "string",// Mandatory: Country code
            "Nationality": "string", // Mandatory: Passenger's nationality
            "ContactNumber": "string", // Mandatory: Contact number
            "Email": "string",      // Mandatory: Email address
            "IsLeadPassenger": true, // Mandatory: True if this passenger is the lead
            "FFAirline": "string",  // Optional: Frequent flyer airline
            "FFNumber": "string",   // Optional: Frequent flyer number
            "Baggage": {            // Optional: Baggage information
                "BaggageID": "string" // Optional: Baggage id
            }
        }
    ]
}
```

#### **Sample Request**
```json
{
    "SearchID": "c6e5ae65-bff5-4c34-b047-eeaf974658ca",
    "ResultID": "2fbc026f-74b5-443a-a47d-e623de4ce8b4",
    "Passengers": [
        {
            "Title": "Mr",
            "FirstName": "Karim",
            "LastName": "Ahmed",
            "PaxType": "Adult",
            "DateOfBirth": "1975-10-06",
            "Gender": "Male",
            "Address1": "test",
            "CountryCode": "BD",
            "Nationality": "BD",
            "ContactNumber": "577989789789",
            "Email": "test@m.com",
            "IsLeadPassenger": true,
            "PassportNumber": "HJFHFJKHFH6876",
            "PassportExpiryDate": "2020-10-12",
            "PassportNationality": "BD"
        }
    ]
}
```

---

### **Response Structure**
```json
{
    "BookingID": "string",                 // Mandatory: Flyhub's booking reference number
    "Results": [                           // Mandatory: List of flight results
        {
            "ResultID": "string",          // Mandatory: Result ID
            "IsRefundable": false,         // Mandatory: Refundability status
            "Fares": [                     // Mandatory: List of fare details
                {
                    "BaseFare": 11196.97,  // Mandatory: Base fare
                    "Tax": 11332.41,       // Mandatory: Tax
                    "Currency": "string",   // Mandatory: Currency code
                    "OtherCharges": 159.30, // Optional: Additional charges
                    "Discount": 0.00,      // Mandatory: Discount
                    "PaxType": "string",    // Mandatory: Passenger type
                    "PassengerCount": 1,   // Mandatory: Number of passengers
                    "ServiceFee": 0.00     // Mandatory: Service fee if applicable
                }
            ],
            "Discount": 0.00,               // Mandatory: Discount amount
            "Validatingcarrier": "string",   // Mandatory: Validating carrier
            "LastTicketDate": "datetime",    // Mandatory: Last ticket date
            "segments": [                    // Mandatory: List of segment details
                {
                    "TripIndicator": "string", // Mandatory: Trip indicator
                    "Origin": {
                        "Airport": {
                            "AirportCode": "string", // Mandatory: IATA code for origin airport
                            "AirportName": "string", // Mandatory: Name of the origin airport
                            "Terminal": "string",     // Mandatory: Terminal number
                            "CityCode": "string",     // Mandatory: IATA code for origin city
                            "CityName": "string",     // Mandatory: Name of the origin city
                            "CountryCode": "string",  // Mandatory: IATA code for origin country
                            "CountryName": "string"   // Mandatory: Name of the origin country
                        },
                        "DepTime": "datetime"      // Mandatory: Departure date time
                    },
                    "Destination": {
                        "Airport": {
                            "AirportCode": "string",  // Mandatory: IATA code for destination airport
                            "AirportName": "string",  // Mandatory: Name of the destination airport
                            "Terminal": "string",      // Mandatory: Terminal number
                            "CityCode": "string",      // Mandatory: IATA code for destination city
                            "CityName": "string",      // Mandatory: Name of the destination city
                            "CountryCode": "string",   // Mandatory: IATA code for destination country
                            "CountryName": "string"    // Mandatory: Name of the destination country
                        },
                        "ArrTime": "datetime"      // Mandatory: Arrival date time
                    },
                    "Airline": {
                        "AirlineCode": "string",   // Mandatory: IATA code for airline
                        "AirlineName": "string",   // Mandatory: Name of the airline
                        "FlightNumber": "string",  // Mandatory: Flight number
                        "BookingClass": "string",   // Mandatory: Booking class
                        "CabinClass": "string",     // Mandatory: Cabin class
                        "OperatingCarrier": "string" // Mandatory: Operating carrier
                    },
                    "Baggage": "string",         // Mandatory: Baggage information
                    "JourneyDuration": "string", // Mandatory: Total journey duration
                    "StopQuantity": "string"     // Mandatory: Number of stops
                }
            ],
            "TotalFare": 22689.00,          // Mandatory: Total fare
            "Currency": "string",            // Mandatory: Currency code
            "Availability": 0                 // Mandatory: Number of available seats
        }
    ],
    "Passengers": [                         // Mandatory: List of passengers
        {
            "Title": "string",              // Mandatory: Salutation
            "FirstName": "string",          // Mandatory: First name
            "LastName": "string",           // Mandatory: Last name
            "PaxType": "string",             // Mandatory: Passenger type
            "DateOfBirth": "datetime",       // Mandatory: Date of birth
            "Gender": "integer",             // Mandatory: Gender
            "PassportNumber": "string",      // Optional: Passport number
            "PassportExpiryDate": "datetime", // Optional: Passport expiry date
            "PassportNationality": "string", // Optional: Passport nationality
            "Address1": "string",            // Mandatory: Address
            "CountryCode": "string",         // Mandatory: Country code
            "Nationality": "string",         // Mandatory: Nationality
            "ContactNumber": "string",       // Mandatory: Contact number
            "Email": "string",               // Mandatory: Email
            "Ticket": [                      // Mandatory: List of ticket information
                {
                    "TicketNo": "string"      // Mandatory: Ticket number
                }
            ]
        }
    ]
}
```

#### **Sample Response**
```json
{
    "BookingID": "FHB201013790",
    "Results": [
        {
            "ResultID": "18f781ce-0c27-468a-8fe0-d0f2ad500c6a",
            "IsRefundable": false,
            "Fares": [
                {
                    "BaseFare": 11196.97,
                    "Tax": 11332.41,
                    "Currency": "BDT",
                    "

OtherCharges": 159.30,
                    "Discount": 0.00,
                    "PaxType": "Adult",
                    "PassengerCount": 1,
                    "ServiceFee": 0.00
                }
            ],
            "Discount": 0.00,
            "Validatingcarrier": "GF",
            "LastTicketDate": "2023-01-01T00:00:00Z",
            "segments": [
                {
                    "TripIndicator": "Outbound",
                    "Origin": {
                        "Airport": {
                            "AirportCode": "DAC",
                            "AirportName": "Hazrat Shahjalal International Airport",
                            "Terminal": "1",
                            "CityCode": "DAC",
                            "CityName": "Dhaka",
                            "CountryCode": "BD",
                            "CountryName": "Bangladesh"
                        },
                        "DepTime": "2023-01-01T00:00:00Z"
                    },
                    "Destination": {
                        "Airport": {
                            "AirportCode": "DXB",
                            "AirportName": "Dubai International Airport",
                            "Terminal": "1",
                            "CityCode": "DXB",
                            "CityName": "Dubai",
                            "CountryCode": "AE",
                            "CountryName": "United Arab Emirates"
                        },
                        "ArrTime": "2023-01-01T00:00:00Z"
                    },
                    "Airline": {
                        "AirlineCode": "GF",
                        "AirlineName": "Gulf Air",
                        "FlightNumber": "GF-100",
                        "BookingClass": "Y",
                        "CabinClass": "Economy",
                        "OperatingCarrier": "GF"
                    },
                    "Baggage": "2 pieces",
                    "JourneyDuration": "8h 30m",
                    "StopQuantity": "0"
                }
            ],
            "TotalFare": 22689.00,
            "Currency": "BDT",
            "Availability": 0
        }
    ],
    "Passengers": [
        {
            "Title": "Mr",
            "FirstName": "Karim",
            "LastName": "Ahmed",
            "PaxType": "Adult",
            "DateOfBirth": "1975-10-06T00:00:00Z",
            "Gender": 1,
            "PassportNumber": "HJFHFJKHFH6876",
            "PassportExpiryDate": "2020-10-12T00:00:00Z",
            "PassportNationality": "BD",
            "Address1": "test",
            "CountryCode": "BD",
            "Nationality": "BD",
            "ContactNumber": "577989789789",
            "Email": "test@m.com",
            "Ticket": [
                {
                    "TicketNo": "123456789"
                }
            ]
        }
    ]
}
```

---

This summary should provide a comprehensive understanding of the AirBook API's structure and usage. Let me know if you need any modifications or additional information!

Here's a structured overview of the **AirRetrieve** API, including the request and response details:

### AirRetrieve API Documentation

#### API Overview
The **AirRetrieve** API retrieves booking information using the booking reference received from the **AirBook** API. 

- **URL**: `<RootUrl>/AirRetrieve`
- **Method**: `POST`
- **Authorization Header**: 
  - **Key**: `Authorization`
  - **Value**: `Bearer <Token id Received in authentication>`

---

### Request Structure

**Request Body**:

| Level | Element    | Type   | Description                        | Mandatory |
|-------|------------|--------|------------------------------------|-----------|
| 1     | BookingID  | String | Booking ID returned in AirBook API | Yes       |

**Sample Request**:
```json
{
  "BookingID": "FHB201013790"
}
```

---

### Response Structure

**Response Body**:

| Level | Element               | Type    | Description                                                                                     | Mandatory |
|-------|-----------------------|---------|-------------------------------------------------------------------------------------------------|-----------|
| 1     | BookingID             | String  | Flyhub's booking reference number                                                              | Yes       |
| 2     | Results               | List    | Contains the flight details                                                                     | Yes       |
| 2.1   | Extra services        | Object  | Contains the additional service details                                                         | Yes       |
| 2.1.1 | Baggage              | Array   | Contains baggage details                                                                         | Yes       |
| 2.1.1.1 | BaggageId          | String  | Baggage ID                                                                                      | No        |
| 2.1.1.2 | Weight             | String  | Baggage weight in kilos                                                                          | No        |
| 2.1.1.3 | Currency           | String  | Currency code                                                                                   | No        |
| 2.1.1.4 | Price              | Decimal | Amount charged for the baggage                                                                   | No        |
| 2.1.1.5 | Origin             | String  | Origin city                                                                                     | No        |
| 2.1.1.6 | Destination        | String  | Destination city                                                                                | No        |
| 2.1.1.7 | PaxId             | String  | Passenger ID                                                                                    | No        |
| 2.2   | Result ID            | String  | Result ID                                                                                       | Yes       |
| 2.3   | Is Refundable        | Boolean | Indicates if the fare is refundable or not                                                     | Yes       |
| 2.4   | Fares                | List    | Contains fare details                                                                            | Yes       |
| 2.4.1 | BaseFare             | Decimal | Base fare of the booking                                                                         | Yes       |
| 2.4.2 | Tax                  | Decimal | Tax of the booking                                                                               | Yes       |
| 2.4.3 | Currency             | String  | Currency code                                                                                   | Yes       |
| 2.4.4 | OtherCharges         | Decimal | Some additional charges                                                                          | Yes       |
| 2.4.5 | Discount             | Decimal | Discount amount of the booking                                                                   | Yes       |
| 2.4.6 | AgentMarkUp          | Decimal | Agent Markup amount                                                                              | Yes       |
| 2.4.7 | PaxType              | Enumeration | Passenger Type (Adult, Child, Infant)                                                        | Yes       |
| 2.4.8 | Passenger Count      | Integer | Number of Passengers                                                                             | Yes       |
| 2.4.9 | ServiceFee           | Decimal | Service fee if applicable                                                                        | Yes       |
| 2.5   | Discount             | Decimal | Discount amount of the booking                                                                   | Yes       |
| 2.6   | Validatingcarrier     | String  | Validating carrier                                                                                | Yes       |
| 2.7   | LastTicketDate       | DateTime[Nullable] | Last Ticket Date                                                                            | Yes       |
| 2.8   | Segments             | List    | Contains details about flight segments                                                           | Yes       |
| 2.8.1 | TripIndicator        | Enumeration | Trip indicator (Outbound, Inbound)                                                          | Yes       |
| 2.8.2 | Origin               | Element | Contains departure details                                                                       | Yes       |
| 2.8.2.1 | Airport            | Element | Contains departure airport details                                                               | Yes       |
| 2.8.2.1.1 | AirportCode     | String  | IATA code for origin Airport                                                                     | Yes       |
| 2.8.2.1.2 | AirportName     | String  | Name of the origin airport                                                                        | Yes       |
| 2.8.2.1.3 | Terminal        | String  | Terminal Number                                                                                  | Yes       |
| 2.8.2.1.4 | CityCode       | String  | IATA code for origin city                                                                         | Yes       |
| 2.8.2.1.5 | CityName       | String  | Name of the origin city                                                                           | Yes       |
| 2.8.2.1.6 | CountryCode    | String  | IATA code for Origin country                                                                      | Yes       |
| 2.8.2.1.7 | CountryName    | String  | Name of the origin country                                                                        | Yes       |
| 2.8.2.2 | DepTime           | DateTime | Departure date time                                                                              | Yes       |
| 2.8.3 | Destination         | Element | Contains the details destination                                                                  | Yes       |
| 2.8.3.1 | Airport           | Element | Contains destination airport details                                                              | Yes       |
| 2.8.3.1.1 | AirportCode     | String  | IATA code for destination Airport                                                                  | Yes       |
| 2.8.3.1.2 | AirportName     | String  | Name of the destination airport                                                                    | Yes       |
| 2.8.3.1.3 | Terminal        | String  | Terminal Number                                                                                  | Yes       |
| 2.8.3.1.4 | CityCode       | String  | IATA code for destination city                                                                     | Yes       |
| 2.8.3.1.5 | CityName       | String  | Name of the destination city                                                                       | Yes       |
| 2.8.3.1.6 | CountryCode    | String  | IATA code for destination country                                                                  | Yes       |
| 2.8.3.1.7 | CountryName    | String  | Name of the destination country                                                                    | Yes       |
| 2.8.3.2 | ArrTime           | DateTime | Arrival date time                                                                                | Yes       |
| 2.8.4 | Airline            | Element | Element containing the carrier details                                                            | Yes       |
| 2.8.4.1 | AirlineCode       | String  | IATA code for airline                                                                              | Yes       |
| 2.8.4.2 | AirlineName       | String  | Name of the airline                                                                                | Yes       |
| 2.8.4.3 | FlightNumber      | String  | Flight number                                                                                     | Yes       |
| 2.8.4.4 | BookingClass       | String  | Reservation booking designator                                                                   | Yes       |
| 2.8.4.5 | CabinClass         | String  | Cabin class (Economy, Premium Economy, Business, First)                                         | Yes       |
| 2.8.4.6 | Operating Carrier   | String  | Operating carrier                                                                                 | Yes       |
| 2.8.5 | Journey Duration    | String  | Total Journey duration in minutes                                                                  | Yes       |
| 2.8.6 | Stop Quantity        | String  | Number of stops                                                                                   | Yes       |
| 2.8.7 | Equipment           | String  | Equipment description                                                                             | Yes       |
| 2.8.8 | Segment Group       | Integer | Segment group Id                                                                                 | No        |
| 2.9 | TotalFare            | Decimal | Total fare                                                                                      | Yes       |
| 2.10 | TotalFare With Agent Markup | Decimal | Total fare with agent markup                                                                | Yes       |
| 2.11 | Currency            | String  | Currency                                                                                        | Yes       |
| 2.12 | Availability         | Integer | Number of available seats                                                                         | Yes       |
| 2.13 | FareType            | Enumeration | Fare type (NET, InstantTicketing)                                                               | Yes       |
| 2.15 | isMiniRulesAvailable | Boolean | Indicates whether mini-rules are available or not for the itinerary                               | No        |
| 2.16 | HoldAllowed         | String  | Indicates whether or not book and hold is allowed                                                 | No        |
| 3   | Passengers           | List    | Contains the details of passengers                                                                | Yes       |
| 3.1 | Passenger Index       | String  | Passenger index                                                                                 | Yes       |
| 3.2 | Title                | String  | Salutation (Mr, Ms, Mrs)                                                                         | Yes       |
| 3.3 | FirstName           | String  | Passenger's first name                                                                            | Yes       |
| 3.4 | LastName            | String  | Passenger's last name                                                                             | Yes       |
| 3.5 | PaxType             | Enumeration | Type of passenger (Adult, Child, Infant)                                                        | Yes       |
| 3.6 | DateOfBirth         | String  | Passenger's date of birth                                                                        

 | Yes       |
| 3.7 | Nationality         | String  | Passenger's nationality                                                                          | Yes       |
| 3.8 | PassengerID         | String  | Passenger ID                                                                                    | Yes       |
| 3.9 | Contact             | Object  | Contact details of the passenger                                                                  | Yes       |
| 3.9.1 | Email              | String  | Email address                                                                                    | Yes       |
| 3.9.2 | Phone              | String  | Phone number                                                                                     | Yes       |

**Sample Response**:
```json
{
  "BookingID": "FHB201013790",
  "Results": [
    {
      "ExtraServices": {
        "Baggage": [
          {
            "BaggageId": "BG123",
            "Weight": "23",
            "Currency": "USD",
            "Price": 50.00,
            "Origin": "NYC",
            "Destination": "LAX",
            "PaxId": "PAX1"
          }
        ]
      },
      "ResultID": "R123456",
      "IsRefundable": true,
      "Fares": [
        {
          "BaseFare": 200.00,
          "Tax": 50.00,
          "Currency": "USD",
          "OtherCharges": 10.00,
          "Discount": 20.00,
          "AgentMarkUp": 5.00,
          "PaxType": "Adult",
          "PassengerCount": 1,
          "ServiceFee": 15.00
        }
      ],
      "Discount": 20.00,
      "ValidatingCarrier": "AA",
      "LastTicketDate": "2024-12-31T00:00:00Z",
      "Segments": [
        {
          "TripIndicator": "Outbound",
          "Origin": {
            "Airport": {
              "AirportCode": "JFK",
              "AirportName": "John F. Kennedy International Airport",
              "Terminal": "4",
              "CityCode": "NYC",
              "CityName": "New York",
              "CountryCode": "US",
              "CountryName": "United States"
            },
            "DepTime": "2024-11-01T14:00:00Z"
          },
          "Destination": {
            "Airport": {
              "AirportCode": "LAX",
              "AirportName": "Los Angeles International Airport",
              "Terminal": "1",
              "CityCode": "LAX",
              "CityName": "Los Angeles",
              "CountryCode": "US",
              "CountryName": "United States"
            },
            "ArrTime": "2024-11-01T17:00:00Z"
          },
          "Airline": {
            "AirlineCode": "AA",
            "AirlineName": "American Airlines",
            "FlightNumber": "AA123",
            "BookingClass": "Y",
            "CabinClass": "Economy",
            "OperatingCarrier": "AA"
          },
          "JourneyDuration": "180",
          "StopQuantity": "0",
          "Equipment": "Boeing 737",
          "SegmentGroup": 1
        }
      ],
      "TotalFare": 200.00,
      "TotalFareWithAgentMarkup": 205.00,
      "Currency": "USD",
      "Availability": 10,
      "FareType": "NET",
      "isMiniRulesAvailable": false,
      "HoldAllowed": "No"
    }
  ],
  "Passengers": [
    {
      "PassengerIndex": "1",
      "Title": "Mr",
      "FirstName": "John",
      "LastName": "Doe",
      "PaxType": "Adult",
      "DateOfBirth": "1990-01-01",
      "Nationality": "US",
      "PassengerID": "PAX1",
      "Contact": {
        "Email": "john.doe@example.com",
        "Phone": "+123456789"
      }
    }
  ]
}
```

---

### Notes
- Ensure to replace `<RootUrl>` with the actual base URL for the API.
- Ensure the correct authorization token is provided in the request header.
- The above structures are templates and should be adjusted as per your specific implementation and requirements. 

This documentation should help in integrating the AirRetrieve API into your application. Let me know if you need any more adjustments!

Certainly! Based on the provided information for the **AirTicketing API**, here’s a structured documentation stage you can follow:

---

# API Documentation for AirTicketing

## Overview
The **AirTicketing API** allows for the confirmation of booked itineraries for non-LCC (Low-Cost Carrier) airlines. Once the ticketing process is completed, the itinerary cannot be canceled using the AirCancel API.

### Endpoint
- **URL:** `<RootUrl>/AirTicketing`
- **Method:** `POST`

### Authentication
- **Header:**
  - **Key:** `Authorization`
  - **Value:** `Bearer <Token id received in authentication>`

## Request Format
### Request Body
The request must be sent in JSON format. The following parameters are required:

| Level | Element | Type   | Description                                                                 | Mandatory |
|-------|---------|--------|-----------------------------------------------------------------------------|-----------|
| All   | BookingID | String | Booking ID returned from the AirBook API.                                 | Yes       |
| All   | IsAcceptedPriceChangeandIssueTicket | Boolean | "True" if the user accepts the price change, "False" otherwise.        | Yes       |

### Sample Request
```json
{
  "BookingID": "FHB201013790",
  "IsAcceptedPriceChangeandIssueTicket": true
}
```

## Response Format
### Response Body
The API response will be in JSON format and includes the following elements:

| Level   | Element                          | Type      | Description                                                                  | Mandatory |
|---------|----------------------------------|-----------|------------------------------------------------------------------------------|-----------|
| 1       | BookingID                        | String    | Flyhub's booking reference number                                            | Yes       |
| 2       | Results                          | List      | Contains the flight details                                                  | Yes       |
| 2.1     | ExtraServices                    | Object    | Contains additional service details                                          | Yes       |
| 2.1.1   | Baggage                          | Array     | Contains baggage detail elements                                             | Yes       |
| 2.1.1.1 | BaggageId                       | String    | Baggage ID                                                                  | No        |
| 2.1.1.2 | Weight                           | String    | Baggage weight in kilos                                                     | No        |
| 2.1.1.3 | Currency                         | String    | Currency code                                                               | No        |
| 2.1.1.4 | Price                            | Decimal   | Amount charged for the baggage                                              | No        |
| 2.1.1.5 | Origin                           | String    | Origin city                                                                 | No        |
| 2.1.1.6 | Destination                      | String    | Destination city                                                            | No        |
| 2.1.1.7 | PaxId                            | String    | Passenger ID                                                                | No        |
| 2.2     | ResultID                        | String    | Result ID                                                                   | Yes       |
| 2.3     | IsRefundable                    | Boolean   | Indicates if the fare is refundable                                         | Yes       |
| 2.4     | Fares                           | List      | Contains fare details                                                       | Yes       |
| 2.4.1   | BaseFare                         | Decimal   | Base fare of the booking                                                    | Yes       |
| 2.4.2   | Tax                              | Decimal   | Tax of the booking                                                          | Yes       |
| 2.4.3   | Currency                         | String    | Currency code                                                               | Yes       |
| 2.4.4   | OtherCharges                     | Decimal   | Additional charges                                                          | Yes       |
| 2.4.5   | Discount                         | Decimal   | Discount amount of the booking                                              | Yes       |
| 2.4.6   | AgentMarkUp                     | Decimal   | Agent markup amount                                                         | Yes       |
| 2.4.7   | PaxType                         | Enumeration | Passenger Type (Adult, Child, Infant)                                     | Yes       |
| 2.4.8   | PassengerCount                   | Integer   | Number of passengers                                                        | Yes       |
| 2.4.9   | ServiceFee                       | Decimal   | Service fee if applicable                                                   | Yes       |
| 2.5     | Discount                         | Decimal   | Discount amount of the booking                                              | Yes       |
| 2.6     | ValidatingCarrier                | String    | Validating carrier                                                          | Yes       |
| 2.7     | LastTicketDate                   | DateTime[Nullable] | Last Ticket Date                                                         | Yes       |
| 2.8     | Segments                         | List      | Contains details about flight segments                                       | Yes       |
| 2.8.1   | TripIndicator                    | Enumeration | Trip indicator (Outbound, Inbound)                                       | Yes       |
| 2.8.2   | Origin                           | Element   | Contains departure details                                                  | Yes       |
| 2.8.3   | Destination                      | Element   | Contains destination details                                                | Yes       |
| 2.8.4   | Airline                          | Element   | Contains carrier details                                                    | Yes       |
| 2.8.5   | JourneyDuration                  | String    | Total journey duration in minutes                                           | Yes       |
| 2.8.6   | StopQuantity                     | String    | Number of stops                                                             | Yes       |
| 2.8.7   | Equipment                        | String    | Equipment description                                                        | Yes       |
| 2.9     | TotalFare                        | Decimal   | Total fare                                                                  | Yes       |
| 2.10    | TotalFareWithAgentMarkup         | Decimal   | Total fare including agent markup                                            | Yes       |
| 2.11    | Currency                         | String    | Currency                                                                    | Yes       |
| 2.12    | Availability                     | Integer   | Number of available seats                                                   | Yes       |
| 2.13    | FareType                         | Enumeration | Fare type (NET, InstantTicketing)                                         | Yes       |
| 2.15    | IsMiniRulesAvailable             | Boolean   | Indicates if mini rules are available for the itinerary                     | No        |
| 3       | Passengers                       | List      | Contains the details of passengers                                          | Yes       |
| 3.1     | PassengerIndex                   | String    | Passenger index                                                             | Yes       |
| 3.2     | Title                            | String    | Salutation (Mr, Ms, Mrs)                                                  | Yes       |
| 3.3     | FirstName                        | String    | Passenger's first name                                                     | Yes       |
| 3.4     | LastName                         | String    | Passenger's last name                                                      | Yes       |
| 3.5     | PaxType                         | Enumeration | Type of passenger (Adult, Child, Infant)                                  | Yes       |
| 3.6     | DateOfBirth                      | String    | Passenger's date of birth                                                  | Yes       |
| 3.7     | Gender                           | Enumeration | Gender (Male, Female)                                                     | Yes       |
| 3.8     | PassportNumber                   | String    | Passport number                                                             | No        |
| 3.9     | PassportExpiryDate               | String    | Passport expiry date                                                        | No        |
| 3.10    | PassportNationality               | String    | Passport nationality                                                        | No        |
| 3.11    | Address1                         | String    | Address of the passenger                                                   | Yes       |
| 3.12    | Address2                         | String    | Additional address field                                                    | No        |
| 3.13    | CountryCode                      | String    | Country code                                                               | Yes       |
| 3.14    | Nationality                      | String    | Passenger's nationality                                                    | Yes       |
| 3.15    | ContactNumber                    | String    | Contact number                                                             | Yes       |
| 3.16    | Email                            | String    | Email address                                                               | Yes       |
| 3.17    | IsLeadPassenger                  | Boolean   | Indicates if the passenger is the lead passenger                           | Yes       |
| 3.18    | FFAirline                        | String    | Frequent flyer airline                                                      | No        |
| 3.19    | FFNumber                         | String    | Frequent flyer number                                                       | No        |
| 3.20    | Ticket                           | Element   | Contains passenger ticket information                                       | Yes       |
| 3.20.1  | TicketNo                         | String    | Ticket number                                                               | Yes       |
| 4       | BookingStatus                    | Enumeration | Booking status. Refer to Annexure for booking status                      | Yes       |
| 5       | Error                            | Element   | Contains error details                                                      | Yes       |
| 5.1     | ErrorCode                        | Enumeration | Check annexure for details                                                 | No        |
| 5.2     | ErrorMessage                     | String    | Error message description                                                   | No        |
| 6       | IsPriceChanged                   | Boolean   | Indicates if the price has changed after booking was held                  | Yes       |
| 7       | Message                          | String    | Message from the supplier/airline                                          | No        |

### Sample Response
```json
{
  "BookingID": "FHB201013790",
  "Results": [
    {
      "ExtraServices": null,
      "ResultID": "2ceca7d0-bdc2-4318-af92-1a75974ef612",
      "IsRefundable": true,
      "Fares": [
        {
          "BaseFare": 1564.29,
          "Tax": 419.84,
          "Currency": "INR",
         

 "OtherCharges": 200,
          "Discount": 0,
          "AgentMarkUp": 0,
          "PaxType": "Adult",
          "PassengerCount": 1,
          "ServiceFee": 0
        }
      ],
      "Discount": 0,
      "ValidatingCarrier": "AI",
      "LastTicketDate": null,
      "Segments": [
        {
          "TripIndicator": "Outbound",
          "Origin": {
            "Airport": "DEL",
            "City": "Delhi",
            "Country": "India"
          },
          "Destination": {
            "Airport": "LON",
            "City": "London",
            "Country": "UK"
          },
          "Airline": {
            "Carrier": "AI",
            "FlightNo": "AI202",
            "Departure": "2023-10-12T22:00:00",
            "Arrival": "2023-10-13T04:00:00"
          },
          "JourneyDuration": "180",
          "StopQuantity": "0",
          "Equipment": "Boeing 777"
        }
      ],
      "TotalFare": 1984.13,
      "TotalFareWithAgentMarkup": 1984.13,
      "Currency": "INR",
      "Availability": 5,
      "FareType": "NET",
      "IsMiniRulesAvailable": false
    }
  ],
  "Passengers": [
    {
      "PassengerIndex": "0",
      "Title": "Mr",
      "FirstName": "John",
      "LastName": "Doe",
      "PaxType": "Adult",
      "DateOfBirth": "1985-05-15",
      "Gender": "Male",
      "Address1": "123 Street",
      "CountryCode": "IN",
      "Nationality": "Indian",
      "ContactNumber": "1234567890",
      "Email": "john.doe@example.com",
      "IsLeadPassenger": true,
      "Ticket": {
        "TicketNo": "1234567890"
      }
    }
  ],
  "BookingStatus": "Confirmed",
  "Error": null,
  "IsPriceChanged": false,
  "Message": "Ticket issued successfully."
}
```

## Error Codes
The API can return the following error codes along with their messages:

| Error Code          | Message                                      |
|---------------------|----------------------------------------------|
| INVALID_BOOKING_ID  | The provided booking ID is invalid.         |
| TICKET_ALREADY_ISSUED| The ticket has already been issued.         |
| PRICE_CHANGE_ACCEPTED| Price change accepted, ticket issued.       |
| TICKET_ISSUE_FAILED | Ticket issuance failed, please try again.   |

### Conclusion
This documentation provides the necessary details for integrating with the AirTicketing API. Ensure that all required fields are provided and handle responses appropriately, including error handling for potential issues.

---

Feel free to adjust the details as necessary or let me know if you need any additional sections!

Here's a structured stage of documentation for the **AirCancel** API based on the provided details:

---

## 5.8 AirCancel API Documentation

### Overview
The **AirCancel** API allows for the cancellation of itineraries that are in a booked status. Note that this API cannot be used for Low-Cost Carriers (LCC). For non-LCC carriers, the AirCancel API is not allowed if the itinerary has already been ticketed.

### Endpoint
- **URL**: `<RootUrl>/AirCancel`
- **Method**: `POST`

### Headers
- **Authorization**: `Bearer <Token id Received in authentication>`

### Request Structure

#### Request Body
| Level | Element    | Type   | Description                                         | Mandatory |
|-------|------------|--------|-----------------------------------------------------|-----------|
| 1     | BookingID  | String | Booking ID returned in the AirBook API             | Yes       |

#### Sample Request
```json
{
  "BookingID": "FHB201013791"
}
```

### Response Structure

#### Response Body
| Level | Element                          | Type   | Description                                               | Mandatory |
|-------|----------------------------------|--------|-----------------------------------------------------------|-----------|
| 1     | BookingID                        | String | Flyhub's booking reference number                         | Yes       |
| 2     | Results                          | List   | Contains the flight details                               | Yes       |
| 2.1   | ExtraServices                    | Element| Contains additional service details                       | Yes       |
| 2.1.1 | Baggage                         | Array  | Contains baggage details                                   | Yes       |
| 2.1.1.1 | BaggageId                      | String | Baggage ID                                              | No        |
| 2.1.1.2 | Weight                         | String | Baggage weight in kilos                                   | No        |
| 2.1.1.3 | Currency                       | String | Currency code                                           | No        |
| 2.1.1.4 | Price                          | Decimal| Amount charged for the baggage                            | No        |
| 2.1.1.5 | Origin                         | String | Origin city                                             | No        |
| 2.1.1.6 | Destination                    | String | Destination city                                        | No        |
| 2.1.1.7 | PaxId                          | String | Passenger ID                                           | No        |
| 2.2   | ResultID                        | String | Result ID                                               | Yes       |
| 2.3   | IsRefundable                    | Boolean| Indicates if the fare is refundable                      | Yes       |
| 2.4   | Fares                           | List   | Contains fare details                                     | Yes       |
| 2.4.1 | BaseFare                        | Decimal| Base fare of the booking                                  | Yes       |
| 2.4.2 | Tax                             | Decimal| Tax of the booking                                       | Yes       |
| 2.4.3 | Currency                        | String | Currency code                                           | Yes       |
| 2.4.4 | OtherCharges                    | Decimal| Additional charges                                       | Yes       |
| 2.4.5 | Discount                        | Decimal| Discount amount of the booking                           | Yes       |
| 2.4.6 | AgentMarkUp                     | Decimal| Agent markup amount                                      | Yes       |
| 2.4.7 | PaxType                         | Enumeration | Passenger Type (Adult, Child, Infant)                 | Yes       |
| 2.4.8 | PassengerCount                  | Integer | Number of passengers                                     | Yes       |
| 2.4.9 | ServiceFee                      | Decimal| Service fee if applicable                                 | Yes       |
| 2.5   | Discount                        | Decimal| Discount amount of the booking                           | Yes       |
| 2.6   | ValidatingCarrier               | String | Validating carrier                                       | Yes       |
| 2.7   | LastTicketDate                  | DateTime[Nullable] | Last Ticket Date                                   | Yes       |
| 2.8   | Segments                        | List   | Contains details about flight segments                   | Yes       |
| 2.8.1 | TripIndicator                   | Enumeration | Trip indicator (Outbound, Inbound)                    | Yes       |
| 2.8.2 | Origin                          | Element| Contains departure details                               | Yes       |
| 2.8.2.1 | Airport                        | Element| Contains departure airport details                       | Yes       |
| 2.8.2.1.1 | AirportCode                  | String | IATA code for origin Airport                             | Yes       |
| 2.8.2.1.2 | AirportName                  | String | Name of the origin airport                               | Yes       |
| 2.8.2.1.3 | Terminal                     | String | Terminal Number                                          | Yes       |
| 2.8.2.1.4 | CityCode                     | String | IATA code for origin city                                | Yes       |
| 2.8.2.1.5 | CityName                     | String | Name of the origin city                                  | Yes       |
| 2.8.2.1.6 | CountryCode                  | String | IATA code for origin country                             | Yes       |
| 2.8.2.1.7 | CountryName                  | String | Name of the origin country                               | Yes       |
| 2.8.2.2 | DepTime                        | DateTime | Departure date time                                     | Yes       |
| 2.8.3 | Destination                     | Element | Contains destination details                             | Yes       |
| 2.8.3.1 | Airport                        | Element| Contains destination airport details                     | Yes       |
| 2.8.3.1.1 | AirportCode                  | String | IATA code for destination Airport                        | Yes       |
| 2.8.3.1.2 | AirportName                  | String | Name of the destination airport                          | Yes       |
| 2.8.3.1.3 | Terminal                     | String | Terminal Number                                          | Yes       |
| 2.8.3.1.4 | CityCode                     | String | IATA code for destination city                           | Yes       |
| 2.8.3.1.5 | CityName                     | String | Name of the destination city                             | Yes       |
| 2.8.3.1.6 | CountryCode                  | String | IATA code for destination country                        | Yes       |
| 2.8.3.1.7 | CountryName                  | String | Name of the destination country                          | Yes       |
| 2.8.3.2 | ArrTime                        | DateTime | Arrival date time                                       | Yes       |
| 2.8.4 | Airline                        | Element| Element containing the carrier details                  | Yes       |
| 2.8.4.1 | AirlineCode                    | String | IATA code for airline                                    | Yes       |
| 2.8.4.2 | AirlineName                    | String | Name of the airline                                      | Yes       |
| 2.8.4.3 | FlightNumber                   | String | Flight number                                           | Yes       |
| 2.8.4.4 | BookingClass                   | String | Reservation booking designator (Cabin class)            | Yes       |
| 2.8.4.5 | CabinClass                     | String | Cabin class (Economy, PremiumEconomy, Business, First) | Yes       |
| 2.8.4.6 | OperatingCarrier               | String | Operating carrier                                       | Yes       |
| 2.8.5 | JourneyDuration                 | String | Total journey duration in minutes                        | Yes       |
| 2.8.6 | StopQuantity                    | String | Number of stops                                          | Yes       |
| 2.8.7 | Equipment                       | String | Equipment description                                     | Yes       |
| 2.8.8 | SegmentGroup                    | Integer | Segment group ID                                         | No        |
| 2.9   | TotalFare                       | Decimal| Total fare                                              | Yes       |
| 2.10  | TotalFareWithAgentMarkup        | Decimal| Total fare with agent markup                             | Yes       |
| 2.11  | Currency                        | String | Currency                                                | Yes       |
| 2.12  | Availability                    | Integer | Number of available seats                                 | Yes       |
| 2.13  | FareType                        | Enumeration | Fare type (NET, InstantTicketing)                       | Yes       |
| 2.15  | IsMiniRulesAvailable            | Boolean| Indicates whether mini rules are available for the itinerary | No  |
| 3     | Passengers                      | List   | Contains the details of passengers                      | Yes       |
| 3.1   | PassengerIndex                  | String | Passenger index                                         | Yes       |
| 3.2   | Title                           | String | Salutation (Mr, Ms, Mrs)                                | Yes       |
| 3.3   | FirstName                       | String | Passenger's first name                                   | Yes       |
| 3.4   | LastName                        | String | Passenger's last name                                    | Yes       |
| 3.5   | PaxType                         | Enumeration | Type of passenger (Adult, Child, Infant)                | Yes       |
| 3.6   | DateOfBirth                     | String | Passenger's date of birth                                | Yes       |
| 3.7   | Gender                          | Enumeration | Gender (Male, Female)                                   | Yes       |
| 3.8   | PassportNumber                  | String | Passport number                                         | No        |


| 3.9   | CountryOfIssue                  | String | Country of issue for the passport                        | No        |
| 3.10  | IssuedDate                      | DateTime | Date of passport issue                                   | No        |
| 3.11  | ExpiryDate                      | DateTime | Passport expiry date                                     | No        |
| 3.12  | MobileNumber                    | String | Mobile number of passenger                               | Yes       |
| 3.13  | Email                           | String | Email address of passenger                               | Yes       |

#### Sample Response
```json
{
  "BookingID": "FHB201013791",
  "Results": [
    {
      "ExtraServices": {
        "Baggage": [
          {
            "BaggageId": "BG123",
            "Weight": "20",
            "Currency": "USD",
            "Price": "50.00",
            "Origin": "NYC",
            "Destination": "LAX",
            "PaxId": "PAX1"
          }
        ],
        "ResultID": "R123",
        "IsRefundable": true,
        "Fares": [
          {
            "BaseFare": "300.00",
            "Tax": "50.00",
            "Currency": "USD",
            "OtherCharges": "20.00",
            "Discount": "10.00",
            "AgentMarkUp": "15.00",
            "PaxType": "Adult",
            "PassengerCount": 1,
            "ServiceFee": "5.00"
          }
        ],
        "Discount": "5.00",
        "ValidatingCarrier": "AA",
        "LastTicketDate": null,
        "Segments": [
          {
            "TripIndicator": "Outbound",
            "Origin": {
              "Airport": {
                "AirportCode": "JFK",
                "AirportName": "John F. Kennedy International Airport",
                "Terminal": "4",
                "CityCode": "NYC",
                "CityName": "New York",
                "CountryCode": "US",
                "CountryName": "United States"
              },
              "DepTime": "2024-12-01T08:00:00Z"
            },
            "Destination": {
              "Airport": {
                "AirportCode": "LAX",
                "AirportName": "Los Angeles International Airport",
                "Terminal": "1",
                "CityCode": "LAX",
                "CityName": "Los Angeles",
                "CountryCode": "US",
                "CountryName": "United States"
              },
              "ArrTime": "2024-12-01T11:00:00Z"
            },
            "Airline": {
              "AirlineCode": "AA",
              "AirlineName": "American Airlines",
              "FlightNumber": "AA123",
              "BookingClass": "Y",
              "CabinClass": "Economy",
              "OperatingCarrier": "AA"
            },
            "JourneyDuration": "180",
            "StopQuantity": "0",
            "Equipment": "Boeing 737",
            "SegmentGroup": 1
          }
        ],
        "TotalFare": "375.00",
        "TotalFareWithAgentMarkup": "390.00",
        "Currency": "USD",
        "Availability": 5,
        "FareType": "NET",
        "IsMiniRulesAvailable": false
      },
      "Passengers": [
        {
          "PassengerIndex": "1",
          "Title": "Mr",
          "FirstName": "John",
          "LastName": "Doe",
          "PaxType": "Adult",
          "DateOfBirth": "1990-01-01",
          "Gender": "Male",
          "PassportNumber": "123456789",
          "CountryOfIssue": "US",
          "IssuedDate": "2010-01-01",
          "ExpiryDate": "2020-01-01",
          "MobileNumber": "1234567890",
          "Email": "john.doe@example.com"
        }
      ]
    }
  ]
}
```

### Error Responses
| Code | Description                             |
|------|-----------------------------------------|
| 400  | Bad Request: Invalid parameters.        |
| 401  | Unauthorized: Invalid or expired token. |
| 403  | Forbidden: Cancellation not allowed.    |
| 404  | Not Found: Booking ID not found.       |
| 500  | Internal Server Error.                  |

---

Feel free to modify any sections or request additional information!

Here’s a structured stage of documentation for the **AirPromotion** API based on the provided details:

---

## 5.9 AirPromotion API Documentation

### Overview
The **AirPromotion** API allows users to retrieve available promotions for a specified itinerary. It uses the search ID from the AirSearch response and the result ID of the interested itinerary to fetch promotional details.

### Endpoint
- **URL**: `<RootUrl>/AirPromotion`
- **Method**: `POST`

### Headers
- **Authorization**: `Bearer <Token id Received in authentication>`

### Request Structure

#### Request Body
| Level | Element   | Type   | Description                                        | Mandatory |
|-------|-----------|--------|----------------------------------------------------|-----------|
| 1     | SearchID  | String | Search ID received in the AirSearch response       | Yes       |
| 2     | ResultID  | String | Result ID of the interested itinerary from AirSearch response | Yes       |

#### Sample Request
```json
{
  "SearchID": "18f781ce-0c27-468a-8fe0-d0f2ad500c6a",
  "ResultID": "1b123aae-dd05-48e7-b12a-b14436595c50"
}
```

### Response Structure

#### Response Body
| Level | Element       | Type   | Description                                             | Mandatory |
|-------|---------------|--------|---------------------------------------------------------|-----------|
| 1     | PromoCodes    | List   | Contains all available promocodes                       | Yes       |
| 1.1   | Code          | String | Contains the promotion code                              | Yes       |
| 1.2   | Currency      | String | Currency code for the promotion                         | Yes       |
| 1.3   | MaxAmount     | Decimal| Maximum discount amount available                       | Yes       |
| 1.4   | Description   | String | Description of the promotion code                       | Yes       |
| 2     | Error         | Element| Contains error details if any                          | Yes       |
| 2.1   | ErrorCode     | Enumeration | Specific error code (check annexure for details)  | No        |
| 2.2   | ErrorMessage  | String | Description of the error message                        | No        |

#### Sample Response
```json
{
  "PromoCodes": [
    {
      "Code": "FS_1",
      "Currency": "BDT",
      "MaxAmount": 200,
      "Description": "Festive season offer"
    }
  ],
  "Error": null
}
```

### Error Responses
| Code | Description                               |
|------|-------------------------------------------|
| 400  | Bad Request: Invalid parameters.          |
| 401  | Unauthorized: Invalid or expired token.   |
| 404  | Not Found: SearchID or ResultID not found. |
| 500  | Internal Server Error.                    |

---

Feel free to adjust any sections or request further modifications!

Here’s the structured stage of documentation for the **AirCheckPromotion** API based on the provided details:

---

## 5.10 AirCheckPromotion API Documentation

### Overview
The **AirCheckPromotion** API is used to verify the applicability of a promotion code for a selected itinerary. It should be called prior to the **AirPrice** API to ensure the promotion benefits are applied. If the promo code is valid, it will be applied to the selected itinerary.

### Endpoint
- **URL**: `<RootUrl>/AirCheckPromotion`
- **Method**: `POST`

### Headers
- **Authorization**: `Bearer <Token id Received in authentication>`

### Request Structure

#### Request Body
| Level | Element    | Type   | Description                                        | Mandatory |
|-------|------------|--------|----------------------------------------------------|-----------|
| 1     | Promocode  | String | Promotion code to be validated                     | Yes       |
| 2     | SearchID   | String | Search ID received in the AirSearch response       | Yes       |
| 3     | ResultID   | String | Result ID of the interested itinerary from AirSearch response | Yes       |

#### Sample Request
```json
{
  "Promocode": "FS_1",
  "SearchID": "18f781ce-0c27-468a-8fe0-d0f2ad500c6a",
  "ResultID": "1b123aae-dd05-48e7-b12a-b14436595c50"
}
```

### Response Structure

#### Response Body
| Level | Element          | Type       | Description                                             | Mandatory |
|-------|------------------|------------|---------------------------------------------------------|-----------|
| 1     | PromotionDetails  | Element    | Contains promotion details                              | Yes       |
| 1.1   | PromotionCode     | String     | The promotion code                                      | Yes       |
| 1.2   | PromotionCurrency  | String     | Currency of the promotion                               | Yes       |
| 1.3   | AmountApplied     | Decimal    | Amount applied from the promotion                       | Yes       |
| 1.4   | PromotionAmount    | Decimal    | Total amount of the promotion                           | Yes       |
| 1.5   | PromotionPercentage | Decimal    | Percentage value of the promotion                       | Yes       |
| 1.6   | MaxDiscountLimit   | Decimal    | Maximum discount limit for the promotion                | Yes       |
| 1.7   | IsExpired         | Boolean    | Indicates if the promotion is expired                   | Yes       |
| 1.8   | IsLimitExceeds    | Boolean    | Indicates if the usage limit of the promotion has been exceeded | Yes       |
| 1.9   | IsInvalidCode     | Boolean    | Indicates if the promotion code is invalid              | Yes       |
| 2     | ApplyStatus       | Enumeration | Status of the promotion application                     | Yes       |
| 2.1   | Possible values   | -          | 1. Default (Error or Invalid)<br>2. Valid (Promotion code is valid)<br>3. NotAvailable (Promotion code not available)<br>4. Expired (Promotion code expired)<br>5. Exceeds (Promotion code exceeds usage limit) | Yes |
| 3     | Error             | Element    | Contains error details if applicable                   | Yes       |
| 3.1   | ErrorCode         | Enumeration | Specific error code (check annexure for details)      | No        |
| 3.2   | ErrorMessage      | String     | Description of the error message                        | No        |

#### Sample Response
```json
{
  "PromotionDetails": {
    "PromotionCode": "string",
    "PromotionCurrency": "string",
    "AmountApplied": 0,
    "PromotionAmount": 0,
    "PromotionPercentage": 0,
    "MaxDiscountLimit": 0,
    "IsExpired": true,
    "IsLimitExceeds": true,
    "IsInvalidcode": true
  },
  "ApplyStatus": "Error or Invalid",
  "Error": {
    "ErrorCode": "Default",
    "ErrorMessage": "string"
  }
}
```

### Error Responses
| Code | Description                                   |
|------|-----------------------------------------------|
| 400  | Bad Request: Invalid parameters.              |
| 401  | Unauthorized: Invalid or expired token.       |
| 404  | Not Found: Promotion code or itinerary not found. |
| 500  | Internal Server Error.                        |

---

Feel free to make any changes or request additional information!

Here’s the structured stage of documentation for the **AirRemovePromotion** API based on the provided details:

---

## 5.11 AirRemovePromotion API Documentation

### Overview
The **AirRemovePromotion** API is used to remove one or more applied promo codes from a selected itinerary. This action may be required if the user decides to revert the use of previously applied promotions.

### Endpoint
- **URL**: `<RootUrl>/AirRemovePromotion`
- **Method**: `POST`

### Headers
- **Authorization**: `Bearer <Token id Received in authentication>`

### Request Structure

#### Request Body
| Level | Element   | Type          | Description                                   | Mandatory |
|-------|-----------|---------------|-----------------------------------------------|-----------|
| 1     | Promocodes| List of Strings | Contains all promo codes that need to be removed | Yes       |

#### Sample Request
```json
{
  "Promocodes": [
    "FS_1",
    "FS_13"
  ]
}
```

### Response Structure

#### Response Body
| Level | Element | Type   | Description                                        | Mandatory |
|-------|---------|--------|----------------------------------------------------|-----------|
| 1     | Error   | Element| Contains error details if applicable               | Yes       |
| 1.1   | ErrorCode | Enumeration | Specific error code (check annexure for details) | No        |
| 1.2   | ErrorMessage | String   | Description of the error message                   | No        |

### Error Responses
| Code | Description                                   |
|------|-----------------------------------------------|
| 400  | Bad Request: Invalid parameters.              |
| 401  | Unauthorized: Invalid or expired token.       |
| 404  | Not Found: Promo code not found.              |
| 500  | Internal Server Error.                        |

---

Feel free to let me know if you need any modifications or additional details!

Here’s the structured stage of documentation for the **AirGetFlight** API based on the provided details:

---

## 5.12 AirGetFlight API Documentation

### Overview
The **AirGetFlight** API is an optional endpoint that retrieves detailed information about a specific itinerary. This can be useful for users who want to view the specifics of their flight plans, including segments, departure and arrival details, and airline information.

### Endpoint
- **URL**: `<RootUrl>/AirDetails`
- **Method**: `POST`

### Headers
- **Authorization**: `Bearer <Token id Received in authentication>`

### Request Structure

#### Request Body
| Level | Element   | Type   | Description                                   | Mandatory |
|-------|-----------|--------|-----------------------------------------------|-----------|
| 1     | SearchID  | String | Search ID received in the AirSearch response  | Yes       |
| 2     | ResultID  | String | Result ID of the interested itinerary         | Yes       |

#### Sample Request
```json
{
  "SearchID": "18f781ce-0c27-468a-8fe0-d0f2ad500c6a",
  "ResultID": "1b123aae-dd05-48e7-b12a-b14436595c50"
}
```

### Response Structure

#### Response Body
| Level | Element      | Type   | Description                                      | Mandatory |
|-------|--------------|--------|--------------------------------------------------|-----------|
| 1     | FlightDetails| Element| Object containing flight details                  | Yes       |
| 1.1   | Segments     | List   | Contains all flight segments and details         | Yes       |
| 1.1.1 | TripIndicator| Enumeration | Indicates the type of trip (OutBound/InBound)  | Yes       |
| 1.1.2 | Origin       | Element| Contains details of the origin                   | Yes       |
| 1.1.2.1 | Airport    | Element| Object containing details of the airport         | Yes       |
| 1.1.2.1.1 | AirportCode | String | IATA code of the origin airport                  | Yes       |
| 1.1.2.1.2 | AirportName | String | Name of the origin airport                       | No        |
| 1.1.2.1.3 | Terminal   | String | Terminal number                                  | No        |
| 1.1.2.1.4 | CityCode   | String | IATA code of the origin city                     | Yes       |
| 1.1.2.1.5 | CityName   | String | Name of the city                                 | Yes       |
| 1.1.2.1.6 | CountryCode| String | IATA code of the origin country                  | Yes       |
| 1.1.2.1.7 | CountryName| String | Name of the origin country                       | Yes       |
| 1.1.2.2 | DepTime    | DateTime | Departure date and time                          | Yes       |
| 1.1.3 | Destination   | Element| Contains details of the destination              | Yes       |
| 1.1.3.1 | Airport    | Element| Object containing details of the airport         | Yes       |
| 1.1.3.1.1 | AirportCode | String | IATA code of the destination airport             | Yes       |
| 1.1.3.1.2 | AirportName | String | Name of the destination airport                  | No        |
| 1.1.3.1.3 | Terminal   | String | Terminal number                                  | No        |
| 1.1.3.1.4 | CityCode   | String | IATA code of the destination city                | Yes       |
| 1.1.3.1.5 | CityName   | String | Name of the city                                 | Yes       |
| 1.1.3.1.6 | CountryCode| String | IATA code of destination country                 | Yes       |
| 1.1.3.1.7 | CountryName| String | Name of the destination country                  | Yes       |
| 1.1.3.2 | ArrTime    | DateTime | Arrival time                                   | Yes       |
| 1.1.4 | Airline      | Element| Contains airline details                         | Yes       |
| 1.1.4.1 | AirlineCode | String | IATA code of the airline                        | Yes       |
| 1.1.4.2 | AirlineName | String | Name of the carrier                             | Yes       |
| 1.1.4.3 | FlightNumber| String | Flight number                                  | Yes       |
| 1.1.4.4 | BookingClass| String | Reservation Booking Designator                  | Yes       |
| 1.1.4.5 | CabinClass  | String | Cabin class (Economy, Premium Economy, etc.)   | Yes       |
| 1.1.4.6 | OperatingCarrier| String | Operating Carrier                               | Yes       |
| 1.1.5 | Baggage      | String | Baggage and its weight                          | Yes       |
| 1.1.6 | JourneyDuration | String | Total journey duration in minutes               | Yes       |
| 1.1.7 | StopQuantity | String | Number of stops (e.g., 0, 1, 1+)               | Yes       |
| 1.1.8 | Equipment     | String | Equipment description                            | No        |
| 1.2   | Error        | Element| Contains error details if applicable            | Yes       |
| 1.2.1 | ErrorCode    | Enumeration | Specific error code (check annexure for details)| No        |
| 1.2.2 | ErrorMessage | String   | Description of the error message                | No        |

### Sample Response
```json
{
  "FlightDetails": {
    "segments": [
      {
        "TripIndicator": "OutBound",
        "Origin": {
          "Airport": {
            "AirportCode": "DAC",
            "AirportName": "Shahjalal intl. Airport",
            "Terminal": null,
            "CityCode": "DAC",
            "CityName": "Dhaka",
            "CountryCode": "BD",
            "CountryName": "Bangladesh"
          },
          "DepTime": "2020-10-20T15:50:00"
        },
        "Destination": {
          "Airport": {
            "AirportCode": "CGP",
            "AirportName": "Shah Amanat International Airport",
            "Terminal": null,
            "CityCode": "CGP",
            "CityName": "Chittagong",
            "CountryCode": "BD",
            "CountryName": "Bangladesh"
          },
          "ArrTime": "2020-10-20T16:45:00"
        },
        "Airline": {
          "AirlineCode": "VQ",
          "AirlineName": "Novoair",
          "FlightNumber": "911",
          "BookingClass": "U",
          "CabinClass": "Economy",
          "OperatingCarrier": "VQ"
        },
        "Baggage": "Baggage: ADT-20KGS<br/>",
        "JourneyDuration": "55",
        "StopQuantity": "0",
        "Equipment": "ATR725"
      }
    ]
  },
  "Error": null
}
```

### Error Responses
| Code | Description                                   |
|------|-----------------------------------------------|
| 400  | Bad Request: Invalid parameters.              |
| 401  | Unauthorized: Invalid or expired token.       |
| 404  | Not Found: Itinerary details not found.      |
| 500  | Internal Server Error.                        |

---

Let me know if you need any further modifications or additional sections!

Here's a structured documentation stage for the **AirMiniRules** API:

---

### 5.13 AirMiniRules API Documentation

**Description:**
The **AirMiniRules** API retrieves mini fare rules for an itinerary. It is important to note that not all itineraries have associated mini fare rules. The availability of mini fare rules can be checked using the `isMiniRulesAvailable` field in the **AirPrice** API response.

**URL:**
```
<RootUrl>/AirMiniRules
```

**HTTP Method:**
```
POST
```

**Authentication:**
- **Header Key:** Authorization
- **Header Value:** Bearer `<Token id Received in authentication>`

#### Request Parameters

| Level | Element    | Type      | Description                                                                  | Mandatory |
|-------|------------|-----------|------------------------------------------------------------------------------|-----------|
| 1     | SearchID   | String    | Search ID received in the **AirSearch** response.                           | Yes       |
| 2     | ResultID   | String    | Result ID of the interested itinerary received in the **AirSearch** response.| Yes       |

**Sample Request:**
```json
{
    "SearchID": "18f781ce-0c27-468a-8fe0-d0f2ad500c6a",
    "ResultID": "1b123aae-dd05-48e7-b12a-b14436595c50"
}
```

#### Response Parameters

| Level | Element    | Type        | Description                                                               | Mandatory |
|-------|------------|-------------|---------------------------------------------------------------------------|-----------|
| 1     | miniRules  | List        | Contains all the mini rules for the itinerary.                           | Yes       |
| 1.1   | FareRuleType | String      | Type of fare rule.                                                      | Yes       |
| 1.2   | Paxtype    | Enumeration  | Passenger type (1. Adult, 2. Child, 3. Infant).                        | Yes       |
| 1.3   | CityPair   | String      | Origin-Destination city codes.                                          | Yes       |
| 1.4   | CurrencyCode | String      | Currency code.                                                          | No        |
| 1.5   | isRefundable | Boolean     | Indicates whether the price is refundable.                              | Yes       |
| 1.6   | AmountRefundableBeforeDeparture | Decimal | Amount refundable if cancelled before departure.                        | Yes       |
| 1.7   | isRefundableBeforeDeparture | Boolean | Indicates whether the amount is refundable before departure.            | Yes       |
| 1.8   | AmountRefundableAfterDeparture | Decimal | Amount refundable if cancelled after departure.                          | Yes       |
| 1.9   | isRefundableAfterDeparture | Boolean | Indicates whether the amount is refundable after departure.             | Yes       |
| 1.10  | isExchangeable | Boolean    | Indicates whether the itinerary is exchangeable.                        | Yes       |
| 1.11  | AmountExchangeableBeforeDeparture | Decimal | Total amount exchangeable before departure.                             | Yes       |
| 1.12  | isExchangeableBeforeDeparture | Boolean | Indicates if exchangeable before departure.                             | Yes       |
| 1.13  | AmountExchangeableAfterDeparture | Decimal | Amount exchangeable after departure.                                     | Yes       |
| 1.14  | isExchangeableAfterDeparture | Boolean | Indicates if exchangeable after departure.                              | Yes       |
| 1.15  | isPercentage | Boolean     | Indicates if the amount is calculated based on percentage.              | Yes       |
| 1.16  | isNoShow    | Boolean     | Indicates whether the passenger didn't show up.                          | Yes       |
| 2     | Error       | Element     | Contains error details.                                                  | Yes       |
| 2.1   | ErrorCode   | Enumeration  | Check annexure for details.                                             | No        |
| 2.2   | ErrorMessage | String      | Error message description.                                              | No        |

**Sample Response:**
```json
{
    "miniRules": [
        {
            "FareRuleType": "string",
            "Paxtype": "Adult",
            "CityPair": "BLR-DEL",
            "CurrencyCode": "BDT",
            "isRefundable": true,
            "amountRefundableBeforeDeparture": 0,
            "isRefundableBeforeDeparture": true,
            "amountRefundableAfterDeparture": 0,
            "isRefundableAfterDeparture": true,
            "isExchangeable": true,
            "amountExchangeableBeforeDeparture": 0,
            "isExchangeableBeforeDeparture": true,
            "amountExchangeableAfterDeparture": 0,
            "isExchangeableAfterDeparture": true,
            "isPercentage": true,
            "isNoShow": true
        }
    ],
    "Error": null
}
```

**Notes:**
- Ensure that the `SearchID` and `ResultID` provided in the request correspond to valid entries from the **AirSearch** response to successfully retrieve the mini fare rules.
- Handle the `Error` object appropriately in the response to identify any issues with the request.

---

This format provides clarity on how to use the **AirMiniRules** API, including its request structure, response data, and possible error handling. Let me know if you need any further adjustments!

Here's the structured documentation stage for the **GetBalance** API:

---

### 5.16 GetBalance API Documentation

**Description:**
The **GetBalance** API retrieves the current balance for a client. This API is useful for checking the total available balance and credit amount for a specified user.

**URL:**
```
<RootUrl>/GetBalance
```

**HTTP Method:**
```
POST
```

**Authentication:**
- **Header Key:** Authorization
- **Header Value:** Bearer `<Token id Received in authentication>`

#### Request Parameters

| Level | Element   | Type   | Description                          | Mandatory |
|-------|-----------|--------|--------------------------------------|-----------|
| 1     | UserName  | String | User name of the client.            | Yes       |

**Sample Request:**
```json
{
    "UserName": "test@sample.com"
}
```

#### Response Parameters

| Level | Element    | Type      | Description                              | Mandatory |
|-------|------------|-----------|------------------------------------------|-----------|
| 1     | Balance    | Decimal   | Total available balance.                 | Yes       |
| 2     | Credits    | Decimal   | Credit amount limit.                     | Yes       |
| 3     | Status     | Enumeration | Response status. Possible values: <br> 1. Not set <br> 2. Successful <br> 3. Failed | Yes       |
| 4     | Error      | Element   | Contains error details.                  | Yes       |
| 4.1   | ErrorCode  | Enumeration | Check annexure for details.            | No        |
| 4.2   | ErrorMessage | String   | Error message description.              | No        |

**Sample Response:**
```json
{
    "Balance": 1200,
    "Credits": 200,
    "Status": "Successful",
    "Error": null
}
```

**Notes:**
- Ensure that the `UserName` provided in the request is valid to retrieve the correct balance.
- The `Status` field in the response indicates the result of the operation and should be checked to confirm successful retrieval of the balance.
- Handle the `Error` object appropriately in the response to identify any issues with the request.

---

This format outlines how to use the **GetBalance** API, detailing the request and response structures, along with sample data for clarity. Let me know if you need any further modifications or additional information!

Test Cases
Travel partners must execute the following test cases as part of the certification process. JSON Request/Response examples and associated PNR numbers must be submitted for verification. Test cases should be sent to the API team individually rather than combined in a single document.

[Case 1]: Domestic One Way – 1 Adult
[Case 2]: Domestic One Way – 1 Adult + 1 Child
[Case 3]: Domestic Return – 2 Adults
[Case 4]: International One Way – 1 Adult + 1 Child + 1 Infant
[Case 5]: International Return – 2 Adults + 2 Children + 1 Infant
[Case 6]: Multi Way – 2 Adults