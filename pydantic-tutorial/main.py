## Video source for the tutorial: https://www.youtube.com/watch?v=M81pfi64eeM

from datetime import datetime, UTC
from functools import partial
from pydantic import (
    BaseModel, 
    ValidationError, 
    Field, 
    EmailStr, 
    HttpUrl, 
    SecretStr,
    ValidationInfo,
    field_validator,
    model_validator,
    computed_field,
    ConfigDict
)
from typing import Literal, Annotated
from uuid import UUID, uuid4

# Old implementation:
# class User(BaseModel):
#     # variables with type declaration will need to be provided when instantiating the data model
#     uid: int
#     username: str
#     email: str

#     # if default values for variables are provided, then they do not need to be passed during instantiation:
#     bio: str = "This is the default bio"
#     is_active: bool = True

#     # If certain data types are optional, then they can be instantiated as None:
#     full_name: str | None = None
#     verified_on: datetime | None = None

# New implementation:
# Type declarations can be made very descriptive with conditionals to ensure data integrity
# This is achieved using Annotated from typing and Field from pydantic:
class User(BaseModel):
    model_config = ConfigDict(
        validate_by_name=True,
        strict=True, # type coersion will not be allowed with this argument
        extra="allow", # By default, pydantic IGNORES fields that are not described by the data model. Using this flag overrides this behaviour
        # validate_assignment=True # This will revalidate fields after they are reassigned at runtime
        frozen=True # This will make the data immutable. Any reassignment attempt will throw an error.
    )
    # The other literal options for extra= are "ignore", which is the default behaviour
    # and "forbid", which will not allow data objects to be passed in containing any fields that are not defined by the data model.

    # variables with type declaration will need to be provided when instantiating the data model
    # uid: Annotated[int, Field(gt=0)] # Old implementation with integer based IDs
    uid: UUID = Field(alias="id", default_factory=uuid4)
    # The data being imported may have used "id" as the key, but in our Python data model
    # we want the "id" to be mapped to "uid". This is achieved by defining aliases

    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr
    age: Annotated[int, Field(ge=13, le=130)]
    password: SecretStr
    # secret strings will be hidden in the data model

    # if default values for variables are provided, then they do not need to be passed during instantiation:
    website: HttpUrl | None = None
    bio: str = "This is the default bio"
    is_active: bool = True

    # If certain data types are optional, then they can be instantiated as None:
    # full_name: str | None = None
    verified_on: datetime | None = None

    # computed field example:
    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0

    # using decorator functions to validate and sanitise inputs:
    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()
    
    # By default: field_validators are run AFTER pydantic has performed its typechecks
    # If a data object contained a website without https, it would not pass the EmailStr type check
    # The below field validatory, in its current form would not solve the problem as 
    # it would be run AFTER the data object has already failed the pydantic type check
    # NEED to use the parameter mode="before" in field_validator to ensure the validation check
    # is performed BEFORE pydantic's typecheck at runtime

    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

    # Need the below validator to work with serialised json input
    @field_validator("uid", mode="before")
    @classmethod
    def cast_to_uuid(cls, v: str | UUID) -> UUID:
        if isinstance(v, str):
            return UUID(v)
        return v

    # Best practices for using validators:
    # Always return the datatype from the validator, or raise an error.
    # The error raised should be a ValueError, which gets converted to a ValidationError by Pydantic
    # Do not mutate the original data value before raise exception clauses, mutate data after the failure checks

    # Computed fields are calculated at runtime when they are called.
    # computed_fields are written as properties of the data model:

    @computed_field
    @property # The property decorator is not needed here as it is coerced by computed_field. BUT mypy will throw warning. Removing the property decorator will cause IDE intellisense to fail. So, pick your poison.
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10_000

# model_validator allows for comparison between different fields within the data model:
# this can have certain use cases in the data validation workflow
class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

# BlogPost data model version 1:
# class BlogPost(BaseModel):
#     title: Annotated[str, Field(min_length=1, max_length=200)]
#     content: Annotated[str, Field(min_length=10)]
#     author_id: str | int

#     view_count: int = 0
#     is_published: bool = False

#     tags: list[str] = Field(default_factory=list) # Instantiate an empty list the safe way

#     # created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
#     # default_factory expects a callable, so we need to pass datetime.now() as a lambda function
#     # the other way of doing this is to use partial from functools:
#     created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
#     # you pass in the callable to partial, with the kwargs to call it

#     status: Literal["draft", "published", "archived"] = "draft"
#     slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

# BlogPost version 2 with nested data models:
# author_id's type is changed to User
# comments list is added which is a list of Comment objects
# Pydantic recursively checks all the nested data models
class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author: User

    view_count: int = 0
    is_published: bool = False

    tags: list[str] = Field(default_factory=list) # Instantiate an empty list the safe way

    # created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))
    # default_factory expects a callable, so we need to pass datetime.now() as a lambda function
    # the other way of doing this is to use partial from functools:
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    # you pass in the callable to partial, with the kwargs to call it

    status: Literal["draft", "published", "archived"] = "draft"
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

    comments: list[Comment] = Field(default_factory=list)

# Special type annotations will need to be added to the repo which are separate to the base pydantic module
# Example: uv add pydantic[email] for email-specific type annotations

if __name__ == "__main__":
    # Old implementation:
    # user = User(
    #     uid=123,
    #     username="johndoe",
    #     email="johndoe@email.com",
    #     age=30
    # )
    # print(user)

    # New implementation:
    user = User(
        username="JohnDoe",
        email="johndoe@email.com",
        age=39,
        password=SecretStr("secret123"),
        website="johndoe.com" # type: ignore
    )
    print(user)
    # Because password is of type SecretStr, it will show up as blurred in print outputs
    # To view secret strings, need to use the appropriate getter method:
    print(user.password.get_secret_value())

    # input sanitisation: JohnDoe was changed to johndoe due to the field_validator
    # computed field checks:
    print(user.is_influencer)
    print(user.display_name)


    # By default, the BaseModel of pydantic is mutable.
    # Changing the value of a variable at runtime will not initiate a re-checking of the type
    
    # user.bio = 57
    # print(user.bio)

    # Even though the type of bio is hinted as string, it can be changed to an int at runtime
    # without pydantic throwing an error

    print(user.model_dump_json())
    # Serialise the data object to store locally or send over the network

    # The main purpose of pydantic is to validate data types align with set contracts
    # If the data doesn't align to the contract, then errors are thrown, which can be handled:

    # try:
    #     user2 = User(
    #         uid="123",
    #         username=None,
    #         email=123
    #     )
    # except ValidationError as e:
    #     print(e)

    # In the error message, there was no error for the uid in the above example
    # This is because type coersion is enabled by default in pydantic.
    # This means that pydantic converted "123" into an integer under the hood.
    # However, if such type coersion cannot be done successfully, like Int("test"),
    # then it would have thrown an error for uid as well.

    # Trying to create a data object that violates conditionals set for the fields:
    test = 1
    try:
        user2 = User(
            username="cs",
            email="johndoe@email.com",
            age=12,
            password=SecretStr("secret123")
        )
    except ValidationError as e:
        print(e)

    # This will throw descriptive error messages for each of the fields violating the field conditionals

    ### BlogPost Dictionary
    # In a recursive fashion, pydantic will check that the below json object satisfies
    # the BlogPost, User and Comment data models
    # If any is violated, pydantic will throw ValidationError.
    post_data = {
        "title": "Understanding Pydantic Models",
        "content": "Pydantic makes data validation easy and intuitive...",
        "slug": "understanding-pydantic",
        "author": {
            "username": "johndoe",
            "email": "JohnDoe@gmail.com",
            "age": 39,
            "password": "secret123",
        },
        "comments": [
            {
                "content": "I think I understand nested models now!",
                "author_email": "student@example.com",
                "likes": 25,
            },
            {
                "content": "Can you cover FastAPI next?",
                "author_email": "viewer@example.com",
                "likes": 15,
            },
        ],
    }

    # post = BlogPost(**post_data) # This method caused too many mypy errors to pop up
    post = BlogPost.model_validate(post_data)

    print(post.model_dump_json(indent=2))

    ### User Dictionary
    user_data = {
        "id": "3bc4bf25-1b73-44da-9078-f2bb310c7374",
        "username": "JohnDoe",
        "email": "JohnDoe@gmail.com",
        "age": 39,
        "password": "secret123",
    }
    user = User.model_validate(user_data)

    # serialising with the Python datamodel keys:
    print(user.model_dump_json(indent=2)) # uid is the key

    # serialising with the alias key names:
    print(user.model_dump_json(indent=2, by_alias=True)) # id is the key

    # exclusion filter for serialisation:
    print(user.model_dump_json(indent=2, by_alias=True, exclude={"password"}))

    # inclusion filter for serialisation:``
    print(user.model_dump_json(indent=2, by_alias=True, include={"username", "email"}))
