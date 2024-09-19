from ..models.topic import Topic, db
from ..utils.functions import create_http_response
from  .auth import authentication_required
from ..utils.validations import input_validation
from flask import Response


def get_topics() -> tuple[Response, int]:
    try:
        topics = db.session.execute(db.select(Topic)).scalars().all()
        return create_http_response(result=topics, status="success", http_status=200)
    except Exception as e:
        return create_http_response(message=f"unexpected error: {e}", status="failed", http_status=500)


@authentication_required
@input_validation(
    name={"required": True, "min_length": 3},
)
def create_topic(request_data: dict) -> tuple[Response, int]:
    name = request_data.get('name')
    already_existing_topic = db.session.execute(db.select(Topic).where(Topic.name == name)).scalar()
    if already_existing_topic:
        return create_http_response(message='already existing topic with that name', status='failed', http_status=400)

    new_topic = Topic(
        name=name
    )

    db.session.add(new_topic)
    db.session.commit()

    return create_http_response(
        message='Successfully created topic',
        status='success',
        http_status=201
    )
