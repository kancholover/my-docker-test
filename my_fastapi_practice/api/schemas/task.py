from pydantic import BaseModel, Field


class TaskBase(BaseModel): 
    title: str | None = Field(None, example = "세탁소에 맡긴 것을 찾으러 가기")

class TaskCreate(TaskBase): #POST 함수용, 미구현
    pass

class TaskCreateResponse(TaskCreate): #TaskCreate의 응답
    id: int

    class Config:
        orm_mode = True #DB에 접속할 때 사용, 미구현

class Task(TaskBase):
    id: int
    done: bool = Field(False, description = "완료 플래그")

    class Config:
        orm_mode = True