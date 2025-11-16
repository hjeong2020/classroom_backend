from sqlmodel import Field, SQLModel



class StudentBase(SQLModel):
    name: str = Field(index=True)
    english_name: str = Field(index=True)
    homework_point: int = Field(default=0)
    class_point: int = Field(default=0)
    total_points: int = Field(default=0)


class Student(StudentBase, table=True):
    id: int = Field(default=None, primary_key=True)


