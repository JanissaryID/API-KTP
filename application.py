from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import database.crud as crud
import database.model as model
import database.schema as schema
from database.db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Machine Details",
    description="You can perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/ktp', response_model=List[schema.KTP])
def retrieve_all_ktp_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ktp = crud.get_ktp(db=db, skip=skip, limit=limit)
    return ktp


@app.post('/add', response_model=schema.KtpAdd)
def add_new_ktp(ktp: schema.KtpAdd, db: Session = Depends(get_db)):
    ktp_nik = crud.get_ktp_by_person_nik(db=db, nik_person=ktp.nik)
    if ktp_nik:
        raise HTTPException(status_code=400, detail=f"KTP NIK {ktp.nik_person} already exist in database: {ktp_nik}")
    return crud.add_ktp_details_to_db(db=db, ktp=ktp)


@app.delete('/delete')
def delete_ktp_by_nik(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_ktp_by_nik(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_ktp_details_by_nik(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update', response_model=schema.KTP)
def update_ktp_details(sl_id: int, update_param: schema.UpdateKtp, db: Session = Depends(get_db)):
    details = crud.get_ktp_by_nik(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_ktp_details(db=db, details=update_param, sl_id=sl_id)