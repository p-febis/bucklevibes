import json
import asyncio
from typing import TypedDict, cast
from ffmpeg.asyncio import FFmpeg


class ConfigV1(TypedDict):
    id: str
    name: str
    sound: str
    defines: dict[str, list[int] | None]


def file_path_from_key_code(keycode: str):
    hex_keycode = "%02x" % int(keycode)
    file_name = f"{hex_keycode}-1.wav"
    return f"wav/{file_name}"


async def main():
    with open("config.json") as file:
        config: ConfigV1 = cast(ConfigV1, json.load(file))

    print(f"Parsing {config['name']}...")

    key_codes = config["defines"].keys()

    awaitables = []

    for keycode in key_codes:
        file_path = file_path_from_key_code(keycode)

        array = config["defines"][keycode]
        if array is None:
            continue

        start_time, duration = int(array[0]) / 1000, int(array[1]) / 1000

        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(config["sound"], ss=start_time, t=duration)
            .output(file_path)
        )

        awaitables.append(ffmpeg.execute())

    await asyncio.gather(*awaitables)
    print("Finished, Enjoy!")


asyncio.run(main())
