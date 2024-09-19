from models import db, Record

class RecordService:
    
    @staticmethod
    def add_record(emotion_name, likelihood_score, colour_displayed, record_date, colour_match):
        new_record = Record(
            emotion_name=emotion_name,
            likelihood_score=likelihood_score,
            colour_displayed=colour_displayed,
            record_date=record_date,
            colour_match=colour_match
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record

    @staticmethod
    def get_records():
        return Record.query.all()

    @staticmethod
    def find_record_by_id(record_id):
        return Record.query.get(record_id)
    
    @staticmethod
    def delete_record(record_id):
        record = Record.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False
    
    @staticmethod
    def update_record(record_id, emotion_name=None, likelihood_score=None, colour_displayed=None, record_date=None, colour_match=None):
        record = Record.query.get(record_id)
        if not record:
            return None
        
        if emotion_name is not None:
            record.emotion_name = emotion_name
        if likelihood_score is not None:
            record.likelihood_score = likelihood_score
        if colour_displayed is not None:
            record.colour_displayed = colour_displayed
        if record_date is not None:
            record.record_date = record_date
        if colour_match is not None:
            record.colour_match = colour_match

        db.session.commit()
        return record
