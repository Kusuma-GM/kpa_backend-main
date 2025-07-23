from pydantic import BaseModel
from datetime import date
from typing import Dict, Any

class WheelFields(BaseModel):
    treadDiameterNew: str
    lastShopIssueSize: str
    condemningDia: str
    wheelGauge: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelProfile: str
    intermediateWWP: str
    bearingSeatDiameter: str
    rollerBearingOuterDia: str
    rollerBearingBoreDia: str
    rollerBearingWidth: str
    axleBoxHousingBoreDia: str
    wheelDiscWidth: str

class WheelSpecCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields

class WheelSpecResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, Any]

class BogieDetails(BaseModel):
    bogieNo: str
    makerYearBuilt: str
    incomingDivAndDate: str
    deficitComponents: str
    dateOfIOH: date

class BogieChecksheetSection(BaseModel):
    bogieFrameCondition: str
    bolster: str
    bolsterSuspensionBracket: str
    lowerSpringSeat: str
    axleGuide: str

class BMBCChecksheet(BaseModel):
    cylinderBody: str
    pistonTrunnion: str
    adjustingTube: str
    plungerSpring: str

class BogieChecksheetCreate(BaseModel):
    formNumber: str
    inspectionBy: str
    inspectionDate: date
    bogieDetails: BogieDetails
    bogieChecksheet: BogieChecksheetSection
    bmbcChecksheet: BMBCChecksheet

class BogieChecksheetResponse(BaseModel):
    success: bool
    message: str
    data: Dict[str, Any]