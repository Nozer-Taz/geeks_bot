from aiogram import executor
from config import dp
from handlers import (
    start,
)











if __name__ == "__main__":
    executor.start_polling(
        dp
    )
