from fastapi import FastAPI


app = FastAPI()


def source():

    return "company"

app.get("/companies")
def get_companies():

    return "Companies on Rader"

app.get("/companies/{id}")
def get_company():

    return "Company"

app.post("/admin/addcompany")
def add_company():
    return "Company Added"

app.get("/sources")
def sources():

    return "Sources"

app.get("/opportunities")
def opportunities():

    return "List of opportunities"

app.get("/opportunities/{id}")
def get_opportunity():

    return "Opportunity"

app.get("/evidence")
def evidence():

    return "Discovered Post or announcements"

app.post("/admin/sources")
def add_source():
    
    return "Source added"

app.post("/admin/collect/{source_id}")
def collect_source():
    
    return "Request an authorized collection run"


app.post("/health")
def health():
    return "Company Added"
