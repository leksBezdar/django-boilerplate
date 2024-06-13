from django.http import HttpRequest
from ninja import Header, Router
from ninja.errors import HttpError

from core.api.schemas import ApiResponse
from core.api.v1.reviews.schemas import SProductReviewIn, SProductReviewOut
from core.apps.common.exceptions import ServiceException
from core.apps.products.use_cases.reviews.create import CreateProductReviewUseCase
from core.project.containers import init_container


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
    product_id: int,
    review: SProductReviewIn,
    token: str = Header(alias="Auth-Token"),
) -> ApiResponse[SProductReviewOut]:
    container = init_container()
    create_use_case: CreateProductReviewUseCase = container.resolve(
        CreateProductReviewUseCase
    )

    try:
        created_review = create_use_case.execute(
            token=token,
            product_id=product_id,
            review=review.to_entity(),
        )
    except ServiceException as e:
        raise HttpError(status_code=400, message=e.message)

    return ApiResponse(data=SProductReviewOut.from_entity(created_review))
