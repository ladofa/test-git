import asyncio
import time

async def task(name, delay):
    print(f"작업 {name} 시작: {time.strftime('%X')}")
    await asyncio.sleep(delay)  # 비동기적 대기
    print(f"작업 {name} 종료: {time.strftime('%X')}")

async def main():
    # task("A", 2)
    # task("B", 3)
    # task("C", 1)

    await asyncio.gather(
        task("A", 2),
        task("B", 3),
        task("C", 1)
    )

print(f"프로그램 시작: {time.strftime('%X')}")
asyncio.run(main())
print(f"프로그램 종료: {time.strftime('%X')}")