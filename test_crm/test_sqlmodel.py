from typing import Optional, List

from sqlmodel import SQLModel, create_engine, Session, Field
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

# 定义一个类
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str


database_url = "sqlite:///./test1.db"
engine = create_engine(database_url)
# engine = create_async_engine(database_url)


# 创建用户
def create_user(user: User):
    with Session(engine) as session:
        with session.begin():
            session.add(user)
            session.commit()


'''根据用户查询'''
def select_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user

'''根据用户名称查询'''
def select_user_by_name(username: str) -> List[User]:
    with Session(engine) as session:
        query = session.query(User).filter(User.name == username)
        users = query.all()
        return users


'''更新用户'''
def update_user(user: User):
    with Session(engine) as session:
        with session.begin():
            # session.update(user)
            session.merge(user)
            session.commit()


'''删除用户'''
def del_user(user: User):
    with Session(engine) as session:
        with session.begin():
            session.delete(user)
            session.commit()


# async def main():
#     # 关键字构建对象
#     user = User(id=3, name="test1", email="test@bac.com")
#     # 字典构建
#     # user_data = {"id": 4, "name": "test2", "email": "test2@abc.com"}
#     # user1 = User(**user_data)
#     await create_user(user)
#     user_res = await select_user(3)
#     print(user_res)
#

 # Create the table if it doesn't exist
User.metadata.create_all(engine)
if __name__ == '__main__':
    user = User(id=3, name="test5", email="test@bac.com")
    # 字典构建
    # user_data = {"id": 4, "name": "test2", "email": "test2@abc.com"}
    # user1 = User(**user_data)
    try:
        create_user(user)
        # user = select_user(3)
        users = select_user_by_name("test5")
        for user in users:
            print(user)
        # update_user(user)
        # print("1:",user)
        # del_user(user)
        # print("2:",user)
    except Exception as e:
        print("error",e)



