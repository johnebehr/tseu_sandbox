from app.db.models import (
    cope_contributions, 
    dues_and_cope_track_2yrs, 
    dues, 
    mast_agency, 
    mast_city, 
    mast_county, 
    mast_location, 
    mast_organizer, 
    members
)

# Make the tables available
cc = cope_contributions.COPE_Contributions()
d_and_c_2yrs = dues_and_cope_track_2yrs.Dues_And_Cope_Track_2yrs()
dues = dues.Dues()
ma = mast_agency.Mast_Agency()
mc = mast_city.Mast_City()
mco = mast_county.Mast_County()
ml = mast_location.Mast_Location()
mo = mast_organizer.Mast_Organizer()
m = members.Members()