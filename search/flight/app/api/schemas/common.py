from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class CabinClass(str, Enum):
    ECONOMY = "Economy"
    PREMIUM_ECONOMY = "PremiumEconomy" 
    BUSINESS = "Business"
    FIRST = "First"

class TripType(str, Enum):
    ONEWAY = "Oneway"
    RETURN = "Return"
    CIRCLE = "Circle"

class PassengerType(str, Enum):
    ADULT = "ADT"
    CHILD = "CHD"
    INFANT = "INF"

class Passenger(BaseModel):
    pax_id: str = Field(..., example="PAX1")
    ptc: PassengerType

class OriginDestRequest(BaseModel):
    origin_dep_request: dict = Field(..., example={
        "iatA_LocationCode": "DAC",
        "date": "2024-03-25"
    })
    dest_arrival_request: dict = Field(..., example={
        "iatA_LocationCode": "CXB"
    })

class FlightSearchRequest(BaseModel):
    point_of_sale: str = Field(..., example="BD")
    origin_dest: List[OriginDestRequest]
    pax: List[Passenger]
    shopping_criteria: dict = Field(..., example={
        "tripType": "Oneway",
        "travelPreferences": {
            "vendorPref": [],
            "cabinCode": "Economy"
        },
        "returnUPSellInfo": True
    })
