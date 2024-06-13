from datetime import UTC, datetime
from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import SProductReviewIn, SProductReviewOut


product_review_router = Router(tags=["Reviews"])


@product_review_router.post(
    "{product_id}/reviews/",
    response={
        200: ApiResponse[SProductReviewOut],
    },
    operation_id="CreateReview",
)
def create_review_product(
    request: HttpRequest,
    product_id: int,  # noqa
    token: str,  # noqa
    review: SProductReviewIn,
) -> ApiResponse[SProductReviewOut]:
    return ApiResponse(
        data=SProductReviewOut(
            rating=review.rating,
            text=review.text,
            id=1,
            created_at=datetime.now(UTC),
            updated_at=None,
        )
    )
