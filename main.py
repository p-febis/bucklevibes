import json
import asyncio
from typing import TypedDict, cast
from ffmpeg.asyncio import FFmpeg

class ConfigV1(TypedDict):
    id: str
    name: str
    sound: str
    defines: dict[str, list[int] | None]


async def main():
    with open("config.json") as file:
        config: ConfigV1 = cast(ConfigV1, json.load(file))

    print(f"Parsing {config['name']}...")

    key_codes = config['defines'].keys()

    awaitables = []

    for key_code in key_codes:
        hex_keycode = "%02x" % int(key_code)
        file_name = f"{hex_keycode}-1.wav"
        file_path = f"wav/{file_name}"

        array = config["defines"][key_code]
        if array is None:
            continue


        start_time, duration = int(array[0]) / 1000, int(array[1]) / 1000
        
        ffmpeg = FFmpeg().option("y").input(config["sound"], ss=start_time, t=duration).output(file_path)
        awaitables.append(ffmpeg.execute())

    await asyncio.gather(*awaitables)

asyncio.run(main())
