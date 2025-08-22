# BuckleVibes

BuckleVibes is a simple Python script that converts soundpacks from MechVibes
into a `wav` folder format compatible with [bucklespring](https://github.com/zevv/bucklespring).

Got a favorite MechVibes soundpack? Make it far faster using it with bucklespring.

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/p-febis/bucklevibes
cd bucklevibes
```

2. **Install ffmpeg**
This script depends on ffmpeg, it should be available on your system.

3. **Install dependencies**
```
pip install -r requirements.txt
```

### Usage

**Basic Example**
1. Place your unzipped MechVibes soundpack folder (e.g. `my_soundpack`)
inside the `bucklevibes` directory

2. Run the script, specifying the soundpack folder as the input
```
python3 main.py -i my_soundpack
```

This will automatically create a `wav` folder in the root of the project.
If you would like to use another folder name, specify it with the `-o` flag.


### Using with Bucklespring

Once the script is finished:
1. Copy the generated output folder (e.g. `wav`) to the directory where your
bucklespring executable is located.

2. Run bucklespring and point it to your new sound folder.
```
./buckle -p wav
```
3. Profit!
