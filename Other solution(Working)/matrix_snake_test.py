import asyncio
import async_matrix_snake as ams

print(asyncio.run(ams.get_matrix("https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt")))