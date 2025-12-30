from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.room_stay import router as room_stay_router
from app.api.invoice import router as invoice_router
from app.api.person import router as person_router
from app.api.payment import router as payment_router
from app.api.room import router as room_router
from app.api.room_stay_person import router as room_stay_person_router
from app.api.dashboard import router as dashboard_router

app = FastAPI(
    title="Hotel Management System",
    version = "1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(room_stay_router)
app.include_router(person_router)
app.include_router(payment_router)
app.include_router(room_router)
app.include_router(invoice_router)
app.include_router(room_stay_person_router)
app.include_router(dashboard_router)

@app.get("/health")
def health_check():
    return {
        "status" : "ok"
    }
