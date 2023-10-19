"""Entry point of application."""


from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from starlette.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

app = FastAPI(title='Deepra test assignment.')


EXCEPTION_MSG = '<h1>{status_code}</h1>'


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException,
) -> HTMLResponse:
    """Show error message.

    Args:
        request: Request that produce exception.
        exc: Handled exception.

    Returns:
        Response with error.
    """
    return HTMLResponse(EXCEPTION_MSG.format(status_code=exc.status_code))


BAD_REQUEST_MSG = """
<h1>Bad request</h1>

<p>You forgot `name` and `message` params. \
Try got to the <a href="/?name=Rekruto&message=Давай дружить!">URL</a></p>
"""


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: HTTPException,
) -> HTMLResponse:
    """Show error message with params hint.

    Args:
        request: Request that produce exception.
        exc: Handled exception (RequestValidationError actually).

    Returns:
        Response with error and hint.
    """
    return HTMLResponse(
        BAD_REQUEST_MSG,
        status_code=HTTP_400_BAD_REQUEST,
    )


GREET_MSG = """
<h1>Hello {name}!</h1>

<p>{message}</p>
"""


@app.get('/')
async def greet(name: str, message: str) -> HTMLResponse:
    """Greet user with provided name and message.

    Args:
        name: Greetee name.
        message: Greeting message.

    Returns:
        "Hello {name}! {message}!"
    """
    return HTMLResponse(
        GREET_MSG.format(
            name=name,
            message=message,
        ),
        status_code=HTTP_200_OK,
    )
