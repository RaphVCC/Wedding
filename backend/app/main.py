from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
import os
import sys

# Health check endpoint primeiro (antes de qualquer import que pode falhar)
app = FastAPI(title="Wedding Website API")

@app.get("/health")
def health():
    return {"status": "ok", "message": "Server is running"}

# Agora importa o resto
try:
    from app.core.config import settings
    from app.core.database import engine, Base
    
    # Criar tabelas
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Warning: Could not create tables: {e}", file=sys.stderr)
    
    # CORS middleware
    cors_origins = getattr(settings, 'CORS_ORIGINS', ['*'])
    if not cors_origins or cors_origins == ['*']:
        cors_origins = ['*']
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Static files for uploads
    try:
        static_dir = Path(settings.STATIC_DIR)
        static_dir.mkdir(parents=True, exist_ok=True)
        app.mount("/static", StaticFiles(directory=static_dir), name="static")
    except Exception as e:
        print(f"Warning: Could not mount static files: {e}", file=sys.stderr)
    
except Exception as e:
    print(f"Error initializing app: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()

# Include routers (importante: antes do catch-all do frontend)
try:
    from app.routers import (
        auth, home, story, info, timeline, gallery, gifts, rsvp, upload
    )
    app.include_router(auth.router)
    app.include_router(home.router)
    app.include_router(story.router)
    app.include_router(info.router)
    app.include_router(timeline.router)
    app.include_router(gallery.router)
    app.include_router(gifts.router)
    app.include_router(rsvp.router)
    app.include_router(upload.router)
except Exception as e:
    print(f"Warning: Could not load some routers: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()

# Serve frontend static files
try:
    frontend_dist = Path(__file__).parent.parent / "frontend_dist"
    if frontend_dist.exists() and (frontend_dist / "index.html").exists():
        assets_dir = frontend_dist / "assets"
        if assets_dir.exists():
            app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")
        
        @app.get("/{full_path:path}")
        async def serve_frontend(full_path: str, request: Request):
            if full_path.startswith(("api/", "auth/", "static/", "docs", "openapi.json", "redoc", "health")):
                raise HTTPException(status_code=404, detail="Not found")
            index_path = frontend_dist / "index.html"
            if index_path.exists():
                return FileResponse(index_path)
            raise HTTPException(status_code=404, detail="Frontend not found")
    else:
        @app.get("/")
        def root():
            return {"message": "Wedding Website API", "status": "running", "frontend": "not built"}
except Exception as e:
    print(f"Warning: Could not setup frontend: {e}", file=sys.stderr)
    @app.get("/")
    def root():
        return {"message": "Wedding Website API", "status": "running"}


@app.on_event("startup")
async def startup_event():
    try:
        from app.core.database import SessionLocal
        from app.models.admin_user import AdminUser
        from app.core.security import get_password_hash
        from app.core.config import settings
        
        db = SessionLocal()
        try:
            admin = db.query(AdminUser).filter(AdminUser.username == settings.ADMIN_USERNAME).first()
            if not admin:
                admin = AdminUser(
                    username=settings.ADMIN_USERNAME,
                    hashed_password=get_password_hash(settings.ADMIN_PASSWORD)
                )
                db.add(admin)
                db.commit()
        except Exception as e:
            print(f"Warning: Could not create admin user: {e}", file=sys.stderr)
        finally:
            db.close()
    except Exception as e:
        print(f"Warning: Startup error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()

