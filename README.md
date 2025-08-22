# BuckleVibes

BuckleVibes is a simple Python script that converts soundpacks from MechVibes
into a wav/ folder format compatible with the Buckle buckling spring
keyboard sound simulator.

Got a favorite MechVibes soundpack? Make it far faster using it with bucklespring.

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/p-febis/bucklevibes
cd bucklevibes
```

2. **Install dependencies**
```
pip install -r requirements.txt
```

### Usage

Using the script is straightforward.

1. Unzip a Mechvibes **V1** soundpack in the root of the project
2. Create a wav folder (`mkdir wav`)
3. Run the script
```
python3 main.py
```
4. Copy the wav folder to wherever you have bucklespring stored
5. Profit.
```
./buckle -p wav
```
