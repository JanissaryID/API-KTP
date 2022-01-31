from sqlalchemy.orm import Session
import database.model as model
import database.schema as schema


def get_ktp_by_person_nik(db: Session, nik_person: int):
    return db.query(model.KTPModel).filter(model.KTPModel.nik == nik_person).first()


def get_ktp_by_nik(db: Session, sl_id: int):
    return db.query(model.KTPModel).filter(model.KTPModel.nik == sl_id).first()


def get_ktp(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.KTPModel).offset(skip).limit(limit).all()


def add_ktp_details_to_db(db: Session, ktp: schema.KtpAdd):
    ktp_details = model.KTPModel(
        nik=ktp.nik,
        name=ktp.name,
        status=ktp.status
    )
    db.add(ktp_details)
    db.commit()
    db.refresh(ktp_details)
    return model.KTPModel(**ktp.dict())


def update_ktp_details(db: Session, sl_id: int, details: schema.UpdateKtp):
    db.query(model.KTPModel).filter(model.KTPModel.nik == sl_id).update(vars(details))
    db.commit()
    return db.query(model.KTPModel).filter(model.KTPModel.nik == sl_id).first()


def delete_ktp_details_by_nik(db: Session, sl_id: int):
    try:
        db.query(model.KTPModel).filter(model.KTPModel.nik == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)