from fastapi import FastAPI

# Tạo instance FastAPI
app = FastAPI(
    title="Kanban TODO API",
    description="API đơn giản để quản lý công việc theo mô hình Kanban",
    version="1.0.0"
)

# Route đầu tiên - GET /
@app.get("/")
async def root():
    return {
        "message": "Chào mừng đến với Kanban TODO API!",
        "version": "1.0.0",
        "status": "running"
    }

# Route thứ hai - GET /health
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Kanban TODO API"
    }
