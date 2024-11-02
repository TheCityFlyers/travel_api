from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class Airport(BaseModel):
    code: str
    name: str
    city: str
    country: str
    terminal: Optional[str] = None

class Airline(BaseModel):
    code: str
    name: str
    flight_number: str

class FlightSegmentResponse(BaseModel):
    departure: Airport
    arrival: Airport
    airline: Airline
    departure_time: datetime
    arrival_time: datetime
    duration: int  # in minutes
    cabin_class: str
    booking_class: str
    stops: int
    baggage_allowance: str

class FareBreakdown(BaseModel):
    passenger_type: str
    passenger_count: int
    base_fare: float
    taxes: float
    total: float

class FlightOffer(BaseModel):
    offer_id: str
    provider: str  # "bdfare" or "flyhub"
    validating_carrier: str
    is_refundable: bool
    segments: List[FlightSegmentResponse]
    fare_breakdowns: List[FareBreakdown]
    total_fare: float
    currency: str
    available_seats: int
    last_ticketing_date: Optional[datetime] = None 