import argparse
import json
import asyncio
import os
from typing import TypedDict, cast
from ffmpeg.asyncio import FFmpeg


class ConfigV1(TypedDict):
    id: str
    name: str
    sound: str
    defines: dict[str, list[int] | str | None]


tool_config = {
    "input_folder": ".",
    "output_folder": "wav",
}


async def main():
    handle_arguments()
    make_output_directory()

    with open(resolve_input_path("config.json")) as file:
        config: ConfigV1 = cast(ConfigV1, json.load(file))

    print(f"Parsing {config['name']}...")

    input_path = resolve_input_path(config["sound"])
    key_codes = config["defines"].keys()

    awaitables = []

    for keycode in key_codes:
        file_path = resolve_output_path(file_name_from_key_code(keycode))

        resource = config["defines"][keycode]
        if resource is None:
            continue

        if isinstance(resource, str):
            awaitables.append(
                FFmpeg()
                .option("y")
                .input(resolve_input_path(resource))
                .output(file_path)
                .execute()
            )
            continue

        array = resource

        start_time, duration = int(array[0]) / 1000, int(array[1]) / 1000

        ffmpeg = (
            FFmpeg()
            .option("y")
            .input(input_path, ss=start_time, t=duration)
            .output(file_path)
        )

        awaitables.append(ffmpeg.execute())

    await asyncio.gather(*awaitables)
    print("Finished, Enjoy!")


def resolve_input_path(file_path: str):
    return os.path.join(tool_config["input_folder"], file_path)


def resolve_output_path(file_path: str):
    return os.path.join(tool_config["output_folder"], file_path)


def file_name_from_key_code(keycode: str):
    hex_keycode = "%02x" % int(keycode)
    return f"{hex_keycode}-1.wav"


def handle_arguments():
    parser = argparse.ArgumentParser(prog="python3 main.py")
    parser.add_argument("-i", "--input", help="Set the input folder")
    parser.add_argument("-o", "--output", help="Set the output folder")
    arguments = parser.parse_args()

    if arguments.input:
        tool_config["input_folder"] = str(arguments.input)

    if arguments.output:
        tool_config["output_folder"] = str(arguments.output)


def make_output_directory():
    os.makedirs(resolve_output_path(""), exist_ok=True)


asyncio.run(main())
